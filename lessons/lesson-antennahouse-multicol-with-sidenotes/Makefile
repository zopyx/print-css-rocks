all: antennahouse 

antennahouse:
	-run.sh -d  index.html -o antennahouse.pdf

images: FORCE
	-rm -fr images
	mkdir -p images/antennahouse 
	echo 1 >images/placeholder
	-magick -density 150 -quality 85 antennahouse.pdf                                   images/antennahouse/antennahouse.png
	-magick antennahouse.pdf -thumbnail 100x100 -background white -alpha remove       images/antennahouse/thumb-antennahouse.png

FORCE:
