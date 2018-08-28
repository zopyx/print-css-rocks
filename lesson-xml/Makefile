all: pdfreactor prince antennahouse

pdfreactor:
	pdfreactor.py -c styles.css -i index.xml -o pdfreactor.pdf

prince: 
	prince -s styles.css  index.xml -o prince.pdf

vivliostyle: 
	vivliostyle-formatter --style=styles.css index.xml 

antennahouse: 
	run.sh -css styles.css -d index.xml -o antennahouse.pdf

clean:
	find . -name \*.pdf -exec rm {} \;

images: FORCE
	-rm -fr images
	mkdir -p images/pdfreactor images/princexml images/antennahouse images/vivliostyle
	echo 1 >images/placeholder
	$(eval OPTS :=-density 150 -quality 85)
	$(eval OPTS2 := +profile "icc")
	$(eval THUMBOPTS := -thumbnail 100x100 -background white -alpha remove)
	-convert $(OPTS) pdfreactor.pdf         $(OPTS2) images/pdfreactor/pdfreactor.png
	-convert $(OPTS) prince.pdf             $(OPTS2) images/princexml/prince.png
	-convert $(OPTS) antennahouse.pdf       $(OPTS2) images/antennahouse/antennahouse.png
#	-convert $(OPTS) vivliostyle-output.pdf $(OPTS2) images/vivliostyle/vivliostyle.png
	-convert $(THUMBOPTS)  pdfreactor.pdf         $(OPTS2) images/pdfreactor/thumb-pdfreactor.png
	-convert $(THUMBOPTS)  prince.pdf     		  $(OPTS2) images/princexml/thumb-prince.png
	-convert $(THUMBOPTS)  antennahouse.pdf 	  $(OPTS2) images/antennahouse/thumb-antennahouse.png
#	-convert $(THUMBOPTS)  vivliostyle-output.pdf $(OPTS2) images/vivliostyle/thumb-vivliostyle.png

FORCE:
