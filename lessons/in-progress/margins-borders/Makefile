all:
	run.sh -d index.html >ah.pdf
	weasyprint index.html wp.pdf
	prince index.html -o prince.pdf
	pdfreactor.py -i index.html -o pdfreactor.pdf
	pagedjs-cli index.html -o pagedjs.pdf
	-diff-pdf --output-diff ah-wp.pdf				ah.pdf wp.pdf
	-diff-pdf --output-diff ah-prince.pdf			ah.pdf prince.pdf
	-diff-pdf --output-diff ah-pdfreactor.pdf		ah.pdf pdfreactor.pdf
	-diff-pdf --output-diff prince-pdfreactor.pdf   prince.pdf pdfreactor.pdf
	-diff-pdf --output-diff prince-wp.pdf           prince.pdf wp.pdf
	-diff-pdf --output-diff pdfreactor-wp.pdf       pdfreactor.pdf wp.pdf
	-diff-pdf --output-diff pagedjs-prince.pdf      pagedjs.pdf prince.pdf
	-diff-pdf --output-diff pagedjs-pdfreactor.pdf  pagedjs.pdf pdfreactor.pdf

