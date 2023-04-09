import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_french_to_english_null_input(self):
        self.assertEqual(french_to_english(''),'')

    def test_english_to_french_null_input(self):
        self.assertEqual(english_to_french(''),'')

    def test_french_to_english_with_word(self):
        translation = french_to_english('Bonjour')
        self.assertEqual(translation["translations"][0]["translation"],'Hello')

    def test_english_to_french_with_word(self):
        translation = english_to_french('Hello')
        self.assertEqual(translation["translations"][0]["translation"],'Bonjour')

if __name__ == '__main__':
    unittest.main()
