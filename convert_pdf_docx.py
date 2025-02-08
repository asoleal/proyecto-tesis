import pdfplumber
from docx import Document

def pdf_a_docx(pdf_path, docx_path):
    # Crear un nuevo documento de Word
    doc = Document()

    # Abrir el archivo PDF
    with pdfplumber.open(pdf_path) as pdf:
        # Iterar sobre cada página del PDF
        for page_num, page in enumerate(pdf.pages, start=1):
            # Extraer el texto de la página
            text = page.extract_text()
            
            if text:
                # Agregar el texto al documento Word
                doc.add_paragraph(text)
            else:
                print(f"No se pudo extraer texto de la página {page_num}")

    # Guardar el documento Word
    doc.save(docx_path)
    print(f"El archivo DOCX ha sido guardado en: {docx_path}")

# Rutas de los archivos
pdf_path = "0000.pdf"  # Cambia esto por la ruta de tu archivo PDF
docx_path = "salida.docx"  # Cambia esto por la ruta donde deseas guardar el archivo DOCX

# Llamar a la función para convertir
pdf_a_docx(pdf_path, docx_path)
