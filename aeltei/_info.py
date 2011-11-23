#!/usr/bin/env python3

# aeltei: a virtual multi soundfont instrument environment
# Copyright (C) 2011  Niels Serup

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Maintainer:  Niels Serup <ns@metanohi.name>
# Abstract filename: aeltei.info

class AttributeDict(dict):
    """A dictionary where x.a == x['a']"""
    def __init__(self, *args, **kwds):
        self._to_apply=kwds.get('to_apply')
        self._apply_what=kwds.get('apply_what')
        if args:
            kwds = {}
            nkwds = self._init(args, {})
            for k, v in nkwds.items():
                kwds[k] = v
        dict.__init__(self, **kwds)

    def _init(self, args, kwds):
        nkwds = AttributeDict()
        for i in range(0, len(args), 2):
            k, v = args[i:i + 2]
            rv = None
            if isinstance(v, list):
                v = self._init(v, kwds)
            else:
                if isinstance(v, str):
                    v = v.format(**kwds)
                if self._to_apply and (self._apply_what is None or
                                       type(v) in self._apply_what):
                    rv = self._to_apply(v)
            if not rv: rv = v
            kwds[k] = v
            nkwds[k] = rv
        return nkwds

    __getattr__ = lambda self, k: self.__getitem__(k)
    __setattribute__ = lambda self, k, v: self.__setitem__(k, v) \
        if not k.startswith('_') else None
    __delattr__ = lambda self, k: tryorpass(KeyError, self.__delitem__, k)

    def __setstate__(self, adict):
        for k, v in adict.items():
            self.__setitem__(k, v)

class PeriodTextTuple(tuple):
    """A tuple meant for version numbers"""
    def __init__(self, *args):
        self.text = '.'.join(str(x) for x in self)

    __new__ = lambda self, *xs: tuple.__new__(self, xs)
    __str__ = lambda self: self.text


program = AttributeDict(
    'name',               'aeltei',
    'version',            PeriodTextTuple(0, 2, 0),
    'description',        'a virtual multi soundfont instrument environment',
    'author',             AttributeDict(
        'name',                'Niels Serup',
        'email',              'ns@metanohi.name',
        'name_with_email',    '{name} <{email}>'),
    'url',                'http://metanohi.name/projects/aeltei/',
    'copyright',          'Copyright (C) 2011  Niels Serup',
    'short_license',      AttributeDict(
        'name',               'AGPLv3+',
        'text',               '''\
License AGPLv3+: GNU AGPL version 3 or later <http://gnu.org/licenses/agpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.'''),
    'version_info',       '{name} {version.text}\n{copyright}\n\
{short_license.text}'
    )

