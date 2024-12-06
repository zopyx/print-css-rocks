all: pdfreactor prince antennahouse bfo

pdfreactor:
	pdfreactor.py -c styles.css -i index.xml -o pdfreactor.pdf --base-url file://$(PWD)/

prince: 
	prince -s styles.css  index.xml -o prince.pdf

antennahouse: 
	run.sh -css styles.css -d index.xml -o antennahouse.pdf

bfo: 
	bfo.sh --output bfo.pdf --css styles.css index.xml 

clean:
	find . -name \*.pdf -exec rm {} \;

images: FORCE
	-rm -fr images
	mkdir -p images/pdfreactor images/princexml images/antennahouse  images/bfo
	echo 1 >images/placeholder
	$(eval OPTS :=-density 150 -quality 85)
	$(eval OPTS2 := +profile "icc")
	$(eval THUMBOPTS := -thumbnail 100x100 -background white -alpha remove)
	-magick $(OPTS) pdfreactor.pdf         $(OPTS2) images/pdfreactor/pdfreactor.png
	-magick $(OPTS) prince.pdf             $(OPTS2) images/princexml/prince.png
	-magick $(OPTS) antennahouse.pdf       $(OPTS2) images/antennahouse/antennahouse.png
	-magick $(OPTS) bfo.pdf                $(OPTS2) images/bfo/bfo.png
	-magick  pdfreactor.pdf   $(THUMBOPTS)       $(OPTS2) images/pdfreactor/thumb-pdfreactor.png
	-magick  prince.pdf       $(THUMBOPTS)   	  $(OPTS2) images/princexml/thumb-prince.png
	-magick  antennahouse.pdf $(THUMBOPTS)  	  $(OPTS2) images/antennahouse/thumb-antennahouse.png
	-magick  bfo.pdf          $(THUMBOPTS)       $(OPTS2) images/bfo/thumb-bfo.png

FORCE:
