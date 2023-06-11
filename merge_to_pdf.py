from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import os
from datetime import datetime


def merge_jpg_to_pdf(jpg_files, output_pdf):
    instagram_page_size = (1080, 1080)
    c = canvas.Canvas(output_pdf, pagesize=instagram_page_size)

    for jpg_file in jpg_files:
        # drawImage(image, x, y, width=None, height=None, mask=None)
        # c.drawImage(jpg_file, 0, 0, letter[0], letter[1])
        c.drawImage(jpg_file, 0, 0)

        # Add a new page for the next image
        c.showPage()

    c.save()


if __name__ == "__main__":
    DIRECTORY = "images/TS/"
    jpg_files = os.listdir(DIRECTORY)
    jpg_files = [f"{DIRECTORY}/{jpg_file}" for jpg_file in jpg_files]

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_pdf = f"taylorswift_{current_time}.pdf"

    merge_jpg_to_pdf(jpg_files, output_pdf)
