from pdf2docx import Converter

pdf_file = "0000.pdf"
docx_file = "0000.docx"

cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
