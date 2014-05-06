.. highlight:: python
Test Doc Ref
^^^^^^^^^^^^

.. _code-examples:

Showing code examples
---------------------

.. index:: pair: code; examples
           single: sourcecode

Examples of Python source code or interactive sessions are represented using
standard reST literal blocks.  They are started by a ``::`` at the end of the
preceding paragraph and delimited by indentation.

Representing an interactive session requires including the prompts and output
along with the Python code.  No special markup is required for interactive
sessions.  After the last line of input or output presented, there should not be
an "unused" primary prompt; this is an example of what *not* to do::

   >>> 1 + 1
   2
   >>>

Syntax highlighting is done with `Pygments <http://pygments.org>`_ (if it's
installed) and handled in a smart way:

* There is a "highlighting language" for each source file.  Per default, this is
  ``'python'`` as the majority of files will have to highlight Python snippets,
  but the doc-wide default can be set with the :confval:`highlight_language`
  config value.

* Within Python highlighting mode, interactive sessions are recognized
  automatically and highlighted appropriately.  Normal Python code is only
  highlighted if it is parseable (so you can use Python as the default, but
  interspersed snippets of shell commands or other code blocks will not be
  highlighted as Python).

* The highlighting language can be changed using the ``highlight`` directive,
  used as follows::
