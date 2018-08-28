all: pdfreactor prince antennahouse 

pdfreactor:
	-pdfreactor.py  --addLinks --addBookmarks --javaScriptMode ENABLED -i index.html -o pdfreactor.pdf

prince: 
	-prince --javascript index.html -o prince.pdf

vivliostyle: 
	-vivliostyle-formatter index.html 

antennahouse:
	-run.sh -d  index.html -o antennahouse.pdf

clean:
	find . -name \*.pdf -exec rm {} \;

check-css:
	csslint --ignore=ids,bulletproof-font-face,import *css

check-html:
	htmllint index.html

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

push: 
	git push


docs: FORCE
	git pull
	python3 -m venv .
	bin/pip install sphinx sphinx-bootstrap-theme ninja sphinxcontrib-googleanalytics lxml
	cd docs; rm -fr build; make html; ../bin/python fix_titles.py
	rm -fr /var/www/print-css-rocks/html
	mkdir /var/www/print-css-rocks/html
	cp -a docs/build/html/* /var/www/print-css-rocks/html

FORCE:

generate-all: FORCE
	./generate.sh
	cd docs;  export PATH=${PWD}/../bin:${PATH} ../bin/python generate_lessons.py; make html
