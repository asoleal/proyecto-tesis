rm *.aux *.bcf *.bbl *.log *.blg
pdflatex prueba.tex
biber prueba
pdflatex prueba.tex
pdflatex prueba.tex
