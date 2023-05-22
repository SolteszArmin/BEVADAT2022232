import PyPDF2

def convert_pdf_to_text(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text = page.extract_text()
                txt_file.write(text)

# PDF és TXT fájl elérési útvonalak
pdf_file_path = '230310291.pdf'
txt_file_path = '230310291.txt'

# Fájl konvertálása
convert_pdf_to_text(pdf_file_path, txt_file_path)