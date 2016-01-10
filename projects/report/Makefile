MAIN = main

all:
	pdflatex ${MAIN}.tex
	pdflatex ${MAIN}.tex
	bibtex ${MAIN}
	pdflatex ${MAIN}.tex
	pdflatex ${MAIN}.tex

.PHONY:clean_all, clean
cleanall:
	rm -f *aux *log *toc *bbl *blg *pdf *out *bcf *fdb_latexmk *fls *xml
clean:
	rm -f *aux *log *toc *bbl *blg *out *bcf *fdb_latexmk *fls *xml
