#!/usr/bin/env python

"""
sentry-teamwork
===============

A Sentry plugin to integrate with Teamwork.

License
-------
Copyright 2015 Sentry
"""

from setuptools import setup, find_packages

install_requires = [
]

setup(
    name='sentry-teamwork',
    version='0.1.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='https://github.com/getsentry/sentry-teamwork',
    description='A Sentry plugin that integrates with Teamwork',
    long_description=__doc__,
    license='Apache 2.0',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    entry_points={
        'sentry.plugins': [
            'sentry_teamwork = sentry_teamwork.plugin:TeamworkTaskPlugin'
        ],
        'sentry.apps': [
            'sentry_teamwork = sentry_teamwork'
        ],
    },
    include_package_data=True,
)
