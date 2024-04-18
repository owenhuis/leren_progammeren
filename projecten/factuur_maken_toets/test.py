from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def create_pdf(file_path, image_path):
    # Creëer een canvas
    c = canvas.Canvas(file_path, pagesize=letter)

    # klant informatie
    c.drawString(10, 750, "Aan: bedrijfsnaam of klanntnaam")
    c.drawString(40, 725, "de heer of vrouw eerste letter. achternaam ")
    c.drawString(40, 700, "straatnaam en huisnummer")
    c.drawString(40, 675, "postcode + VESTIGINGSPLAATS")

    #mijn logo
    c.drawImage(image_path,350,0,200,150)

    #mijn informatie
    c.drawString(400, 735,"codwen")
    c.drawString(400, 715, "roboutslaan 34")
    c.drawString(400, 705, "3312 KP Dordrecht")
    c.drawString(400, 685, "kvk nummer:  0000000")
    c.drawString(400, 675, "btw-id: 0000000")
    c.drawString(400, 655, "bank: ing")
    c.drawString(400, 645, "IBAN: nl 0000001")
    c.drawString(400, 635, "bic: 007")
    c.drawString(400, 615, "telefoon: 06 0000001")
    c.drawString(400, 605, "email: mijn@gmail.com")
    c.drawString(400, 585, "website: http://mijnwebsite.com")
    
    # factuur gegevens
    c.drawString(10, 550, "FACTUUR")
    c.drawString(40, 525, "factuurnummer: xxx")
    c.drawString(40, 510, "factuurdatum: DD-MM-YYYY")
    c.drawString(40, 500, "mijn referentie: xxx")
    c.drawString(40, 485, "vervaldatum: DD-MM-YYYY")
    
    #lijn
    c.line(0, 450,750,450)

    # datum - omschrijving - aantal - prijs per stuk - btw - totaal
    c.drawString(40,435,"datum")
    c.drawString(100,435,"omschrijving")
    c.drawString(200,435,"aantal")
    c.drawString(300,435,"prijs per stuk")
    c.drawString(400,435,"btw")
    c.drawString(500,435,"totaal")

    #lijn
    c.line(0,425,750,425)

    #informatie van tussen de lijnen
    c.drawString(40,400,"dd-mm-yyyy")
    c.drawString(115,400,"xxx")
    c.drawString(200,400,"xxx")
    c.drawString(300,400,"xxx")
    c.drawString(400,400,"xxx")
    c.drawString(500,400,"xxx")

    c.line(0,350,750,350)

    #btw berekening
    c.drawString(40,325,"totaal excl. btw")
    c.drawString(500,325,"xxx")
    c.drawString(200,300,"btw%")
    c.drawString(200,285,"xxx")
    c.drawString(250,300,"overbedrag")
    c.drawString(250,285,"xxx")
    c.drawString(350,300,"totaal incl. btw")
    c.drawString(350,285,"xxx")
    c.drawString(40,250,"totaal btw")
    c.drawString(500,250,"xxx")

    #lijn
    c.line(0,200,750,200)

    #te betalen
    c.drawString(40,175,"te betalen")
    c.drawString(500,175,"xxx")

    #voorwaarden
    c.drawString(40,150,"voorwaarden")
    c.drawString(40,100,"binnen 14 dagen betalen daarna 0.1% rente per dag")

    # Sluit het canvas af
    c.save()

output_folder = "factuur_maken_toets/pdf_files"
image_path = "factuur_maken_toets/logo.png"
file_name = "test.pdf"
output_path = os.path.join(output_folder, file_name)

# Roep de functie aan om het PDF-bestand te maken en geef het volledige pad door
create_pdf(output_path,image_path)