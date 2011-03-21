#!/usr/bin/env python
from distutils.core import setup

readme = open('README.txt').read()

conf = dict(
    name='aeltei',
    version='0.1.0',
    author='Niels Serup',
    author_email='ns@metanohi.org',
    package_dir={'': '.'},
    py_modules=[],
    scripts=['aeltei'],
    url='http://metanohi.org/projects/aeltei/',
    license='COPYING.txt',
    description='',
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: End Users/Desktop',
                 'Intended Audience :: Developers',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Topic :: Utilities',
                 'Environment :: Console',
                 'License :: DFSG approved',
                 'License :: OSI Approved :: GNU Affero General Public License v3',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2'
                 ]
)

try:
    # setup.py register wants unicode data..
    conf['long_description'] = readme.decode('utf-8')
    setup(**conf)
except Exception:
    # ..but setup.py sdist upload wants byte data
    conf['long_description'] = readme
    setup(**conf)