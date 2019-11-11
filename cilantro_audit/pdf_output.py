from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

class PdfOutput():

    def __init__(self, pdf_file_name):
        self.canvas = canvas.Canvas(pdf_file_name, pagesize=letter)

    def create_page(self):
        self.canvas.drawString(100, 100, "BLANK ATM")

home_dir = os.environ['HOME']
dir_path = home_dir + "/cilantroPdfOutput/"

if os.access(dir_path, os.F_OK) is False: # If output dir doesn't already exist
    if os.access(home_dir, os.W_OK) is False: # If we have don't write access in home directory
        print("Can't create output folder; access denied.")
        exit()
    else: # create the output dir
        os.mkdir(dir_path)

path = dir_path + "blank.pdf"

pdf = PdfOutput(path)
pdf.create_page()
pdf.canvas.showPage()
pdf.canvas.save()
