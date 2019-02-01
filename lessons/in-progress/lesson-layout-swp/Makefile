all: antennahouse 

antennahouse:
	-run.sh -d  index.html -o antennahouse.pdf

images: FORCE
	-rm -fr images
	mkdir -p images/antennahouse 
	echo 1 >images/placeholder
	-convert -density 150 -quality 85 antennahouse.pdf                                   images/antennahouse/antennahouse.png
	-convert -thumbnail 100x100 -background white -alpha remove antennahouse.pdf         images/antennahouse/thumb-antennahouse.png

FORCE:
