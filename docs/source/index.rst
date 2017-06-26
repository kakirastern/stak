================
The STAK Project
================
**S**\pace **T**\elescope Science Institute **A**\stronomy **K**\it (STAK), a
resource for Python astronomy software and tutorial materials.


STAK Package Documentation
==========================
**STAK Module Tutorials**

.. toctree::
  :maxdepth: 1

  walkthrough/walk_hselect	      

**Command Line Tools**

.. toctree::
  :maxdepth: 1

  commandline/index      


**Modules/Classes**

.. toctree::
  :maxdepth: 1

  stak/index


The STAK Project Goal
=====================
The `Space Telescope Science Data Analysis System (STSDAS)
<http://www.stsci.edu/institute/software_hardware/stsdas>`_ was a software
package for reducing and analyzing astronomical data, layered on top of IRAF.
The Space Telescope Science Institute has begun the effort to transition
critical and requested parts of the STSDAS package, along with other IRAF
libraries, into python.  The STAK package will *not* be a direct copy of the
STSDAS package, but instead will work to use the improved techniques and
algorithms that exists in the astronomy/Python ecosystem, relying heavily
on the use of the Astropy project.  In addition to writing replacement
functionality where needed, we are also providing the community with short
tutorials on how to translate a large portion of IRAF tasks into Python
through the format of Jupyter Notebooks.

**Important Note: The HST and JWST pipelines will NOT be part of this package,
unlike the IRAF STSDAS package.**


STAK Jupyter Notebooks
======================
A main goal of the STAK project is to provide a guide/tutorials for
users moving from IRAF to Python.  We are building `Jupyter notebooks
<http://jupyter-notebook.readthedocs.io/en/latest/>`_ for most IRAF
packages included in the IRAF STScI distribution.  The Jupyter notebook
provides documentation combined with runnable Python code in one interactive
space.

The Jupyter notebooks for the STAK project are stored in a separate repo, with
a separate doc page, which can be found here:
http://stak-notebooks.readthedocs.io/en/latest/

INFO ON JOE'S DOWNLOAD SCRIPT GOES HERE


Getting Help and User Feedback
==============================
You can send us any comments, questions or bug reports on
our `github page <https://github.com/spacetelescope/stak>`_

We would love to hear feedback from the community, included but not limited to:

* Which IRAF tasks do you use the most?
* Which IRAF tasks have you had trouble finding a Python equivalent for?
* What do you feel is missing from the Python ecosystem that might help
  astronomers transition from IRAF to Python?


Contributing
============
STAK encourages outside contributions!  Please visit our github pages for
`stak <https://github.com/spacetelescope/stak>`_ and `stak-notebooks
<https://github.com/spacetelescope/stak-notebooks>`_ to contribute.  If you
need a github contribution primer, `here's one for forking and pushing
<https://help.github.com/articles/fork-a-repo/>`_. For a general git/github
primer there are many resources on the internet, but `this one
<https://guides.github.com/activities/hello-world/>`_ might be a good place to
start.  If you have any questions or would like further guidance on how to
contribute don't hesitate to post an issue on either of our github pages.

