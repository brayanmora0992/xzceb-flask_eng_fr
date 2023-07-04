import unittest

from translator import english_to_french, french_to_english

class EnglishTranslation(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'), 'bonjour') #test when the string 'Hello' is given as input the output should be Bonjour

class FrenchTranslation(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('bonjour'), 'hello') #test when the string 'Bonjour' is given as input the output should be Hello

unittest.main()