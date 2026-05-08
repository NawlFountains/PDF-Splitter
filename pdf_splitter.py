import os
import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter

def split_pdf(original_pdf, start_page, end_page):
    output_name = f"{os.path.splitext(original_pdf)[0]}({start_page}-{end_page}).pdf"
    reader = PdfReader(original_pdf)
    writer = PdfWriter()
    page_range = range(start_page, end_page + 1)

    for page_num, page in enumerate(reader.pages, 1):
        if page_num in page_range:
            writer.add_page(page)
    
    with open(output_name, "wb") as out:
        writer.write(out)
    
    print(f"Saved pdf {output_name}")
    

parser = argparse.ArgumentParser(description="Split a PDF by page range")
parser.add_argument("pdf", help="Path to the input PDF file")
parser.add_argument("start", type=int, help="Start page number")
parser.add_argument("end", type=int, help="End page number")
args = parser.parse_args()

split_pdf(args.pdf, args.start, args.end)