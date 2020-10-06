from PyPDF2 import PdfFileReader, PdfFileWriter
import sys


input = sys.argv[1:]


def pdf_merger(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as out:
        pdf_writer.write(out)


pdf_merger(input, output='merged.pdf')
