#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages


setup(
    name='catprep',
    description='A preprocessing library for categorical variables',
    version='0.0.4',
    author='nel215',
    author_email='otomo.yuhei@gmail.com',
    url='https://github.com/nel215/catprep',
    py_modules=['catprep'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
    ],
    keywords=['machine learning', 'preprocessing'],
)
