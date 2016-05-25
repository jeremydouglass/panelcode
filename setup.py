# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='panelcode',
    version='0.0.1',
    description='a lightweight layout description language for panels and grids',
    long_description=readme,
    author='Jeremy Douglass',
    author_email='jeremydouglass@gmail.com',
    url='https://jeremydouglass.com/panelcode',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

