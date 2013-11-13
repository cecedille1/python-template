#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()

setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    packages=[
        '{{ cookiecutter.repo_name }}',
    ],
    package_dir={
        '{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'
    },
    include_package_data=True,
    install_requires=[
    ],
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
    ],
    test_suite='tests',
)
