all: pdfreactor prince antennahouse  weasyprint pagedjs typeset.sh vivliostyle bfo

pdfreactor: FORCE
	-pdfreactor.py  --addLinks --addBookmarks --javaScriptMode ENABLED -i index.html -o pdfreactor.pdf

prince: FORCE
	-prince --javascript index.html -o prince.pdf

antennahouse: FORCE
	-run.sh -d  index.html -o antennahouse.pdf

weasyprint: FORCE
	-weasyprint  -e utf-8 index.html weasyprint.pdf

pagedjs: FORCE
	-timeout --foreground -s 9 10 pagedjs-cli -i index.html -o pagedjs.pdf

typeset.sh: FORCE
	-typesetsh.phar render:html --allow-local /home -rx index.html typeset.pdf

vivliostyle:FORCE
	-vivliostyle build --output vivliostyle.pdf index.html

bfo: FORCE
	-bfo.sh  --output bfo.pdf index.html 


clean:
	find . -name \*.pdf -exec rm {} \;

images: FORCE
	-rm -fr images
	mkdir -p images/pdfreactor images/princexml images/antennahouse  images/weasyprint images/pagedjs images/typeset.sh images/vivliostyle images/bfo
	echo 1 >images/placeholder
	$(eval OPTS :=-density 150 -quality 85)
	$(eval OPTS2 := +profile "icc")
	$(eval THUMBOPTS := -thumbnail 100x100 -background white -alpha remove)
	-convert $(OPTS) pdfreactor.pdf         $(OPTS2) images/pdfreactor/pdfreactor.png
	-convert $(OPTS) prince.pdf             $(OPTS2) images/princexml/prince.png
	-convert $(OPTS) antennahouse.pdf       $(OPTS2) images/antennahouse/antennahouse.png
	-convert $(OPTS) weasyprint.pdf         $(OPTS2) images/weasyprint/weasyprint.png
	-convert $(OPTS) pagedjs.pdf            $(OPTS2) images/pagedjs/pagedjs.png
	-convert $(OPTS) typeset.pdf            $(OPTS2) images/typeset.sh/typeset.png
	-convert $(OPTS) vivliostyle.pdf            $(OPTS2) images/vivliostyle/vivliostyle.png
	-convert $(OPTS) bfo.pdf            $(OPTS2) images/bfo/bfo.png
	-convert $(THUMBOPTS)  pdfreactor.pdf         $(OPTS2) images/pdfreactor/thumb-pdfreactor.png
	-convert $(THUMBOPTS)  prince.pdf     		  $(OPTS2) images/princexml/thumb-prince.png
	-convert $(THUMBOPTS)  antennahouse.pdf 	  $(OPTS2) images/antennahouse/thumb-antennahouse.png
	-convert $(THUMBOPTS)  weasyprint.pdf     	  $(OPTS2) images/weasyprint/thumb-weasyprint.png
	-convert $(THUMBOPTS)  pagedjs.pdf     	      $(OPTS2) images/pagedjs/thumb-pagedjs.png
	-convert $(THUMBOPTS)  typeset.pdf     	      $(OPTS2) images/typeset.sh/thumb-typeset.png
	-convert $(THUMBOPTS)  vivliostyle.pdf     	  $(OPTS2) images/vivliostyle/thumb-vivliostyle.png
	-convert $(THUMBOPTS)  bfo.pdf     	          $(OPTS2) images/bfo/thumb-bfo.png

FORCE:

push: 
	git push
