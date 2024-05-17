# Copyright (C) 2024 Intel Corporation
# Licensed subject to the terms of the separately executed evaluation license agreement between Intel Corporation and you.

from setuptools import setup, find_packages

setup(
    name='openfl-contrib',
    version='1.6',
    author='The OpenFL Contributors',
    description='Repository for academic and research contributions to OpenFL',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=["setuptools"],
    install_requires=[
        'openfl @ git+https://github.com/securefederatedai/openfl.git@develop',
    ],
    python_requires='>=3.8, <3.11'
)