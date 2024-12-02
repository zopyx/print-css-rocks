all: pdfreactor


pdfreactor:
	pdfreactor.py -i index.html --javaScriptMode ENABLED -o pdfreactor.pdf --base-url file://$(PWD)/

images: FORCE
	-rm -fr images
	mkdir -p images/pdfreactor 
	echo 1 >images/placeholder
	$(eval OPTS :=-density 150 -quality 85)
	$(eval OPTS2 := +profile "icc")
	$(eval THUMBOPTS := -thumbnail 100x100 -background white -alpha remove)
	-convert $(OPTS) pdfreactor.pdf         $(OPTS2) images/pdfreactor/pdfreactor.png
	-convert $(THUMBOPTS)  pdfreactor.pdf         $(OPTS2) images/pdfreactor/thumb-pdfreactor.png

FORCE:
