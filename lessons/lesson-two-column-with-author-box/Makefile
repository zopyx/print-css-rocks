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
	mkdir -p images/pdfreactor images/princexml images/antennahouse  images/bfo
	echo 1 >images/placeholder
	-magick -density 150 -quality 85 pdfreactor.pdf         images/pdfreactor/pdfreactor.png
	-magick -density 150 -quality 85 prince.pdf             images/princexml/prince.png
	-magick -density 150 -quality 85 antennahouse.pdf       images/antennahouse/antennahouse.png
	-magick pdfreactor.pdf   -thumbnail 100x100 -background white -alpha remove        images/pdfreactor/thumb-pdfreactor.png
	-magick prince.pdf       -thumbnail 100x100 -background white -alpha remove        images/princexml/thumb-prince.png
	-magick antennahouse.pdf -thumbnail 100x100 -background white -alpha remove        images/antennahouse/thumb-antennahouse.png

FORCE:
