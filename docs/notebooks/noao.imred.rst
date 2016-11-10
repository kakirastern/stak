
noao.imred
==========

Notes
-----

blah blah cats blah blah

Contents:

-  `crutil.crgrow <#crgrow>`__



crutil.crgrow
-------------

**Please review the `Notes <#notes>`__ section above before running any
examples in this notebook**

The crgrow replacement uses the ``skimage.morphology`` package to grow
the values in any numpy array. The dilation task is a wrapper around
``scipy.ndimage.grey_dilation``. You can insert any kernal type where
``disk`` is called in this example.

.. code:: python

    from astropy.io import fits
    from skimage.morphology import disk,dilation

.. code:: python

    # Change this value to your desired data file
    test_data = '/eng/ssb/iraf_transition/test_data/id0k16pdq_blv_tmp.fits'
    
    # Read in your fits file, when using a fits file, the bytesway call is required to
    # make sure your arry data type is correct.
    hdu = fits.open(test_data,mode='update')
    dq1 = hdu[3].data.byteswap().newbyteorder('=')
    
    # Dilation used to grow the CR flags
    grownDQ = dilation(dq1, disk(2))
    
    # Re-assign the changed array to our original fits file and close the file to save.
    hdu[3].data = grownDQ
    hdu.close()



crutil.crmedian
---------------

.. code:: python

    # use ccdproc ccdproc.cosmicray_median (they also have an la cosmic)
