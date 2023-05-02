# Unit tests for the MorseCode class and functions

import unittest
import morseToEnglish as mte

class TestMorseCode(unittest.TestCase):
    def setUp(self):
        self.message = mte.MorseTranslator()

    def test_encryption(self):

        self.assertEqual(self.message.encrypt('HELLO WORLD'), '.... . .-.. .-.. ---   .-- --- .-. .-.. -..')
        self.assertEqual(self.message.encrypt('SOS'), '... --- ...')

    def test_decryption(self):
        
        self.assertEqual(self.message.decrypt('.... . .-.. .-.. ---   .-- --- .-. .-.. -..'), 'HELLO WORLD')
        self.assertEqual(self.message.decrypt('... --- ...'), 'SOS')

if __name__ == '__main__':
    unittest.main()


