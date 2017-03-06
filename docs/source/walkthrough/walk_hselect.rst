=============
Hselect Usage
=============

Hselect is a Python replacement for the IRAF Hselect task.  The
:doc:`Hselect <../api/stak.Hselect>` class searches through the headers of the
provided FITS files and returns the requested Header keywords in the form of
an `Astropy data table <http://docs.astropy.org/en/stable/table/>`_. The
Astropy table can be accessed through the ``table`` attribute. Below is a
simple example::

    >>> from stak import Hselect
    >>> my_selection = Hselect("my_file.fits", "FILENAME,BUNIT")
    >>> print(my_selection.table)

       
The first positional parameter provided is the filename(s).  These can be
defined several different ways. You can provide a comma separated string of
filenames: ``"my_file1.fits,myfile2.fits"``.  Or you can provide an iterable
(such as a list or tuple) with the filename
strings:``("my_file1.fits","my_file2.fits")``.  Finally, you can use the ``*``
wildcard: ``"my_file*.fits"``.

The second positional parameter is a string containing the comma separated
header keywords that should be included in the output table.  This parameter
can also include the ``*`` wildcard character: ``"FILENAME, NAXIS*"``


Optional Parameters
-------------------
  
There are several optional inputs you can provide to narrow your table results.
The first is the extension keyword, which takes in a tuple of integer
extensions. Hselect will only search the listed FITS extension headers if
provided. If no extension is provided Hselect will use all header extensions
in the file.

.. code-block:: python

    >>> my_selection2 = Hselect("my_file.fits", "FILENAME,BUNIT",
                                extension=(0,1))

Another optional input is to provide Hselect with a string defining an
assertion expression to be evaluated against a specific keyword(s).  The
expression can be defined using ``=,>,<,>=,<=`` operators in a
"keyword operator value" combination.  These inner expressions can then be
combined using AND/OR (case insensitive). Make sure to enclose any string
keyword values in the alternate quote style ``'`` or ``"``. If necessary, use
parenthesis to notate order of evaluation.

.. code-block:: python

    >>> my_selection3 = Hselect("my_file.fits", "FILENAME,BUNIT,TIME-OBS",
                                expression="BUNIT='ELECTRONS'")

You can combine multiple evaluations using ``OR`` and ``AND``, making sure to
include parenthesis where appropriate.

.. code-block:: python

    >>> my_selection3 = Hselect("my_file.fits", "FILENAME,BUNIT,TIME-OBS",
    ...                          expression="BUNIT='ELECTRONS' AND TIME-OBS > 500")

    >>> my_selection4 = Hselect("my_file.fits", "FILENAME,BUNIT,TIME-OBS",
    ...                          expression="(BUNIT='ELECTRONS' OR BUNIT='ELECTRONS/S')
                                              AND TIME-OBS > 500")

See the `Astropy documentation <http://docs.astropy.org/en/stable/table/>`_
for more details on using Astropy tables (sorting, modifying, etc).
