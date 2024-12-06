
all: prince images

prince: 
	-prince --javascript index.html -o prince.pdf


images: FORCE
	-rm -fr images
	mkdir -p images/princexml 
	echo 1 >images/placeholder
	$(eval OPTS :=-density 150 -quality 85)
	$(eval OPTS2 := +profile "icc")
	$(eval THUMBOPTS := -thumbnail 100x100 -background white -alpha remove)
	-magick $(OPTS) prince.pdf             $(OPTS2) images/princexml/prince.png
	-magick prince.pdf $(THUMBOPTS)  $(OPTS2) images/princexml/thumb-prince.png

FORCE:

push: 
	git push
