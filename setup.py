#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='pushcrew',
    version='0.0.1dev0',
    description='Python wrapper around the Pushcrew API',
    author='Misa G.',
    author_email='hi@misalabs.com',
    install_requires=[
        "hammock==0.2.4"
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
