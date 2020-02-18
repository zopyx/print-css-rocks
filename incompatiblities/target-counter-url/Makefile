all:
	prince index.html -o prince.pdf
	weasyprint index.html wp.pdf
	run.sh -d index.html >ah.pdf
	pdfreactor.py -i index.html -o pdfreactor.pdf