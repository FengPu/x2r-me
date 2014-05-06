# -*- coding: utf-8 -*-
#    This file is part of X2R.
#
#    X2R is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    X2R is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with X2R.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
# Module Name:
#
#    tokenizer.py
#
# Abstract:


#
# Author:
#
#    Feng-Pu Yabg (Doc)
#
# Project:
#
#    OpenISDM
#
# -*-

"""
.. module:: tokenizer
   :platform: Unix, Linux, Windows
   :synopsis: tokenizer splits 

.. moduleauthor:: Feng-Pu Yang <fengpuyang@gmail.com>


"""
import re

class Tokenizer:
    """Tokenizer realizes serveral tokenization heuristics:
       
       1. identifying camelcase word
       2. identifying all captials word
       3. treat all non alphanumeric chars as delimiters
    """
    def __init__(self):
	    pass
        		
    def __filtered_camelcase(self, string):   
        """This function find and seperate 
        words of camelcase from a given
        string.

        :param string: The string to tokenize.
        :type string: str.
        :returns:  array<str> -- the array of tokens.

        """     
        splitted = [w for w in re.split(r'([A-Z][a-z]+)', string) if w]
        return splitted
        
    def __filtered_all_captials(self, string):
        """This function find and seperate 
        words of all captials from a given
        string.

        :param string: The string to tokenize.
        :type string: str.
        :returns:  array<str> -- the array of tokens.

        """
        splitted = [w for w in re.split(r'([A-Z][A-Z]+)', string) if w]
        return splitted

    def __filtered_non_alphanumeric(self, string):
        """This function find and seperate 
        words delimited by non-alphanumerics
        (letters, numbers, regardless of case)
        from a given string.

        :param string: The string to tokenize.
        :type string: str.
        :returns:  array<str> -- the array of tokens.

        """
        
        #The "\w" means "any word character" which 
        #usually means alphanumeric (letters, 
        #numbers, regardless of case) plus underscore (_). 
        #To exclude underscore, just replace it with hyphen. 
        string = string.replace("_","-")
        splitted = re.findall(r"\w+",string)
        return splitted
        
    def __normalized(self, word_array):
        """This function does normalization, which
            means to turn all tokens to lowercase
            and to connect them with whitespace.

        :param word_array: The array of tokens.
        :type word_array: array<str>.
        :returns:  str -- the lowercase tokens 
                          seperated by whitespaces.

        """
        normalized_string = (" ".join(word_array)).lower()
        return normalized_string 
        
    def tokenized(self, string):
        """This function is the integration of all known tokenizers.
        Theoretically, any compound words can be tokenized by this 
        function.  

        :param string: The string to tokenize.
        :type string: str.
        :returns:  str -- the tokenized and normalized string.

        """
        
        #non-alphanumeric delimiters based tokenize
        string = self.__filtered_non_alphanumeric(string)
        
        #case-sensitive tokenize
        intermediate_tokens = []
        for w in string:
            toks = self.__filtered_all_captials(w)
            for tok in toks:
                intermediate_tokens.append(tok)
        final_tokens = []
        for w in intermediate_tokens:
            toks = self.__filtered_camelcase(w)
            for tok in toks:
                final_tokens.append(tok)
        #normalize the final tokenized result
        result_string = self.__normalized(final_tokens)
        return result_string
    
    def tokenized_url(self, uri):
        """This function truncate the input URI's head and 
        output the tail part of the input URI. Be precisely, 
        only the tail part after the last slash will be 
        preserved. 
        For example, 
        input "http://www/xx/yy/zz-AB" will get the 
        output as "zz ab"

        :param string: The string (URI) to tokenize.
        :type string: str.
        :returns:  str -- the tokenized and normalized string.

        """
        result = ""
        split_uri = uri.split("/")
        # Test if the URI is not the toppest namespace
        if len(split_uri) > 1:
            result = self.tokenized(split_uri[-1])
        else:
            #TODO: here is the slot for handling the URI with only namespace, 
            #      i.e., without any "/"; 
            #      or invalide URI, incomplete URI
            result = self.tokenized(uri)
        return result