#!/usr/bin/env python
# coding: utf-8

from setuptools import setup


setup(
    name='mspgsql',
    version='1.0.0.dev1',
    description='Python PostgreSQL library for Music-Story dataflows',

    author='Music-Story',
    author_email='webmaster@music-story.com',

    package_dir={'musicstory.pgsql': 'lib'},
    packages=['musicstory.pgsql'],
    install_requires=[
        'python-dotenv>=0.7.1,<0.8',
        'psycopg2>=2.7.0,<3.0',
    ],
)
