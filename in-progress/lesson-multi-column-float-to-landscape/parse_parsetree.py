import os
import pprint
import sys
import lxml.etree
import ah
import PyPDF2


in_fn = sys.argv[-1]

def process_floatables(parsetree_fn, pdf_in_fn='index-out.pdf', pdf_out_fn='index-out2.pdf', template_fn='template.html'):


    print 'Processing AH parsetree: {}'.format(parsetree_fn)
    dirname = os.path.dirname(parsetree_fn)
    with open(parsetree_fn, 'rb') as fp:
        root = lxml.etree.fromstring(fp.read())

    result = dict()
    for node in root.xpath('//*[contains(@text,"id=")]'):
        current = node
        while current.tag != '{http://www.antennahouse.com/names/XSL/AreaTree}PageViewportArea':
            current = current.getparent()

        page_no = int(current.attrib['page-number'])
        abs_page_no = int(current.attrib['abs-page-number'])
        text = node.attrib['text']
        
        d = dict(
                text=text,
                page_no=page_no,
                abs_page_no=abs_page_no)
        for item in text.split('::'):
            k, v = item.split('=')
            d[k] = v
        result[abs_page_no] = d

    pprint.pprint(result)

    with open(pdf_in_fn, 'rb') as fp_in:
        reader = PyPDF2.PdfFileReader(fp_in)
        writer = PyPDF2.PdfFileWriter()

        for page_no in range(reader.numPages):
            page_data = result.get(page_no + 1)
            page = reader.getPage(page_no)
            if page_data:
                floatable_id = page_data['id']
                floatable_html_fn = os.path.join(dirname, '{}.html'.format(floatable_id))
                floatable_html_fn2 = os.path.join(dirname, '{}-2.html'.format(floatable_id))
                # wrap floatable HTML snippet with template.html
                template_fn = os.path.join(dirname, template_fn)
                with open(os.path.join(dirname, template_fn), 'rb') as template_in:
                    with open(floatable_html_fn, 'rb') as floatable_html_in:
                        template_html = template_in.read()
                        template_html = template_html.format(body=floatable_html_in.read())
                        with open(floatable_html_fn2, 'wb') as floatable_html_out:
                            floatable_html_out.write(template_html)

                floatable_pdf_fn = os.path.join(dirname, '{}.pdf'.format(floatable_id))
                ah.run_ah(floatable_html_fn, floatable_pdf_fn)
                with open(floatable_pdf_fn, 'rb') as floatable_in:
                    print '*'*80
                    print 'merging', floatable_pdf_fn
                    floatable_reader = PyPDF2.PdfFileReader(floatable_in)
                    page.mergePage(floatable_reader.getPage(0))

            writer.addPage(page)

        pdf_out_fn = os.path.join(dirname, pdf_out_fn)
        with open(pdf_out_fn, 'wb') as fp_out:
            writer.write(fp_out)
            print 'resulting PDF: {}'.format(pdf_out_fn)

if __name__ == '__main__':
    fn = os.path.abspath(sys.argv[-1])
    process_floatables(fn)
