import unittest

from bookpy import get_isbn_from_pdf
from bookpy import ISBNNotFoundError


class TestGetISBNFromPDF(unittest.TestCase):

    def test_isbn_clean_code_pdf(self):
        pdf_file = "pdf/clean_code.pdf"
        isbns = ('0132350882', '9780132350884')
        self.assertIn(get_isbn_from_pdf(pdf_file), isbns)

    def test_isbn_soft_skills_pdf(self):
        pdf_file = "pdf/soft_skills.pdf"
        isbns = ('1617292397', '9781617292392')
        self.assertIn(get_isbn_from_pdf(pdf_file), isbns)

    def test_isbn_introduction2algorithms(self):
        pdf_file = "pdf/introduction2algorithms.pdf"
        isbns = ('9780262033848', '0262033844')
        self.assertIn(get_isbn_from_pdf(pdf_file), isbns)

    def test_pdf_without_text(self):
        pdf_file = "pdf/without_text.pdf"
        with self.assertRaises(ISBNNotFoundError):
            get_isbn_from_pdf(pdf_file)
