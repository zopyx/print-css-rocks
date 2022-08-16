all: prince pdfreactor antennahouse 

prince:
	prince --tagged-pdf --pdf-profile 'PDF/A-3b' index.html  -o prince.pdf

antennahouse:
	run.sh -d index.html -pdfver PDF1.7/A-3b:2012 -i config.xml >antennahouse.pdf

pdfreactor:
	pdfreactor.py --conformance PDFA3B -i index.html -o pdfreactor.pdf

weasyprint:
	weasyprint --pdf-variant pdf/a-3b index.html weasyprint.pdf

bfo:
	bfo.sh --output bfo.pdf --env-bfo-pdf-profile 'pdf/a-3a' index.html
