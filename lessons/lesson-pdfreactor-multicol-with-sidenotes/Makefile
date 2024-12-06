all: pdfreactor

pdfreactor:
	-pdfreactor.py --verbose -i index.html -o pdfreactor.pdf --base-url file://$(PWD)/

images: FORCE
	-rm -fr images
	mkdir -p images/pdfreactor
	echo 1 >images/placeholder
	-magick -density 150 -quality 85 pdfreactor.pdf                                   images/pdfreactor/pdfreactor.png
	-magick pdfreactor.pdf -background white -alpha remove -thumbnail 100x100 images/pdfreactor/thumb-pdfreactor.png

FORCE:
