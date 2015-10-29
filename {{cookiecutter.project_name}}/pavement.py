#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


DISABLED_LIBS = []


def find_pavelib():
    try:
        import sett
    except ImportError:
        import sys  # noqa
        sys.path.append(path(__file__).dirname())
        import sett  # noqa

find_pavelib()

from paver.easy import *
from sett import which, ROOT, DeployContext, defaults
from setuptools import setup



def find_version(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r', encoding='utf-8') as init:
        for line in init:
            if line.startswith('__version__'):
                x, version = line.split('=', 1)
                return version.strip().strip('\'"')
        else:
            raise ValueError('Cannot find the version in {0}'.format(filename))


def parse_requirements(requirements_txt):
    requirements = []
    try:
        with open(requirements_txt, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or not line:
                    continue
                if line.startswith('-'):
                    raise ValueError('Unexpected command {0} in {1}'.format(
                        line,
                        requirements_txt,
                    ))

                requirements.append(line)
        return requirements
    except IOError:
        return []


@task
def setup_options():
    from paver.setuputils import setup
    with open(ROOT.joinpath('README.md'), 'r', encoding='utf-8') as readme_file:
        readme = readme_file.read()

    setup(
        name='{{ cookiecutter.repo_name }}',
        version=find_version('{{ cookiecutter.repo_name }}/__init__.py'),
        description='{{ cookiecutter.project_short_description }}',
        long_description=readme,
        author='{{ cookiecutter.full_name }}',
        author_email='{{ cookiecutter.email }}',
        packages=setuptools.find_packages(
            '{{ cookiecutter.repo_name }}',
        ),
        package_dir={
            '{{ cookiecutter.repo_name }}': '{{ cookiecutter.repo_name }}'
        },
        include_package_data=True,
        install_requires=parse_requirements('requirements.txt'),
        zip_safe=False,
        keywords='{{ cookiecutter.repo_name }}',
        classifiers=[
        ],
        test_suite='tests',
    )
