
images.imfit
============

Notes
-----

Contents:

-  `fit1d <#fit1d>`__



fit1d
~~~~~

.. code:: python

    # Standard Imports
    import numpy as np
    
    # Astronomy Specific Imports
    from astropy.io import fits
    from astropy.modeling import models, fitting

\*\* Please review the `Notes <#notes>`__ section above before running
any examples in this notebook \*\*

The fit1d task allows you to fit a function to image lines. The function
options available are legendre, chebyshev, spline1 and spline3.

**Should we write a function for this, do people use it?**

-  leg - astropy.modeling.polynomial.Legendre1D (or 2D)
-  cheb - astropy.modeling.polynomial.Chebyshev1D (or 2D)
-  spline1 - scipy.interpolate.UnivariantSpline
-  spline3 - scipy.interpolate.CubicSpline
