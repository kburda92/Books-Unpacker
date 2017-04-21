import unittest
from Book import Book
from os import *
from Utils import Format

class TestBook(unittest.TestCase):
    def property_test(self):
        book = Book(r"C:\Users\Krzysztof\Downloads\An_Introduction_to_GCC-Brian_Gough.pdf")
        actual = book.path
        expected = r"C:\Users\Krzysztof\Downloads"
        self.assertEqual(actual, expected)
        actual = book.name
        expected = "An_Introduction_to_GCC-Brian_Gough"
        self.assertEqual(actual, expected)
        actual = book.ext
        expected = Format.PDF
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
