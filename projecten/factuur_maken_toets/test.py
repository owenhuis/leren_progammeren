from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_pdf(file_path):
    # Creëer een canvas
    c = canvas.Canvas(file_path, pagesize=letter)

    # Voeg tekst toe aan het canvas
    c.drawString(100, 750, "Hallo, world!!")

    # Sluit het canvas af
    c.save()

output_folder = "factuur_maken_toets/pdf_files"
file_name = "test.pdf"
output_path = os.path.join(output_folder, file_name)

# Roep de functie aan om het PDF-bestand te maken en geef het volledige pad door
create_pdf(output_path)