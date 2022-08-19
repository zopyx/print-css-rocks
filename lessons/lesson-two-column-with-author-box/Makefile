all: pdfreactor prince antennahouse

pdfreactor:
	pdfreactor.py -c styles.css -i index.xml -o pdfreactor.pdf

prince: 
	prince -s styles.css  index.xml -o prince.pdf

antennahouse: 
	run.sh -css styles.css -d index.xml -o antennahouse.pdf

bfo: 
	run.sh --output bfo.pdf --css styles.css index.xml

clean:
	find . -name \*.pdf -exec rm {} \;

images: FORCE
	mkdir -p images/pdfreactor images/princexml images/antennahouse 
	echo 1 >images/placeholder
	-convert -density 150 -quality 85 pdfreactor.pdf         images/pdfreactor/pdfreactor.png
	-convert -density 150 -quality 85 prince.pdf             images/princexml/prince.png
	-convert -density 150 -quality 85 antennahouse.pdf       images/antennahouse/antennahouse.png
	-convert -thumbnail 100x100 -background white -alpha remove pdfreactor.pdf          images/pdfreactor/thumb-pdfreactor.png
	-convert -thumbnail 100x100 -background white -alpha remove prince.pdf              images/princexml/thumb-prince.png
	-convert -thumbnail 100x100 -background white -alpha remove antennahouse.pdf        images/antennahouse/thumb-antennahouse.png

FORCE:
