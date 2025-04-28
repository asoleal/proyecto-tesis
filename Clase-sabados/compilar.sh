rm *.aux *.bcf *.bbl *.log *.blg
pdflatex bfs2.tex
biber bfs2
pdflatex bfs2.tex
pdflatex bfs2.tex
