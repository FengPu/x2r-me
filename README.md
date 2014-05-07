X2R-ME
======

X2R is a Tool Set for translating raw data into Linked Data.
X2R is composed of several tools:

   * Extractor
   * USS
   * UMS
   * Mapper

This repository hosts two tools of X2R, **Extractor** and **Mapper**, 
together called as **X2R-ME**.

*Extractor* is a tool to extract URIs from a given RDF, and then turn
these URIs into query terms. The purpose of Extractor is to find the
opportunity of improving the quality of URI used in the given RDF. By
generating query terms, other X2R tools, USS and UMS, can help in
finding or minting better URIs.

*Mapper* is a tool for systematically replacing URIs within a given RDF.
When you have the mapping from original URIs to new URIs, Mapper can
replace the URIs based on the mapping automatically.

The document of Extractor and Mapper is hosted in http://x2r-me.readthedocs.org/en/latest/

N.B. The document is continuously refining.
