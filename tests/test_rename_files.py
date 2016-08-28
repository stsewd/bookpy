from os import path
import unittest

from bookpy import rename_files


class TestRenameFiles(unittest.TestCase):

    def test_gnu_make(self):
        file_path = "tests_resources/gnu_make.pdf"
        new_file_path = "tests_resources/Managing Projects With GNU Make - Robert Mecklenburg (2004).pdf"
        rename_files([file_path])
        self.assertTrue(path.exists(new_file_path))
