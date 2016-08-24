import os
import tempfile
import mimetypes
from subprocess import call

from isbntools.app import get_isbnlike
from isbntools.app import get_canonical_isbn
from isbntools.app import meta

from .book import Book
from .errors import ISBNNotFoundError


class BookpyError(Exception):
    pass


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


def _get_text_from_pdf(pdf_file, first_page=1, last_page=6):
    with tempfile.NamedTemporaryFile() as temp_file:
        output = temp_file.name
        _pdf_to_text_tool(pdf_file, output, first_page, last_page)
        return _get_text_from_file(output)


def get_isbn_from_pdf(pdf_file):
    pdf_text = _get_text_from_pdf(pdf_file)
    for isbn_like in get_isbnlike(pdf_text, level='normal'):
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


def pdf_handler(file_path):
    isbn = get_isbn_from_pdf(file_path)
    return get_book(isbn)


def _get_type_handler(file_type):
    supported_types = {
        'application/pdf': pdf_handler
    }
    try:
        handler = supported_types[file_type]
        return handler
    except KeyError:
        raise BookpyError("File type not supported: " + file_type)


def _get_new_name(old_file_path, new_file_name):
    path = os.path.dirname(old_file_path)
    new_file_path = os.path.join(path, new_file_name)
    return new_file_path


def rename_file(file_path, pattern, **kwargs):
    file_type = mimetypes.guess_type(file_path)[0]
    handler = _get_type_handler(file_type)
    book = handler(file_path)
    book_name = book.name(pattern, **kwargs)
    new_name = _get_new_name(file_path, book_name)
    os.rename(file_path, new_name)


def rename_files(files_list, pattern="{short_title} - {main_author} ({year})", **kwargs):
    # TODO threading
    for file_path in files_list:
        rename_file(file_path, pattern, **kwargs)
