#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    setup_requires=['d2to1>=0.2.7', 'stsci.distutils>=0.3'],
    namespace_packages=['stsci'], packages=['stsci'],
    d2to1=True,
    use_2to3=True,
    zip_safe=False
)
