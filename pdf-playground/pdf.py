import PyPDF2
import sys

# inputs = sys.argv[1:]


# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')


# # must be rb to read as binary
# with open('twopage.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     writer = PyPDF2.PdfWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

# reader = PyPDF2.PdfReader('twopage.pdf')
# page = reader.pages[0]
# print(page.extract_text())


# adding watermark to pages
pdf_file = 'twopage.pdf'
watermark = 'wtr.pdf'
merged = 'merged.pdf'

with open(pdf_file, 'rb') as input_file, open(watermark, 'rb') as watermark_file:
    input_pdf = PyPDF2.PdfFileReader(input_file)
    watermark_pdf = PyPDF2.PdfFileReader(watermark)
    watermark_page = watermark_pdf.getPage(0)

    output = PyPDF2.PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        pdf_page = input_pdf.getPage(i)
        pdf_page.mergePage(watermark_page)
        output.addPage(pdf_page)

    with open('merged.pdf', 'wb') as new_file:
        output.write(new_file)
