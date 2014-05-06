from extractor import Extractor
from rdflib import Graph
import StringIO
def test():
    g = Graph()
    #g.parse("MAD_D.rdf", format="xml")
    f = open("./testsuite/test_fixtures/MAD_D.rdf", 'rb')
    st = f.read().decode('utf-8')
    print type(st)
    g.parse(StringIO.StringIO(st.encode('utf-8')),  format="xml")
    ext = Extractor(g)
    uris = ext.getUris()
    print ext.terms()
    ext.getBnodes()

test()