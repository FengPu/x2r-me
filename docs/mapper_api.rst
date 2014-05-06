.. _mapper_api:

Mapper
~~~~~~~

      Given a RDF content, a URI mapping and an output format, this mapper service replaces URIs based on the URI mapping and return a RDF file in the output format

Web API Definition
^^^^^^^^^^^^^^^^^^

.. http:post:: /mapper{?rdfContent, mapping, format}



   :query rdfContent: (required) This specifies the content of RDF to be processed. 
   :query mapping: (required) This specifies the information needed for `mapper` to update the URIs found in rdfContent.
   :query format: (optional) This specifies the format of output.
   :resheader Content-Type: application/rdf+xml
   :statuscode 200: no error
   :statuscode 404: exception


Query Parameter Format Detail
*****************************

:rdfContent:

:mapping:

:format:

Response Format Detail
**********************

Content-Type: application/rdf+xml
	  
Example
^^^^^^^

   **Example request**:

   .. sourcecode:: http

      POST /mapper?rdfContent&mapping&format HTTP/1.1


   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/rdf+xml

     <?xml version="1.0" encoding="UTF-8"?>
         <rdf:RDF
             xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
             xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#"
             xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
     <rdf:Description rdf:about="http://openisdm.iis.sinica.edu.tw/VR/DaTongSportsCenter">
         <rdf:type rdf:resource="http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing"/>
         <updatedAt xmlns="http://openisdm.iis.sinica.edu.tw/VR/" 
             rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2013-07-31T03:23:47Z</updatedAt>
         <geo:long>121.516</geo:long>
         <hasTelephone xmlns="http://openisdm.iis.sinica.edu.tw/VR/">2592-0055</hasTelephone>
         <hasName xmlns="http://openisdm.iis.sinica.edu.tw/VR/">Da Tong Sports Center</hasName>
         <geo:location>No.51, Dalong St., Datong Dist., Taipei City 103, Taiwan (R.O.C.)</geo:location>
         <usedFor xmlns="http://openisdm.iis.sinica.edu.tw/VR/">Sport</usedFor>
         <createdAt xmlns="http://openisdm.iis.sinica.edu.tw/VR/" 
             rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2012-11-28T09:05:13Z</createdAt>
         <geo:lat>25.0648</geo:lat>
     </rdf:Description>
     </rdf:RDF>


Related Documents
^^^^^^^^^^^^^^^^^

**See also:** 
  * :doc:`Extractor's Web API </extractor_api>`	  
  

