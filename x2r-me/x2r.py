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
#    x2r.py
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
 
from rdflib import Graph
from rdflib import URIRef
from rdflib import Literal
from rdflib import BNode
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import Response
from extractor import Extractor
from mapper import Mapper
from tokenizer import Tokenizer
from map_factory import *
from sets import Set
import requests
import StringIO
import json
import re


"""
.. module:: x2r
   :platform: Unix, Linux, Windows
   :synopsis: Wrap the python implemntations of Extractor and Mapper as HTTP (POST) services

.. moduleauthor:: Feng-Pu Yang <fengpuyang@gmail.com>

"""

app = Flask(__name__)

@app.route("/extractor")
def ext():
    return render_template('extractor.html')

@app.route("/extract", methods=['POST'])
def ext_json():
    rdfUrl = ''
    tok = Tokenizer()
    if request.method == 'POST':
        rdf = request.form['data']
        status_test = "0"#request.form['status']
        filters = ""#request.form['exculdeurls']
        #rdf = "http://jpp.no-ip.org/MAD_J.rdf"
        try:
            #r = requests.get(rdf)
            gg = Graph()
            #g.load(rdfUrl)
            rdf_content = StringIO.StringIO(rdf.encode('utf-8'))
            #print rdf_content.readline()
            gg.parse(rdf_content,  format="xml")
            ext = Extractor(gg)
            uris = ext.getUris()
            mapping = MapFactory()
            for uri in uris:
                term = tok.tokenized_url(uri)
                uri_status = ""
                if status_test == "1":
                    uri_status = ext.testUri(uri)
                else:
                    uri_status = "N/A"  
                uri_lookup = str(uri)+"\"" 
                lnum = ext.get_lines(rdf_content, uri_lookup)          
                ent = MapEntry(uri, term, "", lnum, uri_status)
                mapping.add(ent)
            jsonized_result = json.dumps(mapping.get())              
            return Response(jsonized_result, mimetype='application/json')
        except requests.exceptions.ConnectionError:
            X2Rwarning = 'X2R Warning: The requested URL raises ConnectionError~!!!'
            return X2Rwarning


@app.route("/extractingResult", methods=['POST'])
def ext_result():
    rdfUrl = ''
    if request.method == 'POST':
        rdfUrl = request.form['url']
        try:
            r = requests.get(rdfUrl)
            #rdfUrl = str(r.status_code)
            g = Graph()
            #g.parse("MAD.rdf", format="xml")
            g.load(rdfUrl)
            ext = Extractor(g)
            uris = ext.getUris()
            terms = ext.terms()
            result = {}
            result['uris'] = uris
            result['terms'] = terms
            result['bNodes'] =str(len(ext.getBnodes()))
            result['uNodes'] = str(len(uris))
            return render_template('index.html', result= result)
        except requests.exceptions.ConnectionError:
            X2Rwarning = 'X2R Warning: The requested URL raises ConnectionError~!!!'
            return X2Rwarning


@app.route("/mapper")
def mapp():
    pass
    return render_template('mapper.html')


@app.route("/mappingRdf", methods=['POST'])
def map_result():
    
    if request.method == 'POST':
        rdf = request.form['data']
        try:
            gg = Graph()
            rdf_content = StringIO.StringIO(rdf.encode('utf-8'))
            gg.parse(rdf_content,  format="xml")
            mapper = Mapper(gg)
            #TODO-remove this test block after release
            batch_json = open("test_mapper_batch.json","r").read()
            result = mapper.mapping(batch_json)
            #End TODO-remove this test block after release
            return Response(result, mimetype='application/rdf+xml') 
        except:
            pass
                

def main():
    tok = Tokenizer()
    mapping = MapFactory()
    uris = ["http://abc.ee.ntu/alf_123", "http://sc.e.ncli.ABCdefGU"]
    for uri in uris:
        term = tok.tokenized_url(uri)
        ent = MapEntry(uri, term, "", "", "")
        mapping.add(ent)
    jsonized_result = json.dumps(mapping.get())   
    print jsonized_result   


if __name__ == "__main__":
    #main()
    app.run(port=8080, debug=True)