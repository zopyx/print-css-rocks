all: prince pdfreactor antennahouse typeset.sh weasyprint pagedjs

prince:
	prince --tagged-pdf index.html --tagged-pdf -o prince.pdf

antennahouse:
	run.sh -d index.html >antennahouse.pdf

pdfreactor:
	pdfreactor.py --addTags -i index.html -o pdfreactor.pdf

weasyprint:
	weasyprint index.html weasyprint.pdf

pagedjs:
	pagedjs-cli index.html -o pagedjs.pdf

typeset.sh:
	typeset.sh.phar render:html -rx index.html typeset.pdf

