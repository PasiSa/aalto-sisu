#!/usr/bin/env python3
"""A setuptools based setup module.
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aalto-sisu',
    version='0.1.0',
    description='Aalto-SISU plugin for A+ LMS',
    long_description=long_description,
    keywords='django',
    url='https://github.com/apluslms/aalto-sisu',
    author='Pasi Sarolahti',
    author_email='pasi.sarolahti@iki.fi',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.2',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data = True,

    install_requires=[
        'Django >=1.11.0, <4',
    ],
    dependency_links=[
    ],
)
