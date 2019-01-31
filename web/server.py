import os
import collections
from configparser import ConfigParser

import jinja2
from sanic import Sanic
from sanic import response
from sanic_session import Session
from sanic_jinja2 import SanicJinja2
from sanic.exceptions import NotFound


LESSON_ROOT = os.environ.get('LESSON_ROOT')
if not LESSON_ROOT:
    raise ValueError('$LESSON_ROOT not set')

if not os.path.exists(LESSON_ROOT):
    raise ValueError('$LESSON_ROOT {}')

app = Sanic()
Session(app)

jinja = SanicJinja2(app)
#
# Specify the package name, if templates/ dir is inside module
# jinja = SanicJinja2(app, pkg_name='sanicapp')
# or use customized templates path
# jinja = SanicJinja2(app, pkg_name='sanicapp', pkg_path='other/templates')
# or setup later
# jinja = SanicJinja2()
# jinja.init_app(app)

def render_rst(rst_filename):

    from docutils import core
    from docutils.writers.html4css1 import Writer,HTMLTranslator

    class HTMLFragmentTranslator( HTMLTranslator ):
        def __init__( self, document ):
            HTMLTranslator.__init__( self, document )
            self.head_prefix = ['','','','','']
            self.body_prefix = []
            self.body_suffix = []
            self.stylesheet = []
        def astext(self):
            return ''.join(self.body)

    html_fragment_writer = Writer()
    html_fragment_writer.translator_class = HTMLFragmentTranslator

    def reST_to_html( s ):
        result = core.publish_string( s, writer = html_fragment_writer )
        result = result.decode('utf8')
        return result

    fn = os.path.join(os.path.dirname(__file__), 'content', rst_filename)
    if not os.path.exists(fn):
        raise IOError('RST file {} not found'.format(fn))
    with open(fn) as fp:
        rst_data = fp.read()
    return reST_to_html(rst_data)


@app.route('/')
@jinja.template('index.html')  # decorator method is staticmethod
async def index(request):
    request['flash']('success message', 'success')
    request['flash']('info message', 'info')
    request['flash']('warning message', 'warning')
    request['flash']('error message', 'error')
    return {'greetings': 'Hello, sanic!'}

@app.route('/introduction')
@jinja.template('content.html')  # decorator method is staticmethod
async def introduction(request):
    return {'body': render_rst('intro.rst')}

@app.route('/tools')
@jinja.template('content.html')  # decorator method is staticmethod
async def tools(request):
    return {'body': render_rst('tools.rst')}

@app.route('/references')
@jinja.template('content.html')  # decorator method is staticmethod
async def references(request):
    return {'body': render_rst('references.rst')}

@app.route('/related')
@jinja.template('content.html')  # decorator method is staticmethod
async def related(request):
    return {'body': render_rst('related.rst')}

@app.route('/discussion')
@jinja.template('content.html')  # decorator method is staticmethod
async def discussion(request):
    return {'body': render_rst('discussion.rst')}

@app.route('/blog')
@jinja.template('content.html')  # decorator method is staticmethod
async def blog(request):
    return {'body': render_rst('blog.rst')}

@app.route('/about')
@jinja.template('content.html')  # decorator method is staticmethod
async def about(request):
    return {'body': render_rst('about.rst')}


@app.route('/lesson/<lesson>/download/images/<vendor>/<filename>')
async def download_image(request, lesson, vendor, filename):

    lesson_dir = os.path.join(LESSON_ROOT, lesson)
    if not os.path.exists(lesson_dir):
        raise NotFound('Lession {} does not exist'.format(lesson))

    download_fn = os.path.join(lesson_dir, 'images', vendor, filename)
    if not os.path.exists(download_fn):
        raise NotFound('Download filename {} does not exist'.format(download_fn))
    return await response.file(download_fn)

@app.route('/lesson/<lesson>/download/<filename>')
async def download_pdf(request, lesson, filename):

    lesson_dir = os.path.join(LESSON_ROOT, lesson)
    if not os.path.exists(lesson_dir):
        raise NotFound('Lession {} does not exist'.format(lesson))

    download_fn = os.path.join(lesson_dir, filename)
    if not os.path.exists(download_fn):
        raise NotFound('Download filename {} does not exist'.format(download_fn))
    return await response.file(download_fn)


@app.route('/lessons')
@jinja.template('lessons.html')  # decorator method is staticmethod
async def lessons(request):

    compliance = collections.OrderedDict()
    compliance['intro'] = []
    compliance['advanced'] = []
    compliance['special'] = []

    for lesson in os.listdir(LESSON_ROOT):
        if not lesson.startswith('lesson-'):
            continue
        lesson_data = get_lesson_data(lesson)
        cmpl = lesson_data['compliance']
        readme = lesson_data['readme']
        category = lesson_data['category']
        compliance[category].append(dict(name=lesson, converters=cmpl, readme=readme))
    return dict(compliance=compliance)

@app.route('/lesson/<lesson>')
@jinja.template('lesson.html')  # decorator method is staticmethod
async def lesson(request, lesson):
    lesson_dir = os.path.join(LESSON_ROOT, lesson)
    if not os.path.exists(lesson_dir):
        raise NotFound('Lession {} does not exist'.format(lesson))
    return dict(params=get_lesson_data(lesson) )


def get_lesson_data(lesson):

    lesson_dir = os.path.join(LESSON_ROOT, lesson)
    conversion_ini = os.path.join(lesson_dir, 'conversion.ini')
    readme_fn = os.path.join(lesson_dir, 'README.rst')
    readme = None
    if os.path.exists(readme_fn):
        readme = open(readme_fn).read()

    pdfs = list()
    compliance = dict()
    mode = 'html'
    category = 'intro'
    if os.path.exists(conversion_ini):
        CP = ConfigParser()
        CP.read(conversion_ini)
        if CP.has_option('common', 'mode'):
            mode = CP.get('common', 'mode')
        if CP.has_option('common', 'category'):
            category = CP.get('common', 'category')

        for section in CP.sections():
            if section not in ('PDFreactor', 'PrinceXML', 'Vivliostyle', 'Antennahouse'):
                continue

            pdf_file = CP.get(section, 'pdf')
            status = CP.get(section, 'status')
            message = CP.get(section, 'message')

            generated_pdf = os.path.join(lesson_dir, pdf_file)
            if not os.path.exists(generated_pdf):
                print('--> No PDF file {}'.format(generated_pdf))

            image_directory  = os.path.join(lesson_dir, 'images', section.lower())
            images = []
            if os.path.exists(image_directory):
                images = sorted(os.listdir(image_directory))
                if not images:
                    print('--> No images found in {}'.format(image_directory))
                images = [image for image in images if not image.startswith('thumb-')]

            pdfs.append(dict(name=section, pdf_file=pdf_file, status=status, message=message, images=images))
            compliance[section] = dict(name=section, pdf_file=pdf_file, status=status, message=message)

        has_css = os.path.exists(os.path.join(lesson_dir, 'styles.css'))
        css_text = ''
        if has_css:
            with open(os.path.join(lesson_dir, 'styles.css')) as fp:
                css_text = fp.read()

        source = ''
        if os.path.exists(os.path.join(lesson_dir, 'index.html')):
            with open(os.path.join(lesson_dir, 'index.html')) as fp:
                source = fp.read()
        elif os.path.exists(os.path.join(lesson_dir, 'index.xml')):
            with open(os.path.join(lesson_dir, 'index.xml')) as fp:
                source = fp.read()

        params = dict(
            category=category,
            name=lesson,
            pdfs=pdfs,
            has_css=has_css,
            css_text=css_text,
            source=source, 
            readme=readme,
            mode=mode,
            compliance=compliance,
            )
        return params


if __name__ == '__main__':
    app.static('/static', './static')
    app.run(host='0.0.0.0', port=8000, debug=True)
