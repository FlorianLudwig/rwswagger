#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'rueckenwind'
]

setup_requirements = [
]

test_requirements = [
    'pytest',
]

setup(
    name='rwswagger',
    version='0.0.3',
    description="Generate swagger file from within rueckenwind",
    long_description=readme,
    author="Florian Ludwig",
    author_email='f.ludwig@greyrook.com',
    url='https://github.com/FlorianLudwig/rwswagger',
    packages=find_packages(include=['rwswagger']),
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='rwswagger',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
