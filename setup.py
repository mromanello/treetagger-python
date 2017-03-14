#!/usr/bin/env python

import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

module_name = "treetagger"
if(sys.version_info < (3, 0)):
  module_name = "treetagger_python2"
  
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='treetagger',
      version='1.0.1',
      description='A Python module for interfacing with the Treetagger by Helmut Schmid.',
      long_description=README,
      author='Mirko Otto',
      author_email='dropsy@gmail.com',
      url='https://github.com/miotto/treetagger-python',
      py_modules=[module_name],
      install_requires=['nltk'],
      license='GPL Version 3',
    )



