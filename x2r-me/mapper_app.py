# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import Response


app = Flask(__name__)

@app.route("/mapper", methods=['POST'])
def map_rdf():
    rdfUrl = ''
    tok = Tokenizer()
    if request.method == 'POST':
        rdf = request.form['url']
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
