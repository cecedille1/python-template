#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


from setuptools import setup

readme = open('README.rst').read()


def find_version(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath) as init:
        for line in init:
            if line.startswith('__version__'):
                x, version = line.split('=', 1)
                return version.strip().strip('\'"')
        else:
            raise ValueError('Cannot find the version in {0}'.format(filename))


setup(
    name='{{ cookiecutter.repo_name }}',
    version=find_version('{{ cookiecutter.repo_name }}/__init__.py'),
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
