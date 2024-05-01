from openpyxl import Workbook

def writeExcel(vacancies):
    wb = Workbook()
    ws = wb.active
    ws.title = "Vacancies"

    for idx, vacancy in enumerate(vacancies, start=1):
        ws.cell(row=idx, column=1, value=vacancy)

    wb.save("vakansiiPython.xlsx")