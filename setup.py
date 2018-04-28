# -*- coding: utf-8 -*-
"""
Exercise creator
setup.py - Executable setup

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
# %%

#from distutils.core import setup
#import py2exe

#setup(console=['exercise_creator.py'])


import py2exe
from distutils.core import setup
setup( console=[{"script": "exercise_creator.py"}] )