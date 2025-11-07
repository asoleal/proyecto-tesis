#!/bin/bash
set -e  # detiene si hay error
rm -f *.aux *.bbl *.blg *.bcf *.run.xml *.log *.toc

pdflatex 0000.tex
biber 0000
pdflatex 0000.tex
pdflatex 0000.tex
echo "✅ Compilación completa con biber y biblatex"
