#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import glob
import os
import sys

from setuptools import setup, find_packages

PACKAGENAME = 'stak'
DESCRIPTION = 'STAK (the STScI Analysis Toolkit) is a general purpose library \
        to provide computational resources for astronomical data reduction  \
        and analysis.'
AUTHOR = 'Sara Ogaz, Justin Ely'
AUTHOR_EMAIL = 'ogaz@stsci.edu'
LICENSE = 'BSD'
URL = 'http://github.com/spacetelescope/stak'

VERSION = '0.1.0'

# Indicates if this version is a release version
RELEASE = 'dev' not in VERSION

with open(os.path.join(PACKAGENAME, 'version.py'), 'w+') as fp:
    fp.write('__all__ = [\'__version__\', \'RELEASE\']\n')
    fp.write('__version__ = \'{0}\'\nRELEASE = {1}\n'.format(VERSION, RELEASE))

entry_points = {'console_scripts': ['hselect = stak.hselect:main']}

setup(name=PACKAGENAME,
      version=VERSION,
      description=DESCRIPTION,
      install_requires=[
          'astropy',
          'six',
          'numpy',
          'stsci.tools',
          'pyparsing'
          ],
      packages=find_packages(),
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      url=URL,
      entry_points=entry_points,


)