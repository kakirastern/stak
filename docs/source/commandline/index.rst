======================
Command Line Utilities
======================

STAK includes some command line versions of common tasks.  This is a
work-in-progress and more functions will be added in the future.


Hselect
=======

Hselect is a Python replacement for the IRAF Hselect task, which searches FITS
headers for requested keywords and prints the results. For more information on
the Python usage of this task please see the
:doc:`Hselect tutorial page <../walkthrough/walk_hselect>`.


Positional Arguments
--------------------

Hselect takes two types of positional arguments.

 - filename(s)
    The FITS file headers that hselect will search. This argument can be
    multiple white-space separated filenames.
    Wildcard characters and IRAF filename syntax is accepted.

 - keyword(s)
    The keyword(s) to include in the output table. This argument can be
    multiple comma separated (no white-space)
    keyword names.  The ``*`` wildcard is also accepted.

Keyword Arguments
-----------------

Hselect takes two types of keyword arguments.

 - -e/--ext
    The extension keyword is used to define specific FITS extensions to be
    used. This argument should be comma separated integers (no white-space).
    Default is set to all extensions in the file.

 - -x/--expression
    The expression keyword is used to apply an assertion expression on the
    output table.  The expression can be defined using ``=,>,<,>=,<=``
    operators in a "keyword operator value" combination.  These inner
    expressions can then be combined using AND/OR (case insensitive).
    Enclose your full expression in quotes, and any string values in the
    alternate quote style ``'`` or ``"``. If necessary, use parenthesis to
    notate order of evaluation.  See below for examples.

Examples
--------

Below are several examples showing the usage of different parameters.
A very simple call to return the value for the keyword BUNIT within all
extensions of the file iczgs3y5q_flt.fits, would look like this::

    $ hselect iczgs3y5q_flt.fits BUNIT

         Filename      Ext    BUNIT
    ------------------ --- -----------
    iczgs3y5q_flt.fits   1 ELECTRONS/S
    iczgs3y5q_flt.fits   2 ELECTRONS/S
    iczgs3y5q_flt.fits   3    UNITLESS
    iczgs3y5q_flt.fits   4     SAMPLES
    iczgs3y5q_flt.fits   5     SECONDS

To run multiple files you can either use a wildcard::

    $ hselect hselect *.fits BUNIT,TIME-OBS

Or enter multiple filenames separated by white-space::

    $ hselect file1.fits file2.fits BUNIT,FILT*,DATE-OBS

To check only certain extensions (0,1,2 in this example) use the following
syntax, integers separated by commas, with no white-space::

    $ hselect file1.fits BUNIT -e 0,1,2 

To add an expression evaluation use the following syntax::

    $ hselect file1.fits file2.fits BUNIT,NAXIS1 --expression 'BUNIT="SECONDS"'

    $ hselect file1.fits NAXIS1 -e 1,2 -x 'NAXIS1=1014 AND BUNIT="SECONDS"'
