.. _developer_guide:


Coding Style
------------

This project follows the Python official coding style `PEP8`_.

.. _PEP8: http://legacy.python.org/dev/peps/pep-0008/

Versioning
----------

The versioning follows `Semantic Versioning 2.0`_.

.. _Semantic Versioning 2.0: http://semver.org/

Here quote the summary of Semantic Version below:

Given a version number MAJOR.MINOR.PATCH, increment the:

    MAJOR version when you make incompatible API changes,
    MINOR version when you add functionality in a backwards-compatible manner, and
    PATCH version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.


Documentation
-------------

For documentation, this project uses `Sphinx`_, which is a Python documentation generator. 
The syntax used in Sphinx is `reStructuredText`_. 
The code comments are also written in reStructuredText by which the Sphinx can generate API references automatically from the comments. This practice makes sure the consistency between code and documents to some extent.   

.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html


Here is a full code comment example quoted from `Documenting Your Project Using Sphinx`_. 

.. _Documenting Your Project Using Sphinx: https://pythonhosted.org/an_example_pypi_project/sphinx.html

The :mod:`an_example_pypi_project` contains

* An ``__init__`` file for the module.
* ``useful_1.py`` and ``useful_2.py``.  These files are IDENTICAL so I'll only
  reprint one here. 
* The ``code.rst`` file which pulls it all together. This file lives in the doc
  directory. 
  
.. note::

   The idea behind the ``auto`` directives is to keep as much documentation in 
   the code docstrings as possible.  However, Sphinx still aims to give you 
   control not found when using real auto tools like doxygen or epydoc. 
   
   Therefore, that is why you need the small stub file ``code.rst`` to bascially
   act as a director for pulling the docstrings from the code. 
   
   

Contents of ``an_example_pypi_project.__init__``::

	"""A pypi demonstration vehicle.
	
	.. moduleauthor:: Andrew Carter <andrew@invalid.com>
	
	"""
	
	import useful_1
	import useful_2
	
	
	def start():
	    "This starts this module running ..."
	    
Contents of ``an_example_pypi_project.useful_1``::

	"""	
	.. module:: useful_1
	   :platform: Unix, Windows
	   :synopsis: A useful module indeed.
	
	.. moduleauthor:: Andrew Carter <andrew@invalid.com>
	
	
	"""
	
	def public_fn_with_googley_docstring(name, state=None):
	    """This function does something.
	    
	    Args:
	       name (str):  The name to use. 
	       
	    Kwargs:
	       state (bool): Current state to be in. 
	
	    Returns: 
	       int.  The return code::
	       
	          0 -- Success!
	          1 -- No good. 
	          2 -- Try again. 
	    
	    Raises:
	       AttributeError, KeyError
	
	    A really great idea.  A way you might use me is
	    
	    >>> print public_fn_with_googley_docstring(name='foo', state=None)
	    0
	    
	    BTW, this always returns 0.  **NEVER** use with :class:`MyPublicClass`.
	    
	    """
	    return 0
	
	def public_fn_with_sphinxy_docstring(name, state=None):
	    """This function does something.
	    
	    :param name: The name to use.
	    :type name: str.
	    :param state: Current state to be in.    
	    :type state: bool.
	    :returns:  int -- the return code.      
	    :raises: AttributeError, KeyError
	
	    """
	    return 0
	
	def public_fn_without_docstring():
	    return True 
	
	def _private_fn_with_docstring(foo, bar='baz', foobarbas=None):
	    """I have a docstring, but won't be imported if you just use ``:members:``.
	    """   
	    return None
	
	
	class MyPublicClass(object):
	    """We use this as a public class example class.
	
	    You never call this class before calling :func:`public_fn_with_sphinxy_docstring`.
	    
	    .. note:: 
	      
	       An example of intersphinx is this: you **cannot** use :mod:`pickle` on this class. 
	    
	    """
	    
	    def __init__(self, foo, bar='baz'):
	        """A really simple class.
	        
	        Args:
	           foo (str): We all know what foo does. 
	           
	        Kwargs:
	           bar (str): Really, same as foo.  
	    
	        """
	        self._foo = foo
	        self._bar = bar
	
	    def get_foobar(self, foo, bar=True):
	        """This gets the foobar
	        
	        This really should have a full function definition, but I am too lazy. 
	
	        >>> print get_foobar(10, 20)
	        30
	        >>> print get_foobar('a', 'b')
	        ab
	        
	        Isn't that what you want?
	        
	        """
	        return foo + bar
	
	    def _get_baz(self, baz=None):
	        """A private function to get baz.
	        
	        This really should have a full function definition, but I am too lazy. 
	        
	        """
	        return baz

And finally, contents of ``code.rst`` which pulls it all together::

	Documentation for the Code
	**************************
	
	.. automodule:: an_example_pypi_project
	
	
	useful #1 -- auto members
	=========================
	
	This is something I want to say that is not in the docstring. 
	
	.. automodule:: an_example_pypi_project.useful_1
	   :members: 
	      
	useful #2 -- explicit members
	=============================
	
	This is something I want to say that is not in the docstring. 
	
	.. automodule:: an_example_pypi_project.useful_2
	   :members: public_fn_with_sphinxy_docstring, _private_fn_with_docstring
	   
	.. autoclass:: MyPublicClass
	   :members: get_foobar, _get_baz
	   

.. note::

   The documents like ``code.rst`` are located at /docs/. And the built documents are located at /build_docs/. 
   Currently, two formats are supported in X2R-ME, namely PDF and HTML formats. The documents are also online 
   available by linking the GitHub to ReadTheDocs services. The online X2R-ME's documents can be accessed via 
   http://x2r-me.readthedocs.org/en/latest/. 
   

			
Testing
-------

This project uses Python `unittest`_ to conduct unit testing. The test codes are located at /x2r-me/testsuite/unit/. The test fixture, such as test data and test databases, used by test suites are located at /x2r-me/testsuite/test_fixtures/. Currently, this project are not using framework for acceptance testing. And all the acceptance testing codes are located in /x2r-me/testsuite/acceptance/.  

.. _unittest: https://docs.python.org/2/library/unittest.html