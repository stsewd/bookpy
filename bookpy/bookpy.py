import tempfile
from subprocess import call

from isbntools.app import get_isbnlike
from isbntools.app import get_canonical_isbn

from .errors import ISBNNotFoundError


def _pdf_to_text_tool(pdf_file, output, first_page, last_page):
    first_page, last_page = map(str, (first_page, last_page))
    call([
        'pdftotext',
        pdf_file,
        '-f', first_page,
        '-l', last_page,
        output
    ])


def _get_text_from_file(file_name):
    with open(file_name, mode='r') as file:
        return file.read()


def _get_text_from_pdf(pdf_file, first_page, last_page):
    with tempfile.NamedTemporaryFile() as temp_file:
        output = temp_file.name
        _pdf_to_text_tool(pdf_file, output, first_page, last_page)
        return _get_text_from_file(output)


def get_isbn_from_pdf(pdf_file, first_page=1, last_page=5):
    pdf_text = _get_text_from_pdf(pdf_file, first_page, last_page)
    for isbn_like in get_isbnlike(pdf_text, level='strict'):
        isbn = get_canonical_isbn(isbn_like)
        if isbn:
            return isbn
    else:
        raise ISBNNotFoundError(pdf_file)
