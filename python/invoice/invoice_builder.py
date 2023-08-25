#!/usr/bin/env python3
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import PageLayout
from decimal import Decimal
from borb.pdf import Image
from borb.pdf import FixedColumnWidthTable
from borb.pdf import FlexibleColumnWidthTable
from borb.pdf import Paragraph
from borb.pdf import Alignment
from borb.pdf import HexColor, X11Color
from borb.pdf import TableCell
from datetime import datetime
import random
import typing
from pathlib import Path
from borb.pdf import PDF

class Product:
    """
    This class represents a purchased product
    """

    def __init__(self, name: str, quantity: int, price_per_sku: float):
        self.name: str = name
        assert quantity >= 0
        self.quantity: int = quantity
        assert price_per_sku >= 0
        self.price_per_sku: float = price_per_sku

def _build_invoice_information():
    table_001 = FixedColumnWidthTable(number_of_rows=5, number_of_columns=1)
    table_001.add(Paragraph("Make payment to:",font="Helvetica-Bold"))
    table_001.add(Paragraph("CMEA Bay Section"))
    table_001.add(Paragraph("Executive Treasurer"))
    table_001.add(Paragraph("P.O. Box 4344"))
    table_001.add(Paragraph("Modesto, CA 95353"))

    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    table_001.no_borders()
    return table_001


def _build_billing_and_shipping_information():
    table_001 = FixedColumnWidthTable(number_of_rows=5, number_of_columns=2)
    table_001.add(Paragraph("Festival Details",font="Helvetica-Bold"))
    table_001.add(Paragraph("From:",font="Helvetica-Bold"))
    table_001.add(Paragraph("B/O Festival C"))  # BILLING
    table_001.add(Paragraph("Boitz,Michael"))  # SHIPPING
    table_001.add(Paragraph("Friday, March 25, 2022"))  # BILLING
    table_001.add(Paragraph("Saratoga High School"))  # SHIPPING
    table_001.add(Paragraph("1:10 PM-8:45 PM"))  # BILLING
    table_001.add(Paragraph("mboitz@lgsuhsd.org"))  # SHIPPING
    table_001.add(Paragraph("Saratoga High School"))  # BILLING
    table_001.add(Paragraph("(408) 867-3411"))  # SHIPPING
    #table_001.add(Paragraph("[Phone]"))  # BILLING
    #table_001.add(Paragraph("[Phone]"))  # SHIPPING
    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    table_001.no_borders()
    return table_001


def _build_itemized_description_table(products: typing.List[Product] = []):
    """
    This function builds a Table containing itemized billing information
    :param:     products
    :return:    a Table containing itemized billing information
    """
    numrows = len(products)
    table_001 = FlexibleColumnWidthTable(number_of_rows=numrows, number_of_columns=3)        
    table_001.add(
        TableCell(
            Paragraph("Ensemble Name", font_color=X11Color("White")),
            background_color=HexColor("0b3954"),
            preferred_width=Decimal(256),
        )
    )
    table_001.add(
        TableCell(
            Paragraph("Classification", font_color=X11Color("White")),
            background_color=HexColor("0b3954"),
            preferred_width=Decimal(128),
        )
    )
    table_001.add(
        TableCell(
            Paragraph("Fee", font_color=X11Color("White")),
            background_color=HexColor("0b3954"),
            preferred_width=Decimal(64),
        )
    )
        
    return table_001



def _build_itemized_description_table0(products: typing.List[Product] = []):
    """
    This function builds a Table containing itemized billing information
    :param:     products
    :return:    a Table containing itemized billing information
    """
    table_001 = FixedColumnWidthTable(number_of_rows=15, number_of_columns=4)
    for h in ["Ensemble Name", "Classification", "Info", "Fee"]:
        table_001.add(
            TableCell(
                Paragraph(h, font_color=X11Color("White")),
                background_color=HexColor("0b3954"),
            )
        )

    odd_color = HexColor("f4f3f3")
    even_color = HexColor("FFFFFF")
    
    for row_number, item in enumerate(products):
        c = even_color if row_number % 2 == 0 else odd_color
        table_001.add(TableCell(Paragraph(item.name), background_color=c))
        table_001.add(TableCell(Paragraph(str(item.quantity)), background_color=c))
        table_001.add(
            TableCell(Paragraph("$ " + str(item.price_per_sku)), background_color=c)
        )
        table_001.add(
            TableCell(
                Paragraph("$ " + str(item.quantity * item.price_per_sku)),
                background_color=c,
            )
        )

    # Optionally add some empty rows to have a fixed number of rows for styling purposes
    for row_number in range(len(products), 10):
        c = even_color if row_number % 2 == 0 else odd_color
        for _ in range(0, 4):
            table_001.add(TableCell(Paragraph(" "), background_color=c))

    # subtotal
    subtotal: float = sum([x.price_per_sku * x.quantity for x in products])
    table_001.add(
        TableCell(
            Paragraph(
                "Subtotal",
                font="Helvetica-Bold",
                horizontal_alignment=Alignment.RIGHT,
            ),
            col_span=3,
        )
    )
    table_001.add(
        TableCell(Paragraph("$ 1,180.00", horizontal_alignment=Alignment.RIGHT))
    )

    # discounts
    table_001.add(
        TableCell(
            Paragraph(
                "Discounts",
                font="Helvetica-Bold",
                horizontal_alignment=Alignment.RIGHT,
            ),
            col_span=3,
        )
    )
    table_001.add(TableCell(Paragraph("$ 0.00", horizontal_alignment=Alignment.RIGHT)))

    # taxes
    taxes: float = subtotal * 0.06
    table_001.add(
        TableCell(
            Paragraph(
                "Taxes", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT
            ),
            col_span=3,
        )
    )
    table_001.add(
        TableCell(Paragraph("$ " + str(taxes), horizontal_alignment=Alignment.RIGHT))
    )

    # total
    total: float = subtotal + taxes
    table_001.add(
        TableCell(
            Paragraph(
                "Total", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT
            ),
            col_span=3,
        )
    )
    table_001.add(
        TableCell(Paragraph("$ " + str(total), horizontal_alignment=Alignment.RIGHT))
    )
    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    table_001.no_borders()
    return table_001


def main():
    # Create document
    pdf = Document()

    # Add page
    page = Page()
    pdf.add_page(page)

    # create PageLayout
    page_layout: PageLayout = SingleColumnLayout(page)
    #page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)
    page_layout.vertical_margin = 0

    page_layout.add(
        Image(
            "https://cmeabaysection.org/wp-content/themes/cmeabaysection/_/images/shared/logo-cmea-bay-section.png",
            width=Decimal(300),
            height=Decimal(60),
        )
    )

    # Invoice information table
    page_layout.add(_build_invoice_information())

    # Empty paragraph for spacing
    page_layout.add(Paragraph(" "))

    # Billing and shipping information table
    page_layout.add(_build_billing_and_shipping_information())

    # Empty paragraph for spacing
    page_layout.add(Paragraph(" "))

    # Itemized description
    page_layout.add(
        _build_itemized_description_table(
            [
                Product("SHS Symphonic Wind Ensemble", 2, 350),
                Product("SHS String Orchestra", 3, 350),
                Product("SHS Saratoga Symphony Orchestra", 2, 350),
            ]
        )
    )

    # store the PDF
    with open(Path("boitz_invoice.pdf"), "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)


if __name__ == "__main__":
    main()
