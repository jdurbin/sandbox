#!/usr/bin/env python 

import os
from tempfile import NamedTemporaryFile
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
from InvoiceGenerator.pdf import ProformaInvoice

# choose english as language
os.environ["INVOICE_LANG"] = "en"

provider = Provider('CMEA Bay Section') 
provider.address = 'P.O. Box 4344'
provider.city = 'Modesto'
provider.state = 'CA'
provider.zip_code = '93532'

client = Client('Boitz, Michael')


creator = Creator('')

invoice = Invoice(client, provider, creator)
invoice.currency_locale = 'en_US.UTF-8'
invoice.currency = 'USD'
invoice.add_item(Item(1, 350, description="SHS Symphonic Wind Ensemble"))
invoice.add_item(Item(1, 350, description="SHS Combined Wind Ensemble"))




pdf = SimpleInvoice(invoice)
pdf.gen("cmea_invoice.pdf", generate_qr_code=False)