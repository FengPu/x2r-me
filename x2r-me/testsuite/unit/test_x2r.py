
import unittest

from x2r import Tokenizer

class TokenizerTest(unittest.TestCase):
    
    def setUp(self):
        self.tokenizer = Tokenizer()
    
    def tearDown(self):
        self.tokenizer = None 
    
    def test_capitalized_words(self):
        test_str = "CapitalizedWords"
        test_oracle = "capitalized words"
        self.assertEqual(self.tokenizer.tokenized(test_str), test_oracle)
    
    def test_camelCase(self):
        test_str = "CapitalizedWords"
        test_oracle = "capitalized words"
        self.assertEqual(self.tokenizer.tokenized(test_str), test_oracle)
        
    def test_uppercase(self):
        test_str = "UPPERCASElowercase"
        test_oracle = "uppercase lowercase"
        self.assertEqual(self.tokenizer.tokenized(test_str), test_oracle)
        
    def test_lowercase_with_delimits(self):
        test_str = "lower_case_with_underscores"
        test_oracle = "lower case with underscores"
        self.assertEqual(self.tokenizer.tokenized(test_str), test_oracle)
        
    def test_uppercase_with_delimits(self):
        test_str = "UPPER_CASE_WITH_UNDERSCORES"
        test_oracle = "upper case with underscores"
        self.assertEqual(self.tokenizer.tokenized(test_str), test_oracle)
    
    def test_abbreviation(self):
        test_str = "Abbr."
        test_oracle = "abbr"
        self.assertEqual(self.tokenizer.tokenized("Abbr."), "abbr")
        
    def test_composite(self):
        test_str = "AB/Ddf#223-oirDDD_www-Doc ddfs,sse;O-W_dd@iop^yydD!pp~qas"
        test_oracle = "ab ddf 223 oir ddd www doc ddfs sse o w dd iop yydd pp qas"
        self.assertEqual(self.tokenizer.tokenized(test_str), test_oracle)
        
        
