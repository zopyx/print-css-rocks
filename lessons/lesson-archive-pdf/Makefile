all: prince pdfreactor antennahouse 

prince:
	prince --tagged-pdf --pdf-profile 'PDF/A-3b' index.html  -o prince.pdf

antennahouse:
	run.sh -d index.html -pdfver PDF1.7/A-3b:2012 -i config.xml >antennahouse.pdf

pdfreactor:
	pdfreactor.py --conformance PDFA3B -i index.html -o pdfreactor.pdf

