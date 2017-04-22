
import os
import lxml.html

html_dir = 'build/html'

for name in os.listdir(html_dir):
    fname = os.path.join(html_dir, name)
    if not os.path.isfile(fname):
        continue
    with open(fname, 'rb') as fp:
        root = lxml.html.fromstring(fp.read())

    nodes = root.xpath('//title')
    if nodes:
        title = nodes[0].text
        title += u' - CSS Paged Media Tutorial and Showcase - Andreas Jung, ZOPYX'
        nodes[0].text = title
        print 'changed'
        print fname


    nodes = root.xpath('//head')
    if nodes:
        head = nodes[0]
        node = lxml.etree.Element('meta')
        node.attrib['name'] = 'description'
        node.attrib['content'] = 'CSS Paged Media (PDF generation from XML and HTML using CSS stylesheets) tutorial and showcase with lessons, tool descriptions and comparions. PDFreactor Antennahouse PrinceXML'
        head.append(node)

        node = lxml.etree.Element('meta')
        node.attrib['name'] = 'keywords'
        node.attrib['content'] = 'CSS,PDF,HTML,XML, CSS Paged media, Antennahouse, PDFreactor, PrinceXML, Markup' 
        head.append(node)


    html = lxml.html.tostring(root)
    with open(fname, 'wb') as fp:
        fp.write(html.encode('utf8'))
