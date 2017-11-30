inz.pdf: inz.tex bibliography.bib mgr.cls settings.tex
	pdflatex -synctex=1 -interaction=nonstopmode inz.tex
	bibtex inz
	pdflatex -synctex=1 -interaction=nonstopmode inz.tex
	pdflatex -synctex=1 -interaction=nonstopmode inz.tex


.PHONY: clean

clean:
	@rm -rfv \
		inz.aux \
		inz.lof \
		inz.log \
		inz.lot \
		inz.out \
		inz.toc \
		inz.synctex.gz \
		settings.aux
