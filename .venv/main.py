import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt*")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    filename = filename.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename, ln=1)

    with open(filepath, 'r') as file:
        content = file.read()
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=0, h=8, txt=content)

    pdf.output(f"PDFs/{filename}.pdf")
