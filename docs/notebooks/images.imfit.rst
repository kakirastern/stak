
images.imfit
============

 ## Some Notes



 ## General Imports

.. code:: python

    import numpy as np
    from astropy.modeling import models, fitting

 ### fit1d

The fit1d task allows you to fit a function to image lines. The function
options available are legendre, chebyshev, spline1 and spline3.

**Should we write a function for this, do people use it?**

-  leg - astropy.modeling.polynomial.Legendre1D (or 2D)
-  cheb - astropy.modeling.polynomial.Chebyshev1D (or 2D)
-  spline1 - scipy.interpolate.UnivariantSpline
-  spline3 - scipy.interpolate.CubicSpline

