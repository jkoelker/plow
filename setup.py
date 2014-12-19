#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()

requirements = [
    'ryu',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='plow',
    version='0.1.0',
    description='Ryu sFlow to influxdb app',
    long_description=readme,
    author='Jason Kölker',
    author_email='jason@koelker.net',
    url='https://github.com/jkoelker/plow',
    packages=[
        'plow',
    ],
    package_dir={'plow':
                 'plow'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache",
    zip_safe=False,
    keywords='plow',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
