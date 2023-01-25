from docx import Document


def save_to_docx(text_result):
    file_name = './result.docx'
    document = Document(file_name)
    document.add_paragraph(text_result)
    document.save(file_name)
