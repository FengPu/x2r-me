Web API 
-------

.. http:post:: /extractor{?excludedNamespaces, checkUrisStatus, rdfContent}


   :query excludedNamespaces: *(optional)* This specifies a list of namespaces to be skipped. That is, if a found URI belonged to this list, the URI will not be processed anymore.   
   :query checkUrisStatus: *(required)* This determines if `extractor` checks the status codes of found URIs. 
   :query rdfContent: *(required)* This specifies the content of RDF to be processed. 
   :resheader Content-Type: application/json
   :statuscode 200: no error
   :statuscode 404: exception
   
For the detail spec., see :doc:`Extractor Web API <extractor_api>`


.. http:post:: /mapper{?rdfContent, mapping, format}



   :query rdfContent: (required) This specifies the content of RDF to be processed. 
   :query mapping: (required) This specifies the information needed for `mapper` to update the URIs found in rdfContent.
   :query format: (optional) This specifies the format of output.
   :resheader Content-Type: application/rdf+xml
   :statuscode 200: no error
   :statuscode 404: exception   
   
For the detail spec., see :doc:`Mapper Web API <mapper_api>`

Python API
----------
This class Extractor

.. autoclass:: extractor.Extractor
   :members:
   
.. autoclass:: mapper.Mapper
   :members:
   
.. autoclass:: tokenizer.Tokenizer
   :members:
   