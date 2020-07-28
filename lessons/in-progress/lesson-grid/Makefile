all: pagedjs 

pagedjs:
	-timeout --foreground -s 9 10 pagedjs-cli -i index.html -o pagedjs.pdf

clean:
	find . -name \*.pdf -exec rm {} \;

images: FORCE
	-rm -fr images
	mkdir -p images/pdfreactor images/princexml images/antennahouse  images/weasyprint images/pagedjs
	echo 1 >images/placeholder
	$(eval OPTS :=-density 150 -quality 85)
	$(eval OPTS2 := +profile "icc")
	-convert $(OPTS) pagedjs.pdf            $(OPTS2) images/pagedjs/pagedjs.png
	-convert $(THUMBOPTS)  pagedjs.pdf     	      $(OPTS2) images/pagedjs/thumb-pagedjs.png

FORCE:

push: 
	git push
