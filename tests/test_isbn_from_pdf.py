import unittest

from bookpy import get_isbn_from_pdf
from bookpy import ISBNNotFoundError


class TestGetISBNFromPDF(unittest.TestCase):

    def test_gnu_make(self):
        pdf_file = "tests_resources/gnu_make.pdf"
        isbns = ('0596006101', '9780596006105')
        self.assertIn(get_isbn_from_pdf(pdf_file), isbns)

    def test_pdf_without_isbn(self):
        pdf_file = "tests_resources/no_isbn.pdf"
        with self.assertRaises(ISBNNotFoundError):
            get_isbn_from_pdf(pdf_file)

    def test_no_pdf(self):
        file_ = "tests_resources/no_pdf.png"
        with self.assertRaises(ISBNNotFoundError):
            get_isbn_from_pdf(file_)
