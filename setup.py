#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

long_desc = """
This package contains a Sphinx extension to embed Panopto applets. It defines a directive "panopto".
"""

requires = ["Sphinx>=0.6", "setuptools"]


setup(
    name="sphinxcontrib-panopto",
    version="2.0.1",
    description="Sphinx panopto applet extension",
    author="Solrun Einarsdottir",
    author_email="solrun.einarsdottir@gmail.com",
    maintainer="Benedikt Magnusson",
    maintainer_email="bsm@hi.is",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["sphinxcontrib"],
)
