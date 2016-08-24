import unittest

from fuzzywuzzy import fuzz

from bookpy import get_book
from bookpy import Book


MIN_EDIT_DISTANCE = 80


class TestGetBook(unittest.TestCase):

    def test_gnu_make(self):
        expected_book = self._get_default_book('gnu_make')
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
            self.assertTrue(True)
        else:
            edit_dist = fuzz.partial_ratio(self._cleanstr(first), self._cleanstr(second))
            self.assertGreaterEqual(edit_dist, MIN_EDIT_DISTANCE)

    @staticmethod
    def _cleanstr(s):
        return s.lower().strip()

    def assertYear(self, first, second):
        if not first or not second:  # It's ok a empty string
            self.assertTrue(True)
        else:
            self.assertEqual(first, second)

    @staticmethod
    def _get_default_book(title):
        books = {
            'gnu_make': Book(
                isbn="9780596552541",
                title="Managing Projects with GNU Make : the Power of GNU Make for Building Anything",
                authors=["Robert Mecklenburg"],
                year="2004"
            ),
        }
        return books[title]
