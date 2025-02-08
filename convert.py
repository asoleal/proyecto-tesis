import pymuport
from pywordmark import Wordmark

# Cargue el documento PDF
doc = pymuport.PdfFile("path_to_your_document.pdf")

# Obtén un objeto de Documento que se puede modified directamente
doc_obj = doc.load()

# Modifica algo en el documento (por ejemplo, agrega texto)
wordmark = Wordmark(doc_obj)
texto = "Muy bien, hemos logrado una mejora destacable en nuestro proyecto!"

doc_obj.replace(texto, "Muy bien, hemos logrado una mejora destacable en nuestro proyecto!")

# Cargue el documento DOCX con la modifyación
with open("path_to_your_docx.docx", "w") as f:
    f.write(doc_obj.load())

print("El documento PDF se ha convertido en DOCX exitosamente!")
