
tables.fitsio
=============

Notes
-----

blah blah cats blah

Contents:

-  `catfits <#catfits>`__



catfits
-------

\*\* Please review the `Notes <#notes>`__ section above before running
any examples in this notebook \*\*

.. code:: python

    from astropy.io import fits
    import glob

.. code:: python

    # Change these values to your desired data files, glob will capture all wildcard matches
    test_data = glob.glob('/eng/ssb/iraf_transition/test_data/*.fits')
    
    for filename in test_data:
        fits.info(filename)


.. parsed-literal::

    Filename: /eng/ssb/iraf_transition/test_data/iczgs3ygq_flt.fits
    No.    Name         Type      Cards   Dimensions   Format
    0    PRIMARY     PrimaryHDU     266   ()              
    1    SCI         ImageHDU       140   (1014, 1014)   float32   
    2    ERR         ImageHDU        51   (1014, 1014)   float32   
    3    DQ          ImageHDU        43   (1014, 1014)   int16   
    4    SAMP        ImageHDU        37   (1014, 1014)   int16   
    5    TIME        ImageHDU        37   (1014, 1014)   float32   
    6    WCSCORR     BinTableHDU     59   7R x 24C     [40A, I, A, 24A, 24A, 24A, 24A, D, D, D, D, D, D, D, D, 24A, 24A, D, D, D, D, J, 40A, 128A]   
    Filename: /eng/ssb/iraf_transition/test_data/iczgs3ygq_newdtype_flt.fits
    No.    Name         Type      Cards   Dimensions   Format
    0    PRIMARY     PrimaryHDU     266   ()              
    1    SCI         ImageHDU       140   (1014, 1014)   int32   
    2    ERR         ImageHDU        51   (1014, 1014)   float32   
    3    DQ          ImageHDU        43   (1014, 1014)   int16   
    4    SAMP        ImageHDU        37   (1014, 1014)   int16   
    5    TIME        ImageHDU        37   (1014, 1014)   float32   
    6    WCSCORR     BinTableHDU     59   7R x 24C     [40A, I, A, 24A, 24A, 24A, 24A, D, D, D, D, D, D, D, D, 24A, 24A, D, D, D, D, J, 40A, 128A]   
    Filename: /eng/ssb/iraf_transition/test_data/iczgs3y5q_flt.fits
    No.    Name         Type      Cards   Dimensions   Format
    0    PRIMARY     PrimaryHDU     265   ()              
    1    SCI         ImageHDU       140   (1014, 1014)   float32   
    2    ERR         ImageHDU        51   (1014, 1014)   float32   
    3    DQ          ImageHDU        43   (1014, 1014)   int16   
    4    SAMP        ImageHDU        37   (1014, 1014)   int16   
    5    TIME        ImageHDU        37   (1014, 1014)   float32   
    6    WCSCORR     BinTableHDU     59   7R x 24C     [40A, I, A, 24A, 24A, 24A, 24A, D, D, D, D, D, D, D, D, 24A, 24A, D, D, D, D, J, 40A, 128A]   
    Filename: /eng/ssb/iraf_transition/test_data/imarith_out.fits
    No.    Name         Type      Cards   Dimensions   Format
    0    PRIMARY     PrimaryHDU     266   ()              
    1    SCI         ImageHDU       140   (1014, 1014)   float32   
    2    ERR         ImageHDU        51   (1014, 1014)   float32   
    3    DQ          ImageHDU        43   (1014, 1014)   int16   
    4    SAMP        ImageHDU        37   (1014, 1014)   int16   
    5    TIME        ImageHDU        37   (1014, 1014)   float32   
    6    WCSCORR     BinTableHDU     59   7R x 24C     [40A, I, A, 24A, 24A, 24A, 24A, D, D, D, D, D, D, D, D, 24A, 24A, D, D, D, D, J, 40A, 128A]   
    Filename: /eng/ssb/iraf_transition/test_data/imfunction_out.fits
    No.    Name         Type      Cards   Dimensions   Format
    0    PRIMARY     PrimaryHDU     266   ()              
    1    SCI         ImageHDU       140   (1014, 1014)   float64   
    2    ERR         ImageHDU        51   (1014, 1014)   float32   
    3    DQ          ImageHDU        43   (1014, 1014)   int16   
    4    SAMP        ImageHDU        37   (1014, 1014)   int16   
    5    TIME        ImageHDU        37   (1014, 1014)   float32   
    6    WCSCORR     BinTableHDU     59   7R x 24C     [40A, I, A, 24A, 24A, 24A, 24A, D, D, D, D, D, D, D, D, 24A, 24A, D, D, D, D, J, 40A, 128A]   
    Filename: /eng/ssb/iraf_transition/test_data/imcopy_out.fits
    No.    Name         Type      Cards   Dimensions   Format
    0    PRIMARY     PrimaryHDU     266   ()              
    1    SCI         ImageHDU       140   (1014, 1014)   float32   
    2    ERR         ImageHDU        51   (1014, 1014)   float32   
    3    DQ          ImageHDU        43   (1014, 1014)   int16   
    4    SAMP        ImageHDU        37   (1014, 1014)   int16   
    5    TIME        ImageHDU        37   (1014, 1014)   float32   
    6    WCSCORR     BinTableHDU     59   7R x 24C     [40A, I, A, 24A, 24A, 24A, 24A, D, D, D, D, D, D, D, D, 24A, 24A, D, D, D, D, J, 40A, 128A]   
    Filename: /eng/ssb/iraf_transition/test_data/imfunction2_out.fits
    No.    Name         Type      Cards   Dimensions   Format
    0    PRIMARY     PrimaryHDU     266   ()              
    1    SCI         ImageHDU       140   (1014, 1014)   float64   
    2    ERR         ImageHDU        51   (1014, 1014)   float32   
    3    DQ          ImageHDU        43   (1014, 1014)   int16   
    4    SAMP        ImageHDU        37   (1014, 1014)   int16   
    5    TIME        ImageHDU        37   (1014, 1014)   float32   
    6    WCSCORR     BinTableHDU     59   7R x 24C     [40A, I, A, 24A, 24A, 24A, 24A, D, D, D, D, D, D, D, D, 24A, 24A, D, D, D, D, J, 40A, 128A]   


