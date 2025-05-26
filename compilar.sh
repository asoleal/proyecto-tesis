rm *.aux *.bbl *.blg *.bcf *.run.xml *.log *.toc
pdflatex 0000.tex
biber 0000
pdflatex 0000.tex
pdflatex 0000.tex
