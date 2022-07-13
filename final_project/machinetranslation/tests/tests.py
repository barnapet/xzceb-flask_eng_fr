import unittest

from .translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test_1(self): 
        self.assertMultiLineEqual(english_to_french("Hello"), 'Bonjour') # test when "Hello" is given as input the output is "Bonjuor".
        self.assertIsNone(english_to_french(None))  # test when None is given as input the output is an error.

class TestFrenchToEnglish(unittest.TestCase): 
    def test_1(self): 
        self.assertEqual(french_to_english("Bonjour"), 'Hello') # test when "Bonjour" is given as input the output is "Hello".
        self.assertIsNone(french_to_english(None))  # test when None is given as input the output is an error.

unittest.main()
