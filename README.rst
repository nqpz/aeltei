======
aeltei
======

aeltei is a soundfont explorer.  You can use a keyboard to enter and play
musical notes in a curses interface.  Current limitations include support for
only one channel, no pitch bending, and no support for saving sounds as MIDI
files.


License
=======

aeltei is free software under the terms of the GNU Affero General Public License
version 3 (or any later version). The author of aeltei is Niels G. W. Serup,
reachable at ngws@metanohi.name.


Dependencies
============

aeltei depends on Python 2.7, the ``fluidsynth`` library, the ``mingus`` Python
module, the progam ``sf2text`` from the ``awesfx`` package of programs, and the
availability of a soundfont (free soundfonts come with ``fluidsynth``).


Use
===

Run ``./aeltei --help``.


Nix
===

This repository contains a ``default.nix`` file.  Using `Nix <https://nixos.org/>`_ you can run ``nix-shell`` in this directory and get an environment where aeltei can be run.
