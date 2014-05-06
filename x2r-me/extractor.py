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
#    extractor.py
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
.. module:: extractor
   :platform: Unix, Linux, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Feng-Pu Yang <fengpuyang@gmail.com>


"""
from rdflib import Graph
from rdflib import URIRef
from rdflib import Literal
from rdflib import BNode
from sets import Set
from tokenizer import Tokenizer
import requests
import StringIO

class Extractor:
    """Extractor parses an RDF content and provides services:
    
       1. extract URIs
       2. extract Blank Nodes
       3. look up for URI's line number
       4. translate URIs into terms
    """

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    def __init__(self, graph):
        self.graph = graph
        self.triple_count = 0
        self.tokenizers = []
    def getUris(self):
        '''This function is used to extract URIs.
        
        :returns:  Array<str>. This function returns an array of URIs.
        
        '''
        uris = set()
        
        for subject, predicate, obj in self.graph:
            self.triple_count = self.triple_count + 1
            if isinstance(subject, URIRef):
                uris.add(subject)
            if isinstance(predicate, URIRef):
                uris.add(predicate)
            if isinstance(obj, URIRef):
                uris.add(obj)
            if not (subject, predicate, obj) in self.graph:
                raise Exception("Iterator / Container Protocols are Broken!!")
        print str(len(uris)) + ' URIs were found!'
        return uris

    def getBnodes(self):
        '''This function is used to extract blank nodes.
        
        :returns:  Array<str>. This function returns an array of blank nodes.
        
        '''
        bnodes = set()
        for subject, predicate, obj in self.graph:
            if isinstance(subject, BNode):
                bnodes.add(subject)
            if isinstance(obj, BNode):
                bnodes.add(obj)
        print str(len(bnodes)) + ' blank nodes were found!'
        return bnodes
    # make later defined extractMethods can be dynamically loaded

    def terms(self):
        return [uri.split("/")[-1].split("#")[-1] for uri in self.getUris()]

    def testUri(self, uri):
        '''This function is used to test if the "uri" is reachable.
        
        :param uri: the uri for testing reachability.
        :type uri: str.
        :returns:  boolean. True for reachable and False for unreachable.
        
        '''
        status = ""
        test = ""
        try:
            status = requests.get(uri).status_code 
        except:
            status = "except" 
        if str(status) == "200" or str(status) == "303":
            test = "1"
        else:
            test = "0"
        return test
    def get_lines(self, sio, lookup_term):    
        '''This function is used to look up "lookup_term" inside the given RDF content.
        
        :param lookup_term: the uri for look up.
        :type lookup_term: str.
        :returns:  str. A string with all the line numbers, where the luupup_term is found,
                        used "," as the delimiter.
        
        '''
        sio.seek(0)        
        nums = []
        for num, line in enumerate(sio, 1):
            if lookup_term in line:
                nums.append(str(num))
        return ','.join(nums)

    def getTripleCount(self):
        return self.triple_count


def main():
    g = Graph()
    #g.parse("MAD_D.rdf", format="xml")
    f = open("MAD_D.rdf", 'rb')
    st = f.read().decode('utf-8')
    print type(st)
    g.parse(StringIO.StringIO(st.encode('utf-8')),  format="xml")
    ext = Extractor(g)
    uris = ext.getUris()
    print ext.terms()
    ext.getBnodes()
if __name__ == "__main__":
    main()
