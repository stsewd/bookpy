from os import path
import unittest

from bookpy import rename_files


class TestRenameFiles(unittest.TestCase):

    def test_rename_clean_code_pdf(self):
        file_path = "pdf/clean_code.pdf"
        new_file_path = "pdf/Clean code - Robert C. Martin.pdf"
        rename_files([file_path])
        self.assertTrue(path.exists(new_file_path))

    def test_rename_soft_skills_pdf(self):
        file_path = "pdf/soft_skills.pdf"
        new_file_path = "pdf/Soft Skills - John Z. Sonmez (2014).pdf"
        rename_files([file_path])
        self.assertTrue(path.exists(new_file_path))
