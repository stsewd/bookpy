import tempfile
from subprocess import call

from isbntools.app import get_isbnlike
from isbntools.app import get_canonical_isbn
from isbntools.app import meta

from .book import Book
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


def get_book(isbn):
    book_info = meta(isbn)
    book = Book(
        isbn=book_info.get('ISBN-13', ""),
        title=book_info.get('Title', ""),
        authors=book_info.get('Authors', ""),
        year=book_info.get('Year', "")
    )
    return book
