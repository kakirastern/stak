======================
Command Line Utilities
======================

STAK includes some command line versions of common tasks.  This is a work in progress and more functions will be added in the future.


Hselect
=======

Hselect is a Python replacement for the IRAF Hselect task, which searches FITS header for requested keywords.  For more information on this task please see the :doc:`Hselect tutorial page <../walkthrough/walk_hselect>` .

To define a subset of extensions by index, use the ``-e`` or ``--EXT`` parameter and provide comma seperated integers.  To define an expression use the ``-x`` or ``--expression`` parameter. Make sure to enclose your expression in quotes, and any string values in the alternate quote style ``'`` or ``"``.  Add parenthesis where needed to denote the order of evaluation.  You can combine expression elements with ``AND`` and ``OR``.

Below are several examples showing the usage of different parameters.  A very simple call to check all extensions of the file iczgs3y5q_flt.fits for the keyword BUNIT would look like::

    $ hselect iczgs3y5q_flt.fits BUNIT

         Filename      Ext    BUNIT
    ------------------ --- -----------
    iczgs3y5q_flt.fits   1 ELECTRONS/S
    iczgs3y5q_flt.fits   2 ELECTRONS/S
    iczgs3y5q_flt.fits   3    UNITLESS
    iczgs3y5q_flt.fits   4     SAMPLES
    iczgs3y5q_flt.fits   5     SECONDS

To run multiple files you can either use a wildcard::

    $ hselect hselect *.fits BUNIT

Or enter multiple filenames seperated by a space::

    $ hselect file1.fits file2.fits BUNIT

To check only certain extensions (0,1,2 in this example) use the following syntax::

    $ hselect file1.fits BUNIT -e 0,1,2 

To add an expression evaluation use the following syntax::

    $ hselect file1.fits file2.fits BUNIT,NAXIS1 --expression 'BUNIT="SECONDS"'

    $ hselect file1.fits NAXIS1 -e 1,2 -x 'NAXIS1=1014 AND BUNIT="SECONDS"'
