# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bloom_infra/__init__.py
from bloom_infra import __version__ as version

setup(
	name='bloom_infra',
	version=version,
	description='bloomstack infra',
	author='sahil',
	author_email='sahil@bloomstack.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
