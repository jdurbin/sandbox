def _build_invoice_information0():
    table_001 = FixedColumnWidthTable(number_of_rows=5, number_of_columns=3)

    table_001.add(Paragraph("Make payment to:",font="Helvetica-Bold"))
    table_001.add(
        Paragraph("Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT)
    )
    now = datetime.now()
    table_001.add(Paragraph("%d/%d/%d" % (now.month,now.day,now.year)))

    table_001.add(Paragraph("CMEA Bay Section"))
    table_001.add(
        Paragraph(
            " ", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT
        )
    )
    #table_001.add(Paragraph("%d" % random.randint(1000, 10000)))

    table_001.add(Paragraph("Executive Treasurer"))
    table_001.add(
        Paragraph(
            "Due Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT
        )
    )
    table_001.add(Paragraph("%d/%d/%d" % (now.month,now.day, now.year)))

    table_001.add(Paragraph("P.O. Box 4344"))
    table_001.add(Paragraph(" "))
    table_001.add(Paragraph(" "))

    table_001.add(Paragraph("Modesto, CA 95353"))
    table_001.add(Paragraph(" "))
    table_001.add(Paragraph(" "))

    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
    table_001.no_borders()
    return table_001