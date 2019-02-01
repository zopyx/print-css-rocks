all: antennahouse pdfreactor prince

antennahouse:
	run.sh -s styles.css -d index.xml -o antennahouse.pdf

pdfreactor:
	pdfreactor -s styles.css  index.xml pdfreactor.pdf

prince:
	prince -s styles.css  index.xml prince.pdf
