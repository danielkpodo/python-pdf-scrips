import PyPDF2

# Reading a simple pdf file
with open("./dummy.pdf", mode='rb') as file_object:
    reader = PyPDF2.PdfFileReader(file_object)
    print(reader.getPage(0))  # gets page number
