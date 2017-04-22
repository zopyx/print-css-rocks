import fpdf
from PyPDF2 import PdfFileWriter, PdfFileReader


overlay_pdf_file_name = 'overlay_PDF.pdf'
pdf_template_file_name = 'base_PDF_template.pdf'
result_pdf_file_name = 'final_PDF.pdf'

# This section creates a PDF containing the information you want to enter in the fields
# on your base PDF.
pdf = fpdf.FPDF(format='letter', unit='pt')
pdf.add_page()
template_page.mergePage(overlay_pdf.getPage(0))
# Write the result to a new PDF file
output_pdf = PdfFileWriter()
output_pdf.addPage(template_page)
