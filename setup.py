#!/usr/bin/env python
# -*- coding: utf-8 -*-


import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

NAME = 'wikio'
DESCRIPTION = 'The program allows users to use Wikipedia through terminal screen using MediaWiki action API.'
URL = ''
EMAIL = 'tranghoangphongvu@gmail.com'
AUTHOR = 'Vu TRANG'

REQUIRED = []

here = os.path.abspath(os.path.dirname(__file__))

setup (
    name=NAME,
    version=1,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    include_package_data=True,
    entry_points = {
        'console_scripts': ['wikio = wikio.main:run'],
    },
)
