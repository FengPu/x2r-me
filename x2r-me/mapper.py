# -*- coding: utf-8 -*-
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
#    mapper.py
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
.. module:: mapper
   :platform: Unix, Linux, Windows
   :synopsis: 

.. moduleauthor:: Feng-Pu Yang <fengpuyang@gmail.com>


"""
from rdflib import Graph
from rdflib import URIRef
from rdflib import Literal
from rdflib import BNode
import json

class Mapper:

    def __init__(self, graph):
        self.graph = graph
        self.operationCount = 0
    def replaceUri(self, oUri, uUri):
        oUriRef = URIRef(oUri)
        uUriRef = URIRef(uUri)
        

        # TODO: refactoring this block, to remove duplication
        for subject, predicate, obj in self.graph:
            if subject == oUriRef:
                self.graph.remove((subject, predicate, obj))
                self.graph.add((uUriRef, predicate, obj))
                self.operationCount = self.operationCount + 1
        # TODO: refactoring this block
        for subject, predicate, obj in self.graph:
            if predicate == oUriRef:
                self.graph.remove((subject, predicate, obj))
                self.graph.add((subject, uUriRef, obj))
                self.operationCount = self.operationCount + 1
        # TODO: refactoring this block
        for subject, predicate, obj in self.graph:
            if obj == oUriRef:
                self.graph.remove((subject, predicate, obj))
                self.graph.add((subject, predicate, uUriRef))
                self.operationCount = self.operationCount + 1
        return self.operationCount
        

    def commit(self, outputFile):
        self.graph.commit()
        ufile = open(outputFile, 'w')
        ufile.write(self.graph.serialize())
        ufile.close()
        self.graph.close()
    
    def commit(self):
        self.graph.commit()
        return self.graph.serialize()
        
    def mapping(self, json_str):
        try:
            mappings = json.loads(json_str)["mapping"]
            for mapping in mappings:
                o_uri = mapping["originalURI"]
                r_uri = mapping["replacedURI"]
                self.replaceUri(o_uri, r_uri)
        except:
            print "Json parsing error."
        return self.commit()


def main():
    g = Graph()
    g.parse("MAD_J.rdf", format="xml")
    mapper = Mapper(g)
    
    #imperative mode
    mapper.replaceUri('gr:Location', 'http://140.109.22.84/test/alf')
    mapper.replaceUri(
        'http://140.109.21.188/facilities#store175',
        'http://small')
    print mapper.commit()
    print "======================================"
    
    #batch mode
    print "next test - batch mode (press any key)"
    intrupt = raw_input()    
    batch_json = open("test_mapper_batch.json","r").read()
    print mapper.mapping(batch_json)
    
if __name__ == "__main__":
    main()
