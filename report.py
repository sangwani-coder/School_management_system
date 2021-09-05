# imports module
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date

# creating the paragraph with
# the heading text and passing the styles of it
# standard stylesheet defined within reportlab itself
styles = getSampleStyleSheet()

# fetching the style of Top level heading (Heading1)
title_style = styles["Heading1"]

# 0: left, 1: center, 2: right
title_style.alignment = 1
try:
    title = input("School name: ")
    reciever = input("receipt issuer: ")
    title = Paragraph(title + " Receipt", title_style)

    # creating a Base Document Template of page size A4
    receipt = input("received from:")
    pdf = SimpleDocTemplate(f"{receipt}.pdf", pagesize=A4)

    # creates a Table Style object and in it,
    # defines the styles row wise
    # the tuples which look like coordinates
    # are nothing but rows and columns
    style = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (4, 4), 1, colors.black),
            ("BACKGROUND", (0, 0), (3, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )
    # data which we are going to display as tables
    pay_date = date.today()
    name = input('students name: ').upper()
    grade = input('class: ')
    term = input("term: ")
    amount = int(input('amount: '))
    amount_words = input("amount in words: ")
    purpose = input("purpose of payment: ")
    # tuition = input("tuition Fee: ")
    # fines = int(input("Fines: "))
    # transport = int(input("transport fees: "))
    # other = int(input("other: "))
    pay_mode = input("paid by cash, cheque, bank: ")
    balance = 4000 - amount

    DATA = [
        ["Date: " + str(pay_date) + "          receipt#: " + "2021"],
        ["Student Name: " + name + "            Amount Paid (ZMW.): " + str(amount)],
        ["Received from: " + receipt + "         Amount in words: " + amount_words],
        ["Class: " + grade],
        ["Balance Due: " + str(balance)],
        ["for payment of: " + purpose + "       School Term:" + term],
        ["Paid by: " + pay_mode],
        ["Received by: " + reciever + "          sign: "],
    ]
    # creates a table object and passes the style to it
    table = Table(DATA, style=style)

    # final step which builds the
    # actual pdf putting together all the elements
    pdf.build([title, table])
    print("receipt printed")
except Exception as e:
    print(e)
