#!/usr/bin/env python

try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    import sys
    print("Please install setuptools.")
    sys.exit(1)

import versions


classifiers = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development',
    'Topic :: Database',
    'Topic :: Database :: Front-Ends',
    'Topic :: Software Development :: Libraries',
]

setup(
    name='SixIsles',
    version=versions.VERSIONS,
    description='PyMongo Based ActiveRecord Pattern O/R Mapper',
    author='teitei-tk',
    author_email='teitei.tk@gmail.com',
    url='https://github.com/teitei-tk/SixIsles',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=classifiers,
    install_requires=open('requirements.txt').read().splitlines(),
    keywords=['orm', 'ormapper', 'o/r mapper', 'PyMongo', 'MongoDB'],
    download_url='https://github.com/teitei-tk/SixIsles/archive/master.zip'
)
