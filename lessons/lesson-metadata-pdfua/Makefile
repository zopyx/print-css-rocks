all: prince pdfreactor antennahouse typeset.sh weasyprint pagedjs

prince:
	prince --tagged-pdf --pdf-profile 'PDF/UA-1' index.html --tagged-pdf -o prince.pdf

antennahouse:
	run.sh -d index.html -pdfver PDF1.7/UA-1:2014 >antennahouse.pdf

pdfreactor:
	pdfreactor.py --addTags  --conformance PDFUA1 -i index.html -o pdfreactor.pdf

bfo:
	bfo.sh --env-bfo-pdf-tagged true --output bfo.pdf index.html

weasyprint:
	weasyprint --pdf-variant pdf/ua-1 index.html weasyprint.pdf

pagedjs:
	timeout --foreground -s 9 10 pagedjs-cli index.html -o pagedjs.pdf

typeset.sh:
	typeset.sh.phar render:html --allow-local / -rx index.html typeset.pdf

