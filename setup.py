#!/usr/bin/env python3
# Abstract filename: aeltei.setup

import sys
import os
from distutils.core import setup

os.chdir(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, '.')

from aeltei._info import program as prog

with open('README.txt') as f:
    readme = f.read()

setup(
    packages=['aeltei', 'aeltei.server', 'aeltei.serverlisten'],
    scripts=['scripts/aeltei', 'scripts/aeltei-server',
             'scripts/aeltei-serverlisten'],
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: End Users/Desktop',
                 'Intended Audience :: Developers',
                 'Topic :: Utilities',
                 'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
                 'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
                 'Environment :: Console :: Curses',
                 'Environment :: Other Environment',
                 'Topic :: Software Development :: Libraries :: pygame',
                 'License :: DFSG approved',
                 'License :: OSI Approved :: GNU Affero General Public License v3',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.1'
                 ],
    name=prog.name,
    url=prog.url,
    version=prog.version.text,
    author=prog.author.name,
    author_email=prog.author.email,
    license=prog.short_license.name,
    description=prog.description,
    long_description=readme,
)
