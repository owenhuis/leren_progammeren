from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import json

def create_pdf(file_path, image_path, data):
    # Create a canvas
    c = canvas.Canvas(file_path, pagesize=letter)
    
    eigen_info = {
        'naam': 'codwen',
        'adres': 'romboutslaan 34',
        'postcode': '3312 KP Dordrecht',
        'KVK-nummer': '0000000',
        'btw-id': '0000000',
        'bank': 'ing',
        'IBAN': 'nl 0000001',
        'bic': '007',
        'telefoon': '06 0000001',
        'email':'mijn@gmail.com',
        'website': 'http://mijnwebsite.com',
    }
    # order_info.append(eigen_info)

    order_info = data['order']
    klant_info = order_info['klant']
    producten_info = order_info['producten']
    # mijn_info = order_info['eigen_info']

    # klant informatie
    c.drawString(10, 750, f"Aan: {klant_info['naam']}")
    c.drawString(40, 725, f"de heer of vrouw van {klant_info['naam']}")
    c.drawString(40, 700, f"{klant_info['adres']}")
    c.drawString(40, 675, f"{klant_info['postcode']} {klant_info['stad']}")
    c.drawString(40, 650, f"KVK-nummer {klant_info['KVK-nummer']}")

    # Mijn logo
    c.drawImage(image_path, 350, 0, 200, 150)


    

    # Mijn informatie
    c.drawString(400, 735, f"{eigen_info['naam']}")
    c.drawString(400, 715, f"{eigen_info['adres']}")
    c.drawString(400, 705, f"{eigen_info['postcode']}")
    c.drawString(400, 685, f"kvk-nummer: {eigen_info['KVK-nummer']}")
    c.drawString(400, 675, f"btw-id: {eigen_info['btw-id']}")
    c.drawString(400, 655, f"bank: {eigen_info['bank']}")
    c.drawString(400, 645, f"IBAN: {eigen_info['IBAN']}")
    c.drawString(400, 635, f"bic: {eigen_info['bic']}")
    c.drawString(400, 615, f"telefoon: {eigen_info['telefoon']}")
    c.drawString(400, 605, f"email: {eigen_info['email']}")
    c.drawString(400, 585, f"website: {eigen_info['website']}")
    
    # factuur informatie
    c.drawString(10, 550, f"FACTUUR {order_info['ordernummer']}")
    c.drawString(40, 525, f"factuurdatum: {order_info['orderdatum']}")
    c.drawString(40, 510, f"vervaldatum: {order_info['betaaltermijn']}")

    # Lijn
    c.line(0, 450, 750, 450)

    # beschrijving van tabel
    c.drawString(40, 435, "datum")
    c.drawString(100, 435, "omschrijving")
    c.drawString(250, 435, "aantal")
    c.drawString(300, 435, "prijs per stuk")
    c.drawString(400, 435, "btw")
    c.drawString(500, 435, "totaal")

    # Lijn
    c.line(0, 425, 750, 425)

    y = 400  

    
    for product_info in producten_info:
        # Informatie tussne lijnen
        c.drawString(20, y, f"{order_info['orderdatum']}")
        c.drawString(90, y, f"{product_info['productnaam']}")
        c.drawString(250, y, f"{product_info['aantal']}")
        c.drawString(300, y, f"{product_info['prijs_per_stuk_excl_btw']}")
        c.drawString(400, y, f"{product_info['btw_percentage']}")

        totaal = product_info['aantal'] * product_info['prijs_per_stuk_excl_btw']
        c.drawString(500, y, f"{totaal:.2f}")  

        
        y -= 15
    y -= 2
    c.line(0, y, 750, y)
    y -= 15
    
    # Calculate total bedrag
    totaal_excl_btw = sum(product_info['aantal'] * product_info['prijs_per_stuk_excl_btw'] for product_info in producten_info)
    totaal_btw = sum((product_info['aantal'] * product_info['prijs_per_stuk_excl_btw']) * (product_info['btw_percentage'] / 100) for product_info in producten_info)
    totaal_incl_btw = totaal_excl_btw + totaal_btw

    # Total excluding btw
    c.drawString(40, y, "totaal excl. btw")
    c.drawString(500, y, f"{totaal_excl_btw:.2f}")  # Display total excluding VAT with two decimal places

    #btw percentage
    c.drawString(200, 300, "btw%")
    c.drawString(200, 285, f"{product_info['btw_percentage']}")

    # Overbedrag
    c.drawString(250, 300, "overbedrag")
    c.drawString(250, 285, f"{totaal}")
   
    totaal_met_btw = totaal * (product_info['btw_percentage'] / 100 + 1)   
    totaal_btw =   totaal_met_btw  -  totaal
    
    # Totaal  btw
    c.drawString(350, 300, "bedrag")
    c.drawString(350, 285, f"{totaal_btw:.2f}")

    # Totaal btw
    c.drawString(40, 250, "totaal btw")
    c.drawString(500, 250, f"{totaal_btw:.2f}")  # Display total VAT with two decimal places

    # eind bedrag
    c.drawString(40, 175, "te betalen")
    c.drawString(500, 175, f"{totaal_incl_btw:.2f}")  # Display total amount to be paid with two decimal places

    # Terms and conditions
    c.drawString(40, 150, "voorwaarden")
    c.drawString(40, 100, "binnen 14 dagen betalen daarna 0.1% rente per dag")

    # Close the canvas
    c.save()




def generate_pdf_file(directory):
    for file_name in os.listdir(directory):
        # Controleer of het een JSON-bestand is
        if file_name.endswith('.json'):
            # Volledig pad naar het JSON-bestand
            json_file_path = os.path.join(directory, file_name)
            
            # Laad data uit JSON-bestand
            with open(json_file_path) as f:
                data = json.load(f)
            
            # Verkrijg de naam zonder de extensie
            name = os.path.splitext(file_name)[0]
            
            # PDF-uitvoernaam
            output_folder = "invoices"
            image_path = "logo.png"
            pdf_file_name = f"{name}.pdf"
            output_path = os.path.join(output_folder, pdf_file_name)
            
            # Maak PDF
            create_pdf(output_path, image_path, data)

# Pad naar de map met JSON-bestanden
directory_path = "json_files"

# Verwerk elk bestand in de map
generate_pdf_file(directory_path)