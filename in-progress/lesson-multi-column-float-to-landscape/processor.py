import os
import sys
import datetime
import tempfile
import lxml.html
import shutil
import pprint
import PyPDF2
import easyprocess
from lxml.cssselect import CSSSelector


outer_tmpl = """
<div class="outer floatable" id="{id}">
    <div class="inner">
        <div class="wrapper">
        id={id}::orientation={orientation}
        </div>
    </div>
</div>
"""


# check external dependencies
for dep in ('run.sh', 'cpdf'):
    if not shutil.which(dep):
        raise RuntimeError('"{}" not found'.format(dep))


# Find and check PDFBox installation
lib_dir = os.path.join(os.path.dirname(__file__), 'lib')
jar_files = [f for f in os.listdir(lib_dir) if f.endswith('.jar')]


try:
    pdfbox_jar = [f for f in jar_files if f.startswith('pdfbox-app')][0]
    pdfbox_jar = os.path.abspath(os.path.join(lib_dir, pdfbox_jar))
except IndexError:
    raise RuntimeError('Could not find suitable pdfbox-app*.jar file')


class Processor(object):

    def __init__(self,
                 input_directory='src',
                 input_filename='index.html',
                 output_directory=None,
                 styles_directory='styles',
                 ah_options='',
                 verbose=True,
                 metadata={}
                 ):

        self.verbose = verbose
        self.metadata = metadata
        self.input_directory = input_directory
        self.input_filename = input_filename
        self.input_filename = os.path.abspath(
            os.path.join(self.input_directory, self.input_filename))
        self.ah_options = ah_options
        self.styles_directory = styles_directory
        if output_directory:
            if os.path.exists(output_directory):
                shutil.rmtree(output_directory)
            os.makedirs(output_directory)
            self.tmpdir = output_directory
        else:
            self.tmpdir = tempfile.mkdtemp()
        self.logfile = os.path.join(self.tmpdir, 'conversion.log')
        self.index_html = os.path.join(self.tmpdir, input_filename)
        self.index2_html = os.path.join(self.tmpdir, 'index2.html')
        self.index2_pdf = os.path.join(self.tmpdir, 'index2.pdf')
        self.index2_areatree = os.path.join(self.tmpdir, 'index2.areatree')
        self.pdf_final = os.path.join(self.tmpdir, 'final.pdf')
        self._copy_src()
        self._copy_resources()
        self._log('copied {} -> {}'.format(self.input_filename, self.index_html))

    def _recursive_copy(self, src, dst):
        """ Perform a recursive copy from <src> to <dst> directory """

        src = os.path.abspath(src)
        dst = os.path.abspath(dst)
        shutil.copytree(src, dst)

    def _copy_src(self):
        """ Copy source directory to working directory """

        self._recursive_copy(self.input_directory, os.path.join(
            self.tmpdir, self.input_directory))

        for name in os.listdir(os.path.join(self.tmpdir, 'src')):
            fn = os.path.join(self.tmpdir, 'src', name)
            shutil.copy(fn, self.tmpdir)

    def _copy_resources(self):
        """ Copy resource directory to working directory """

        self._recursive_copy(self.styles_directory, os.path.join(
            self.tmpdir, self.styles_directory))

    def _log(self, message, level='info'):
        """ A simple file-based logger """

        message = '{} {:5s} {}'.format(
            datetime.datetime.now().strftime('%Y%m%dT%H:%M:%S'),
            level,
            message)
        if self.verbose:
            print(message)

        with open(self.logfile, 'a') as fp:
            print(message, file=fp, sep='\n')

    def _runcmd(self, cmd):
        """ Execute a given external <cmd> and log the results.
            The command must succeed (status=0) in order to count
            execution as an success.
        """

        self._log('*' * 80)
        self._log(cmd)
        proc = easyprocess.EasyProcess(cmd)
        result = proc.call()
        status = result.return_code
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        self._log('Status: {}'.format(status))
        if stdout:
            self._log(stdout)
        if stderr:
            self._log(stderr)
        if status != 0:
            raise RuntimeError('Execution of "{}" failed\n\nOutput:\n{}'.format(cmd, stdout + stderr))

    def get_log(self):
        """ Return the conversion log as string """

        with open(self.logfile, 'r') as fp:
            return fp.read()

    def _pdfbox(self, pdfbox_command, args):
        """ Wrapper around Apache PDFBox.
            <pdfbox_command> = OverlayPDF, PDFMerger etc.
            <args> = list of arguments as strings
        """

        if isinstance(args, str):
            args = [args]
        cmd = 'java -jar "{}" {} {}'.format(pdfbox_jar,
                                            pdfbox_command, ' '.join(args))
        return self._runcmd(cmd)

    def num_pages_should_be(self, pdf_fn, num_pages):
        """ Ensure that a PDF files has exactly <num_pages> pages """

        np = self.num_pages(pdf_fn)
        if np != num_pages:
            raise ValueError('PDF files {} has {} pages instead of {} (expected)'.format(
                pdf_fn, np, num_pages))

    def num_pages(self, pdf_fn):
        """ Return number of pages for a given PDF document """

        with open(pdf_fn, 'rb') as fp_in:
            reader = PyPDF2.PdfFileReader(fp_in)
            return reader.numPages

    def create_template(self):
        """ Take given input file and create a template file with an injected CSS
            file for the flowables and an empty body (with placeholder for inserting
            # the flowable html snippets).
        """

        with open(self.index_html, 'rb') as fp:

            root = lxml.html.fromstring(fp.read())

            # inject flowable.css into the template
            head = root.find('head')
            link = lxml.html.Element('link')
            link.attrib.update(
                dict(rel='stylesheet', type='text/css', href='styles/flowable.css'))
            head.append(link)

            # remove all body childs
            body = root.find('body')
            body.text = u'{body}'
            for child in body.iterchildren():
                body.remove(child)
            body.attrib['class'] = 'page-{page}'

            # save as template.html
            template_fn = os.path.join(self.tmpdir, 'template.html')
            with open(template_fn, 'wb') as fp_out:
                fp_out.write(lxml.html.tostring(root, encoding='utf8'))

            self._log('generated template: {}'.format(template_fn))

    def extract_flowables(self):
        """ Extract flowables into dedicated HTML snippet files and replace 
            them using a custom markup.
        """

        with open(self.index_html, 'rb') as fp:
            root = lxml.html.fromstring(fp.read())

        sel = CSSSelector('.floatable-next-landscape,.floatable-next-portrait')

        for num, node in enumerate(sel(root)):
            float_fn = os.path.join(
                self.tmpdir, 'floatable-{}.html'.format(num + 1))
            base_fn, ext = os.path.splitext(float_fn)
            with open(float_fn, 'w') as fp:
                fp.write(lxml.html.tostring(node, encoding='unicode'))
                self._log('generated flowable: {}'.format(float_fn))

            floatable_id = 'floatable-{}'.format(num + 1)
            orientation = 'landscape' if 'floatable-next-landscape' in node.attrib['class'] else 'portrait'
            outer_html = outer_tmpl.format(id=floatable_id, orientation=orientation)
            new_node = lxml.html.fromstring(outer_html)
            node.getparent().replace(node, new_node)

        with open(self.index2_html, 'wb') as fp:
            fp.write(lxml.html.tostring(root, encoding='utf8'))

        self._log('generated html file: {}'.format(self.index2_html))

    def create_pdf(self, areatree=False):
        """ Generated initial PDF from given HTML file (with placeholders) """

        result = self.run_ah(
            self.index2_html,
            self.index2_pdf,
            areatree=areatree)
        self._log('generated PDF from {} (areatree={})'.format(
            self.index2_html, areatree))
        return result

    def _rotate_pdf(self, pdf_in, pdf_out, angle):
        """ Rotate <pdf_in> by <angle> degrees to <pdf_out> using cpdf"""

        pdf_tmp = tempfile.mktemp(suffix='.pdf')

        cmd = 'cpdf -rotate {} "{}" -o "{}"'.format(angle, pdf_in, pdf_tmp)
        self._runcmd(cmd)

        cmd = 'cpdf -upright {} -o "{}"'.format(pdf_tmp, pdf_out)
        self._runcmd(cmd)
        os.unlink(pdf_tmp)

    def run_ah(self, input_fn, pdf_fn, areatree=False, custom_css=None):
        """ Run Antennahouse on given input file ``index_fn`` generating
            a PDF output file ``pdf_fn``.
        """

        css_cmd = '-s "{}/styles/{}"'.format(self.tmpdir, custom_css) if custom_css else ''

        if areatree:
            cmd = 'run.sh {} -p @AreaTree -d "{}" -o "{}"'.format(
                self.ah_options, input_fn, self.index2_areatree)
        else:
            cmd = 'run.sh {} {} -d "{}" -o "{}"'.format(
                css_cmd, self.ah_options, input_fn, pdf_fn)
        self._runcmd(cmd)

    def process_floatables(self):

        # Read the Antennahouse areatree
        with open(self.index2_areatree, 'rb') as fp:
            root = lxml.etree.fromstring(fp.read())

        # and for all pages with a floatable placeholder text with id=....
        result = dict()
        for node in root.xpath('//*[contains(@text,"id=")]'):
            current = node

            # get hold of the parent page element inside the areatree
            while current.tag != '{http://www.antennahouse.com/names/XSL/AreaTree}PageViewportArea':
                current = current.getparent()

            # text, absolute and internal page number
            text = node.attrib['text']
            page_no = int(current.attrib['page-number'])
            abs_page_no = int(current.attrib['abs-page-number'])

            d = dict(
                text=text,
                page_no=page_no,
                abs_page_no=abs_page_no)
            for item in text.split('::'):
                k, v = item.split('=')
                d[k] = v
            result[abs_page_no] = d

        self._log(pprint.pformat(result))

        # split PDF document with placeholder pages into single PDF document
        # index2-1.pdf, index2-2.pdf etc.
        self._pdfbox('PDFSplit', self.index2_pdf)

        # determine the number of overall pages
        num_pages = self.num_pages(self.index2_pdf)
        self._log('Number of pages to be processed: {}'.format(num_pages))

        for page_no in range(num_pages):
            page_data = result.get(page_no + 1)

            if not page_data:
                continue  # nothing to do

            # current page contains a placeholder?
            # read the floatable snippet and reformat it using template.html
            floatable_id = page_data['id']
            floatable_html_fn = os.path.join(
                self.tmpdir, '{}.html'.format(floatable_id))
            floatable_html_fn2 = os.path.join(
                self.tmpdir, '{}-2.html'.format(floatable_id))

            # wrap floatable HTML snippet into template.html
            with open(os.path.join(self.tmpdir, 'template.html'), 'r', encoding='utf8') as template_in:
                with open(floatable_html_fn, mode='r', encoding='utf8') as floatable_html_in:
                    template_html = template_in.read()
                    template_html = template_html.format(
                        page='left' if page_data[
                            'page_no'] % 2 == 0 else 'right',
                        body=floatable_html_in.read())
                    with open(floatable_html_fn2, 'w', encoding='utf8') as floatable_html_out:
                        floatable_html_out.write(template_html)

            # generate a PDF for the floatable (flowable.css defines this page as
            # landscape mode. So we need to rotate it later before merging)
            if page_data['orientation'] == 'landscape':
                floatable_pdf_fn = os.path.join(
                    self.tmpdir, 'floatable-{}.pdf'.format(page_no + 1))
                floatable_rotated_pdf_fn = os.path.join(
                    self.tmpdir, 'floatable-{}-rotated.pdf'.format(page_no + 1))
                self.run_ah(floatable_html_fn2, floatable_pdf_fn, custom_css='flowable-landscape.css')
                self.num_pages_should_be(floatable_pdf_fn, 1)
                self._rotate_pdf(floatable_pdf_fn,
                                 floatable_rotated_pdf_fn,
                                '90' if page_data['page_no'] % 2 == 0 else '270')
            else:
                floatable_pdf_fn = os.path.join(
                    self.tmpdir, 'floatable-{}.pdf'.format(page_no + 1))
                self.run_ah(floatable_html_fn2, floatable_pdf_fn)
                self.num_pages_should_be(floatable_pdf_fn, 1)
                # just fake the filename for making the further merging code
                # reusable for portrait and landscape
                floatable_rotated_pdf_fn = floatable_pdf_fn 

            # merge it with original PDF page
            pdf_tmp_fn = tempfile.mktemp(suffix='.pdf')
            pdf_out_fn = os.path.join(
                self.tmpdir, 'index2-{}.pdf'.format(page_no + 1))

            self._pdfbox('OverlayPDF',
                         [floatable_rotated_pdf_fn,
                          pdf_out_fn,
                          pdf_tmp_fn])
            shutil.copy(pdf_tmp_fn, pdf_out_fn)
            os.unlink(pdf_tmp_fn)

        # join all files index2-1.pdf, index2-2.pdf ... into final.pdf
        all_pdfs = ['"{}"'.format(os.path.join(self.tmpdir, 'index2-{}.pdf').format(page_no + 1))
                    for page_no in range(num_pages)]
        all_pdfs.append(self.pdf_final)
        self._pdfbox('PDFMerger', all_pdfs)
        self._log('Final PDF: {}'.format(self.pdf_final))

    def __str__(self):
        """ Printable representation of the PDF processor """
        return '{}(logfile={}, workdir={})'.format(self.__class__.__name__, self.logfile, self.tmpdir)

    def document_info(self):
        """ Return PDF internal metadata as dict (title, description...) """

        with open(self.pdf_final, 'rb') as fp_in:
            reader = PyPDF2.PdfFileReader(fp_in)
            return reader.getDocumentInfo()

    def __call__(self):
        ts = datetime.datetime.now()
        self.create_template()
        self.extract_flowables()
        self.create_pdf()
        self.create_pdf(areatree=True)
        self.process_floatables()
        duration = datetime.datetime.now() - ts
        self._log('PDF pages: {}'.format(self.num_pages(self.pdf_final)))
        self._log('Duration: {}'.format(duration))


if __name__ == '__main__':
    import sys

    src = sys.argv[-1]

    proc = Processor(
        input_directory='src',
        input_filename=src,
        styles_directory='styles',
        output_directory='/tmp/out',
        ah_options='-tpdf -pdfver PDF1.7',
    )
    proc()
    print(proc.get_log())
