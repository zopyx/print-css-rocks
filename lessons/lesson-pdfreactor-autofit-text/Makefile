all: pdfreactor

pdfreactor:
	-pdfreactor.py --verbose --javaScriptMode ENABLED -i index.html -o pdfreactor.pdf

images: FORCE
	-rm -fr images
	mkdir -p images/pdfreactor
	echo 1 >images/placeholder
	-convert -density 150 -quality 85 pdfreactor.pdf                                   images/pdfreactor/pdfreactor.png
	-convert -thumbnail 100x100 -background white -alpha remove pdfreactor.pdf         images/pdfreactor/thumb-pdfreactor.png

FORCE:
