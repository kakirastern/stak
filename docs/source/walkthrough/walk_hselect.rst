=============
Hselect Usage
=============

Hselect is a Python replacement for the IRAF Hselect task.  The :doc:`Hselect <../api/stak.Hselect>`
class searches through the headers of the provided FITS files and returns the requested Header
keywords in the form of an `Astropy data table <http://docs.astropy.org/en/stable/table/>`_. The
astropy table can be accessed through the ``table`` attribute. Below is a simple example::

    >>> from stak import Hselect
    >>> my_selection = Hselect("my_file.fits", "FILENAME,BUNIT")
    >>> print my_selection.table

       
Optional Parameters
-------------------
  
There are several optional inputs you can provide to narrow your search results.
The first is the extension keyword, which takes in a tuple of extensions.  If no
extension is provided Hselect will use all header extensions in the file.

.. code-block:: python

    >>> my_selection2 = Hselect("my_file.fits", "FILENAME,BUNIT", extension=(0,1))

Another optional input is to provide Hselect with an expression to be evaluated against a
specific keyword.  This can be any operator in the set ``=,<,>,<=,>=``. If you wish to
evaluate the keyword value as a string remember to enclose the value in quotes.

.. code-block:: python

    >>> my_selection3 = Hselect("my_file.fits", "FILENAME,BUNIT,TIME-OBS",expression="BUNIT='ELECTRONS')

You can combine multiple evaluations using ``OR`` and ``AND``, making sure to include
parenthesis where appropriate.

.. code-block:: python

    >>> my_selection3 = Hselect("my_file.fits", "FILENAME,BUNIT,TIME-OBS",
    ...                          expression="BUNIT='ELECTRONS' AND TIME-OBS > 500)

    >>> my_selection4 = Hselect("my_file.fits", "FILENAME,BUNIT,TIME-OBS",
    ...                          expression="(BUNIT='ELECTRONS' OR BUNIT='ELECTRONS/S') AND TIME-OBS > 500)

See the `Astropy documentation <http://docs.astropy.org/en/stable/table/>`_ for more details on
using Astropy tables (sorting, modifying, etc).
