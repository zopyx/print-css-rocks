from PyPDF2 import PdfFileWriter, PdfFileReader


output = PdfFileWriter()

ipdf = PdfFileReader(open('p1.pdf', 'rb'))
wpdf = PdfFileReader(open('p2.pdf', 'rb'))
watermark = wpdf.getPage(0)

for i in xrange(ipdf.getNumPages()):
    page = ipdf.getPage(i)
    for o in page.getContents():
        print o
        import pdb; pdb.set_trace() 
    page.mergePage(watermark)
    output.addPage(page)

with open('newfile.pdf', 'wb') as f:
   output.write(f)

