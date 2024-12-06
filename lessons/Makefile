all: pdfreactor prince antennahouse  weasyprint pagedjs typeset.sh vivliostyle bfo

pdfreactor: FORCE
	-pdfreactor.py  -i index.html -o pdfreactor.pdf --base-url file://${PWD}/ --log-level DEBUG

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
	$(eval THUMBOPTS := -background white -alpha remove -thumbnail 100x100)
	-magick $(OPTS) pdfreactor.pdf         $(OPTS2) images/pdfreactor/pdfreactor.png
	-magick $(OPTS) prince.pdf             $(OPTS2) images/princexml/prince.png
	-magick $(OPTS) antennahouse.pdf       $(OPTS2) images/antennahouse/antennahouse.png
	-magick $(OPTS) weasyprint.pdf         $(OPTS2) images/weasyprint/weasyprint.png
	-magick $(OPTS) pagedjs.pdf            $(OPTS2) images/pagedjs/pagedjs.png
	-magick $(OPTS) typeset.pdf            $(OPTS2) images/typeset.sh/typeset.png
	-magick $(OPTS) vivliostyle.pdf        $(OPTS2) images/vivliostyle/vivliostyle.png
	-magick $(OPTS) bfo.pdf                $(OPTS2) images/bfo/bfo.png
	-magick  pdfreactor.pdf		 $(THUMBOPTS)         $(OPTS2) images/pdfreactor/thumb-pdfreactor.png
	-magick  prince.pdf			 $(THUMBOPTS)   	  $(OPTS2) images/princexml/thumb-prince.png
	-magick  antennahouse.pdf	 $(THUMBOPTS)  	      $(OPTS2) images/antennahouse/thumb-antennahouse.png
	-magick  weasyprint.pdf		 $(THUMBOPTS)    	  $(OPTS2) images/weasyprint/thumb-weasyprint.png
	-magick  pagedjs.pdf		 $(THUMBOPTS) 	      $(OPTS2) images/pagedjs/thumb-pagedjs.png
	-magick  typeset.pdf		 $(THUMBOPTS) 	      $(OPTS2) images/typeset.sh/thumb-typeset.png
	-magick  vivliostyle.pdf	 $(THUMBOPTS)     	  $(OPTS2) images/vivliostyle/thumb-vivliostyle.png
	-magick  bfo.pdf			 $(THUMBOPTS)         $(OPTS2) images/bfo/thumb-bfo.png

FORCE:

push: 
	git push
