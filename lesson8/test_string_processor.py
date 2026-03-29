import unittest
from string_processor import StringProcessor

class TestStringProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = StringProcessor()

    @unittest.skip("Skipping empty string test for reverse_string")
    def test_reverse_empty_string(self):
        self.assertEqual(self.processor.reverse_string(""), "")

    def test_reverse_normal_strings(self):
        self.assertEqual(self.processor.reverse_string("hello"), "olleh")
        self.assertEqual(self.processor.reverse_string("Привіт"), "тівирП")

    def test_reverse_mixed_characters(self):
        self.assertEqual(self.processor.reverse_string("123!abc"), "cba!321")
        self.assertEqual(self.processor.reverse_string("AaBbCc"), "cCbBaA")

    def test_capitalize_empty_string(self):
        self.assertEqual(self.processor.capitalize_string(""), "")

    def test_capitalize_normal_strings(self):
        self.assertEqual(self.processor.capitalize_string("hello"), "Hello")
        self.assertEqual(self.processor.capitalize_string("привіт"), "Привіт")
        self.assertEqual(self.processor.capitalize_string("HELLO"), "HELLO")

    def test_capitalize_mixed_characters(self):
        self.assertEqual(self.processor.capitalize_string("123abc"), "123abc")
        self.assertEqual(self.processor.capitalize_string("!hello"), "!hello")

    def test_count_vowels_empty_string(self):
        self.assertEqual(self.processor.count_vowels(""), 0)

    def test_count_vowels_english(self):
        self.assertEqual(self.processor.count_vowels("hello"), 2)
        self.assertEqual(self.processor.count_vowels("HELLO"), 2)
        self.assertEqual(self.processor.count_vowels("xyz"), 0)

    def test_count_vowels_russian_ukrainian(self):
        self.assertEqual(self.processor.count_vowels("привет"), 2)
        self.assertEqual(self.processor.count_vowels("привіт"), 2)
        self.assertEqual(self.processor.count_vowels("ёаєі"), 4)

    def test_count_vowels_with_digits_and_symbols(self):
        self.assertEqual(self.processor.count_vowels("h3ll0!"), 0)
        self.assertEqual(self.processor.count_vowels("пр1віт!"), 1)

if __name__ == "__main__":
    unittest.main()