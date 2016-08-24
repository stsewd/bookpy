import tempfile
from subprocess import call

from isbntools.app import get_isbnlike
from isbntools.app import get_canonical_isbn

from . import utils
from .errors import ISBNNotFoundError


def _pdf_to_text_tool(pdf_file, output, first_page, last_page):
    first_page, last_page = map(str, (first_page, last_page))
    call([
        'pdftotext',
        pdf_file,
        '-f', first_page,
        '-l', last_page,
        '-q',  # Don't print any messages or errors
        output,
    ])


def _get_text_from_pdf(pdf_file, first_page=1, last_page=6):
    with tempfile.NamedTemporaryFile() as temp_file:
        output = temp_file.name
        _pdf_to_text_tool(pdf_file, output, first_page, last_page)
        return utils.get_text_from_file(output)


def get_isbn_from_pdf(pdf_file):
    pdf_text = _get_text_from_pdf(pdf_file)
    for isbn_like in get_isbnlike(pdf_text, level='normal'):
        isbn = get_canonical_isbn(isbn_like)
        if isbn:
            return isbn
    else:
        raise ISBNNotFoundError(pdf_file)


def handler(file_path):
    isbn = get_isbn_from_pdf(file_path)
    return isbn
