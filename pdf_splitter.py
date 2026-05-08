import os
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
    

input_pdf = "2003.08934v2.pdf"
start_page = 5
end_page = 10
split_pdf(input_pdf,start_page, end_page)
# while i < len(sys.argv):
#     if sys.argv[i] == '-help' or sys.argv[i] == '-h':
#         print('\nCommand list:\n -h: Help command \n -u <url> of the video to download\n -itag <number> number of itag to download\n')
#         command_help = True
#     elif sys.argv[i] == '-f':
#         try:
#             start_page = sys.argv[i+1]
#             i = i + 1
#             show_options = False
#         except:
#             show_options = True
#     elif sys.argv[i] == '-s':
#         try:
#             url = sys.argv[i+1]
#         except:
#             print('Please specify an url after the -u parameter')
#     i = i + 1
