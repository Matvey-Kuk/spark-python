#!/usr/bin/env python

from distutils.core import setup

setup(
    name='cspark-python',
    version='0.0.1',
    description='Python library for Cisco Spark',
    author='Matvei Kukui',
    author_email='motakuk@gmail.com',
    url='https://github.com/Matvey-Kuk/cspark-python',
    packages=['cspark-python'],
    install_requires=[
        'requests==2.12.5',
        'peewee==2.8.5'
    ],
)
