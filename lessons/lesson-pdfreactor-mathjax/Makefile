all: pdfreactor


pdfreactor:
	pdfreactor.py -i index.html -o pdfreactor.pdf --base-url file://$(PWD)/

images: FORCE
	-rm -fr images
	mkdir -p images/pdfreactor 
	echo 1 >images/placeholder
	$(eval OPTS :=-density 150 -quality 85)
	$(eval OPTS2 := +profile "icc")
	$(eval THUMBOPTS := -thumbnail 100x100 -background white -alpha remove)
	-magick $(OPTS) pdfreactor.pdf         $(OPTS2) images/pdfreactor/pdfreactor.png
	-magick pdfreactor.pdf $(THUMBOPTS)  $(OPTS2) images/pdfreactor/thumb-pdfreactor.png

FORCE:
