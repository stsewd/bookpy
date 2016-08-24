import os
import mimetypes

from isbntools.app import meta

from .book import Book
from . import pdfhandler


HANDLERS = {
    'application/pdf': pdfhandler.handler
}


class BookpyError(Exception):
    pass


def _get_handler(file_type):
    try:
        handler = HANDLERS[file_type]
        return handler
    except KeyError:
        raise BookpyError("File type not supported: {}".format(file_type))


def _get_new_path(old_file_path, new_file_name):
    path = os.path.dirname(old_file_path)
    new_file_path = os.path.join(path, new_file_name)
    return new_file_path


def get_isbn_from_file(file_path):
    file_type = mimetypes.guess_type(file_path)[0]
    handler = _get_handler(file_type)
    isbn = handler(file_path)
    return isbn


def get_book(isbn):
    book_info = meta(isbn)
    book = Book(
        isbn=book_info.get('ISBN-13', ""),
        title=book_info.get('Title', ""),
        authors=book_info.get('Authors', ""),
        year=book_info.get('Year', "")
    )
    return book


def _get_file_extension(file_path):
    return os.path.splitext(file_path)[1]


def _rename_file(file_path, template, **kwargs):
    isbn = get_isbn_from_file(file_path)
    book = get_book(isbn)
    new_file_name = "{book_name}{extension}".format(
        book_name=book.name(template, **kwargs),
        extension=_get_file_extension(file_path)
    )
    new_name = _get_new_path(file_path, new_file_name)
    os.rename(file_path, new_name)


def rename_files(files_list, template=None, **kwargs):
    if not template:  # Load defaulf template
        template = "{short_title}{main_author}{year}"
        kwargs = {
            'year': " ({year})",
            'main_author': " - {name}",
        }
    for file_path in files_list:
        _rename_file(file_path, template, **kwargs)
