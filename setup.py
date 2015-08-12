#!/usr/bin/env python3

"""Setup.py for dirbrowser."""

from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="dirbrowser",
    version="1.0b1",
    description="Command line based directory browser",
    long_description=long_description,
    url="https://github.com/campenr/dirbrowser",
    author="Richard Campen",
    author_email="richard@campen.co",
    license="BSD License",

    # TODO add more classifiers (e.g. platform)

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "License :: OSI Approved :: BSD License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords="directory browser interface",
    packages=find_packages(),
    include_package_data=True

    # TODO add entry into scripts folder

)
