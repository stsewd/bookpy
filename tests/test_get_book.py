import unittest

from fuzzywuzzy import fuzz

from bookpy import get_book
from bookpy import Book


MIN_EDIT_DISTANCE = 80


class TestGetBook(unittest.TestCase):

    def test_get_book_clean_code(self):
        expected_book = self._get_default_book('clean_code')
        actual_book = get_book(expected_book.isbn())
        self.assertAlmostEqualBooks(actual_book, expected_book)

    def test_get_book_soft_skills(self):
        expected_book = self._get_default_book('soft_skills')
        actual_book = get_book(expected_book.isbn())
        self.assertAlmostEqualBooks(actual_book, expected_book)

    def test_get_book_introduction_to_algorithms(self):
        expected_book = self._get_default_book('introduction2algorithms')
        actual_book = get_book(expected_book.isbn())
        self.assertAlmostEqualBooks(actual_book, expected_book)

    def assertAlmostEqualBooks(self, first, second):
        # With the main author is enough for now
        self.assertSimilarStrings(first.main_author(), second.main_author())
        self.assertSimilarStrings(first.title(), second.title())
        self.assertSimilarStrings(first.short_title(), second.short_title())
        self.assertYear(first.year(), second.year())

    def assertSimilarStrings(self, first, second):
        if not first or not second:  # It's ok a empty string
            return
        edit_dist = fuzz.partial_ratio(self._cleanstr(first), self._cleanstr(second))
        self.assertGreaterEqual(edit_dist, MIN_EDIT_DISTANCE)

    @staticmethod
    def _cleanstr(s):
        return s.lower().strip()

    def assertYear(self, first, second):
        if not first or not second:  # It's ok a empty string
            return
        self.assertEqual(first, second)

    @staticmethod
    def _get_default_book(title):
        books = {
            'clean_code': Book(
                isbn="9780132350884",
                title="Clean Code: A hanbook of agile software craftsmanship",
                authors=["Robert C. Martin"],
                year="2009"
            ),

            'soft_skills': Book(
                isbn="9781617292392",
                title="Soft Skills : The software developer's life manual",
                authors=["John Z. Sonmez"],
                year="2014"
            ),

            'introduction2algorithms': Book(
                isbn="9780262033848",
                title="Introduction to algorithms",
                authors=["Thomas H. Cormen"],
                year="2009"
            )
        }
        return books[title]
