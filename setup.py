"""
Exercise creator
setup.py - Executable setup

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""


import py2exe
from distutils.core import setup
setup( console=[{"script": "exercise_creator.py"}] )