rm *.aux *.bcf *.bbl *.log *.blg
pdflatex 0000.tex
biber 0000
pdflatex 0000.tex
pdflatex 0000.tex
