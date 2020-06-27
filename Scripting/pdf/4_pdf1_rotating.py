import PyPDF2

with open('1.pdf','rb') as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print('número de páginas:', reader.numPages)
    page = reader.getPage(0)
    print(page.rotateCounterClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as file2:
        writer.write(file2)

    
