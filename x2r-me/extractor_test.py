import requests
import json
import urllib, urllib2
import struct
  
def test_post(test_file):
    test_file = open(test_file, 'rb')
    rdf_content = test_file.read().decode('utf-8').encode('ascii', 'ignore')
    excluded_namespaces = []
    excluded_namespaces_str = json.dumps(excluded_namespaces)
    payload = {'excludedNamespace': excluded_namespaces_str,
               'data': rdf_content, 
               'format': 'xml-rdf'
              }
    ws_url = "http://127.0.0.1:8080/extract"
    response = requests.post( ws_url , data=payload)
    print response.text

def main():
    test_post("./test_data/MAD_Example.rdf")
    
if __name__ == "__main__":
    main()