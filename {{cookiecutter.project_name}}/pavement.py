# -*- coding: utf-8 -*-

import os
import sys


DISABLED_LIBS = []


def init(env):
    # Initialize the paver environment
    pass


def find_version(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as init:
        for line in init:
            if line.startswith('__version__'):
                x, version = line.split('=', 1)
                return version.strip().strip('\'"')
        else:
            raise ValueError('Cannot find the version in {0}'.format(filename))


def parse_requirements(requirements_txt):
    requirements = []
    try:
        with open(requirements_txt, 'r') as f:
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
    import setuptools
    from paver.setuputils import setup
    readme_md = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme_md, 'r') as readme_file:
        readme = readme_file.read()

    setup(
        name='{{ cookiecutter.repo_name }}',
        version='{{ cookiecutter.version }}',
        version=find_version('{{cookiecutter.repo_name}}/__init__.py'),
        description='{{ cookiecutter.project_short_description }}',
        long_description=readme,
        author='{{ cookiecutter.full_name }}',
        author_email='{{ cookiecutter.email }}',
        packages=[
            packages=setuptools.find_packages(
                include=[
                    '{{ cookiecutter.repo_name }}',
                    '{{ cookiecutter.repo_name }}.*',
                ],
            ),
        ],
        include_package_data=True,
        install_requires=[
        ],
        zip_safe=False,
)


try:
    import sett
    with open(ROOT.joinpath('localpavement.py'), 'r') as localpavement:
        exec(localpavement.read(), locals(), globals())
except (OSError, ImportError) as e:
    pass
