.. X2R documentation master file, created by
   sphinx-quickstart on Wed Jan 29 14:17:04 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Extractor and Mapper's Documentation!
=====================================
.. toctree::
   :maxdepth: 3

   intro




User Guide
__________


Extractor
^^^^^^^^^
   .. include::  ./extractor_api.rst
	


Mapper
^^^^^^
  .. include::   ./mapper_api.rst



Extractor_Obsolete
^^^^^^^^^^^^^^^^^^

* `Prerequist`: Prepare the input as acceptable RDF file formats, including

  * hturtle	
  * microdata	
  * n3	
  * nquads	
  * nt	
  * rdfa	
  * rdfa1.0	
  * rdfa1.1	
  * trix	
  * turtle	
  * xml

* `Input`:

  * By specifying the parameter, *excludenamespaces*, in the form of jsohifized list, extractor can skip URIs belonged to the excludenamespaces during the processing. For example, DBpedia is a truthworth URI holding site, users might not want to replace URIs belonged to it.  
  
    :param: excludenamespace
    :type: string (jsonified list)
  * HTTP response status codes can be used to determine if a URI is still responsive. The parameter, *status*, is set as *True* or *False* to activate or deactivate the checking of status codes for found URIs, respectively. Since the considerable latency of checking status codes, the users who care about the performance or have big RDF files will be suggested to set the parameter *status*, as False. 
  
    :param: status_check
    :type: boolean
  * The parameter *data* is used to input the content of RDF as a string. The line escape chars, such as "\\n", should be explicitly included in the string, or the functionality of lineNumber will not perform as your expectation. 
  
    :param: data
    :type: string
  

* `Major Processes`:

  1. Analyze and filter URIs from the input RDF
  2. Extract terms from URIs
  3. Verify the extracted terms 

* `Output`:

  The output is encoded in json format. The skeleton of output and an example are presented below. 

Output skeleton::
    
	{"metadata": [],
	"mapping": 
    [{"status": "", 
	  "originalURI": "", 
	  "replacedURI": "", 
	  "term": "", 
	  "lineNumbers": ""}]}
	  


Example of the output::


    {"metadata": [],
	"mapping": 
    [{"status": "N/A", 
	  "originalURI": "http://140.109.21.188/facilities#store214", 
	  "replacedURI": "", 
	  "term": "facilities store214", 
	  "lineNumbers": "3,31"}, 
	 {"status": "N/A", 
	  "originalURI": "http://140.109.21.188/facilities#store190", 
	  "replacedURI": "",  
	  "term": "facilities store190", 
	  "lineNumbers": "1,30"}]}


Mapper_Obsolete
^^^^^^^^^^^^^^^

* `Prerequist 1`: Prepare the input as acceptable RDF file
* `Prerequist 2`: Prepare the mapping from orignal URIs to replaced URIs



* `Input`:
  
  * The parameter *data* is used to input the content of RDF as a string. The line escape chars, such as "\\n", should be explicitly included in the string, or the functionality of lineNumber will not perform as your expectation. 
  
    :param: data
    :type: string
  
  * The parameter *mapping* specify the 

    :param: mapping
    :type: string (valid json string)
	
	
    Mapping skeleton::

      {"metadata": [],
  	"mapping": 
      [{"status": "", 
  	  "originalURI": "must-have", 
  	  "replacedURI": "must-have", 
  	  "term": "", 
  	  "lineNumbers": ""}]} 
	
	
  * User can determine the RDF format of output by specifying the parameter *format*.
   
    :param: format
    :type: string 
	
    * hturtle	
    * microdata	
    * n3	
    * nquads	
    * nt	
    * rdfa	
    * rdfa1.0	
    * rdfa1.1	
    * trix	
    * turtle	
    * xml
  

* `Major Process`:

  1. Replace orignal URIs with suggested URIs

* `Output`:

  RDF file in the format specified by the parameter *format*.


General Concept
^^^^^^^^^^^^^^^


Both extractor and mapper are realized in the form of web service. The default entry point of extractor service and mapper service are: 

* Extractor: <Your host domain>/extractor

* Mapper: <Your host domain>/mapper

They both use POST method to pass parameters, and the details of paramters are presented below.

Extractor's input parameters: 

    * excludedNamespaces
    * checkUrisStatus
    * rdfContent

Extractor's output: 

The output of extractor service is a mapping defined in Json format.

Mapping template::
    
	{"metadata":  [],
	 "mapping":   [
	               {"status": "", 
	                "originalURI": "", 
	                "replacedURI": "", 
	                "term": "", 
	                "lineNumbers": ""
	                }
                      ]
	}


Mapper's input parameters:

    * rdfContent 
    * mapping
    * format
	
Mapper's output:

  
Developer Guide
_______________

Convensions, Coding Style, Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Coding Style: *PEP8*
* Programming Language: *Python*
* Documentation Language: *reStructuredText*
* Documentation Tool: *Sphinx*
* Testing Framework: *pyunit*
* Dependency: *Flask, RDFLib and Requests*  


Extension
^^^^^^^^^

Three types of extensions can be contributed. 

  1. The URIAnalyzer
    
    * Whitelist filter
	
    * URI status code analyzer
	
  2. The Tokenizer
  
    * Case based tokenizers

    * Delimits based tokenizers
	
  3. The Verifizer
  
    * Spell checking based verifizer

Testing
^^^^^^^

Seven representive tests for tokenizer is defined in the *TokenizerTest* as follows. Developers, who tend to modify or extend this project should pass these tests. If there are some more typical tests, developers can also add them into *TokenizerTest*.::

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

ToDo
^^^^

1. Verifizers
  * Current version of Extractor hasn't realized the verifizer yet, and only leave the hook. One planned verifizer is the spell checking verifizer. 
2. Translator Map
  * Although finding the proper translators to translate raw data into acceptable format is out of the scope of our project. However, a translator map can greatly reduce the barriers to entry for X2R.  


Content Search
==================

* :ref:`search`




