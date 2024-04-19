from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import json

def create_pdf(file_path, image_path, data):
    # Create a canvas
    c = canvas.Canvas(file_path, pagesize=letter)
    
    order_info = data['order']
    klant_info = order_info['klant']
    product_info = order_info['producten'][0]  # Assuming only one product for simplicity

    # Customer information
    c.drawString(10, 750, f"Aan: {klant_info['naam']}")
    c.drawString(40, 725, f"de heer of vrouw van {klant_info['naam']}")
    c.drawString(40, 700, f"{klant_info['adres']}")
    c.drawString(40, 675, f"{klant_info['postcode']} {klant_info['stad']}")
    c.drawString(40, 650, f"KVK-nummer {klant_info['KVK-nummer']}")

    # My logo
    c.drawImage(image_path, 350, 0, 200, 150)

    # My information
    c.drawString(400, 735, "codwen")
    c.drawString(400, 715, "roboutslaan 34")
    c.drawString(400, 705, "3312 KP Dordrecht")
    c.drawString(400, 685, "kvk-nummer:  0000000")
    c.drawString(400, 675, "btw-id: 0000000")
    c.drawString(400, 655, "bank: ing")
    c.drawString(400, 645, "IBAN: nl 0000001")
    c.drawString(400, 635, "bic: 007")
    c.drawString(400, 615, "telefoon: 06 0000001")
    c.drawString(400, 605, "email: mijn@gmail.com")
    c.drawString(400, 585, "website: http://mijnwebsite.com")
    
    # Invoice information
    c.drawString(10, 550, f"FACTUUR {order_info['ordernummer']}")
    c.drawString(40, 525, f"factuurdatum: {order_info['orderdatum']}")
    c.drawString(40, 510, f"vervaldatum: {order_info['betaaltermijn']}")

    # Line
    c.line(0, 450, 750, 450)

    # Table headers
    c.drawString(40, 435, "datum")
    c.drawString(100, 435, "omschrijving")
    c.drawString(250, 435, "aantal")
    c.drawString(300, 435, "prijs per stuk")
    c.drawString(400, 435, "btw")
    c.drawString(500, 435, "totaal")

    # Line
    c.line(0, 425, 750, 425)

    # Information between the lines
    c.drawString(20, 400, f"{order_info['orderdatum']}")
    c.drawString(90, 400, f"{product_info['productnaam']}")
    c.drawString(250, 400, f"{product_info['aantal']}")
    c.drawString(300, 400, f"{product_info['prijs_per_stuk_excl_btw']}")
    c.drawString(400, 400, f"{product_info['btw_percentage']}")
    totaal = product_info['aantal'] * product_info['prijs_per_stuk_excl_btw']
    c.drawString(500, 400, f"{totaal:.2f}")

    c.line(0, 350, 750, 350)

    # Total excluding VAT
    c.drawString(40, 325, "totaal excl. btw")
    c.drawString(500, 325, f"{totaal:.2f}")
    
    # VAT percentage
    c.drawString(200, 300, "btw%")
    c.drawString(200, 285, f"{product_info['btw_percentage']}")
    
    # Overbedrag (not sure what this means)
    c.drawString(250, 300, "overbedrag")
    c.drawString(250, 285, f"{totaal}")
   
    totaal_met_btw = totaal * (product_info['btw_percentage'] / 100 + 1)   
    totaal_btw =   totaal_met_btw  -  totaal
    # Total including VAT
    c.drawString(350, 300, "bedrag")
    c.drawString(350, 285, f"{totaal_btw:.2f}")

    # Total VAT
    c.drawString(40, 250, "totaal btw")
    c.drawString(500, 250, f"{totaal_btw:.2f}")

    # Line
    c.line(0, 200, 750, 200)

    # Amount to be paid
    c.drawString(40, 175, "te betalen")
    c.drawString(500, 175, f"{totaal_met_btw:.2f}")

    # Terms and conditions
    c.drawString(40, 150, "voorwaarden")
    c.drawString(40, 100, "binnen 14 dagen betalen daarna 0.1% rente per dag")

    # Close the canvas
    c.save()

# Path to the JSON file
json_file_path = 'json_files/2000-018.json'

# Load data from JSON file
with open(json_file_path) as f:
    data = json.load(f)

# Output folder and image path
output_folder = "pdf_files"
image_path = "logo.png"
file_name = "test.pdf"
output_path = os.path.join(output_folder, file_name)

# Call the function to create the PDF
create_pdf(output_path, image_path, data)
