import os
import furl
import inspect
import lxml.html
import collections
import configparser
from configparser import ConfigParser
from docutils import core
from docutils.writers.html4css1 import Writer, HTMLTranslator

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

LESSON_ROOT = os.path.abspath(LESSON_ROOT)
GENERATED_ROOT = os.path.abspath(os.path.join(LESSON_ROOT, 'generated'))

print('LESSON_ROOT=', LESSON_ROOT)
print('GENERATED_ROOT=', GENERATED_ROOT)

app = Sanic()
app.static('/static', './static')
Session(app)
jinja = SanicJinja2(app)

lessons_ini = os.path.join(LESSON_ROOT, 'lessons.ini')
with open(lessons_ini) as fp:
    lines = fp.read().split('\n')
lines = [line.strip() for line in lines if line.strip()]
lessons_ordered = dict([(line, i) for i, line in enumerate(lines)])


def render_rst(rst_filename):

    class HTMLFragmentTranslator(HTMLTranslator):
        def __init__(self, document):
            HTMLTranslator.__init__(self, document)
            self.head_prefix = ['', '', '', '', '']
            self.body_prefix = []
            self.body_suffix = []
            self.stylesheet = []

        def astext(self):
            return ''.join(self.body)

    html_fragment_writer = Writer()
    html_fragment_writer.translator_class = HTMLFragmentTranslator

    def rest_to_html(s):
        result = core.publish_string(s, writer=html_fragment_writer)
        result = result.decode('utf8')

        root = lxml.html.fromstring(result)
        nodes = root.xpath('//div[@class="document"]')
        assert len(nodes) == 1
        return lxml.html.tostring(nodes[0], encoding=str)


    if not rst_filename:
        return u''
    elif rst_filename.endswith('.rst'):
        fn = os.path.join(os.path.dirname(__file__), 'content', rst_filename)
        if not os.path.exists(fn):
            raise IOError('RST file {} not found'.format(fn))
        with open(fn) as fp:
            rst_data = fp.read()
        return rest_to_html(rst_data)
    else:
        return rest_to_html(rst_filename)
        


@app.route('/')
@jinja.template('content.html')
async def introduction(request):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst('intro.rst'), 'navigation': inside}


@app.route('/tools')
@jinja.template('content.html')
async def tools(request):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst('tools.rst'), 'navigation': inside}


@app.route('/references')
@jinja.template('content.html')
async def references(request):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst('references.rst'), 'navigation': inside}


@app.route('/related')
@jinja.template('content.html')
async def related(request):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst('related.rst'), 'navigation': inside}


@app.route('/discussion')
@jinja.template('content.html')
async def discussion(request):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst('discussion.rst'), 'navigation': inside}


@app.route('/blog')
@jinja.template('content.html')
async def blog(request):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst('blog.rst'), 'navigation': inside}


@app.route('/about')
@jinja.template('content.html')
async def about(request):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst('about.rst'), 'navigation': inside}


@app.route('/contributing')
@jinja.template('content.html')
async def contributing(request):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst('contributing.rst'), 'navigation': inside}

@app.route('/support')
@jinja.template('content.html')
async def support(request):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst('support.rst'), 'navigation': inside}


@app.route('/blog/<blog>')
@jinja.template('content.html')
async def blog_content(request, blog):
    inside = inspect.stack()[0][0].f_code.co_name
    return {'body': render_rst(blog), 'navigation': inside}


@app.route('/lesson/<lesson>/download/images/<vendor>/<filename>')
async def download_image(request, lesson, vendor, filename):

    lesson_dir = os.path.join(GENERATED_ROOT, lesson)
    if not os.path.exists(lesson_dir):
        raise NotFound('Lession {} does not exist'.format(lesson))

    download_fn = os.path.join(lesson_dir, 'images', vendor, filename)
    if not os.path.exists(download_fn):
        raise NotFound(
            'Download filename {} does not exist'.format(download_fn))
    return await response.file(download_fn)


@app.route('/lesson/<lesson>/download/<filename>')
async def download_pdf(request, lesson, filename):

    lesson_dir = os.path.join(GENERATED_ROOT, lesson)
    if not os.path.exists(lesson_dir):
        raise NotFound('Lession {} does not exist'.format(lesson))

    download_fn = os.path.join(lesson_dir, filename)
    if not os.path.exists(download_fn):
        raise NotFound(
            'Download filename {} does not exist'.format(download_fn))
    return await response.file(download_fn)


@app.route('/lessons')
@jinja.template('lessons.html')
async def lessons(request):
    inside = inspect.stack()[0][0].f_code.co_name

    compliance = collections.OrderedDict()
    compliance['intro'] = []
    compliance['advanced'] = []
    compliance['special'] = []

    for lesson in os.listdir(LESSON_ROOT):
        if not lesson.startswith('lesson-'):
            continue
        lesson_data = get_lesson_data(lesson)
        cmpl = lesson_data['compliance']
        readme_raw = lesson_data['readme']
        readme = render_rst(lesson_data['readme'])
        category = lesson_data['category']
        compliance[category].append(
            dict(name=lesson, converters=cmpl, readme=readme, readme_raw=readme_raw))
    
    compliance['intro'] = sorted(compliance['intro'], key=lambda item: lessons_ordered.get(item['name'], 999))
    compliance['advanced'] = sorted(compliance['advanced'], key=lambda item: lessons_ordered.get(item['name'], 999))
    compliance['special'] = sorted(compliance['special'], key=lambda item: lessons_ordered.get(item['name'], 999))
    return dict(compliance=compliance, navigation=inside)


@app.route('/lesson/<lesson>')
@jinja.template('lesson.html')
async def lesson(request, lesson):
    inside = inspect.stack()[0][0].f_code.co_name
    lesson_dir = os.path.join(LESSON_ROOT, lesson)
    if not os.path.exists(lesson_dir):
        raise NotFound('Lession {} does not exist'.format(lesson))
    request_url = get_request_url(request)
    return dict(lesson=get_lesson_data(lesson), request_url=request_url, navigation='lessons')


def get_request_url(request):
    """ Deal with virtual hosting """
    forwarded_host = request.headers.get('x-forwarded-host')
    if not forwarded_host:
        return request.url
    f = furl.furl(request.url)
    f.scheme = 'https'  # we assume public SSL/TLS
    f.host = forwarded_host
    f.port = None  # SSL
    return f.tostr()


def get_lesson_data(lesson):

    lesson_dir = os.path.join(LESSON_ROOT, lesson)
    generated_dir = os.path.join(GENERATED_ROOT, lesson)

    conversion_ini = os.path.join(lesson_dir, 'conversion.ini')
    readme_fn = os.path.join(lesson_dir, 'README.rst')
    readme = None
    readme_raw = None
    if os.path.exists(readme_fn):
        readme = open(readme_fn).read()
        readme_raw = render_rst(readme)
    
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
            if section not in ('PDFreactor', 'PrinceXML', 'Antennahouse'):
                continue

            try:
                pdf_file = CP.get(section, 'pdf')
                status = CP.get(section, 'status')
                message = CP.get(section, 'message')
            except configparser.NoOptionError as e:
                raise ValueError('{}: {}'.format(e, lesson))

            generated_pdf = os.path.join(generated_dir, pdf_file)
            if not os.path.exists(generated_pdf):
                print('--> No PDF file {}'.format(generated_pdf))

            image_directory = os.path.join(
                generated_dir, 'images', section.lower())
            images = []
            if os.path.exists(image_directory):
                images = sorted(os.listdir(image_directory))
                if not images:
                    print('--> No images found in {}'.format(image_directory))
                images = [
                    image for image in images if not image.startswith('thumb-')]

            pdfs.append(dict(name=section, pdf_file=pdf_file,
                             status=status, message=message, images=images))
            compliance[section] = dict(
                name=section, pdf_file=pdf_file, status=status, message=message)

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
            readme_raw=readme_raw,
            mode=mode,
            compliance=compliance,
        )
        return params


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
