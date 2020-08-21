NOTE: I started working on a new version of aeltei, but then I dropped it. This
means that the setup.py file does not work right now. To run aeltei, run
aeltei-run and do not use setup.py (ignore the install instructions in this
README). To install aeltei in its current state, copy aeltei-run to a directory
in your PATH.

======
aeltei
======

aeltei is a Python 3.1 virtual multi soundfont instrument environment. It
allows one to a) use a keyboard to enter and play musical notes in a curses
interface, or b) use a graphics tablet or a mouse to play musical notes in a
PyGame interface. These notes can either be played directly or sent to an
aeltei server (with support for more than one client), which another program
can then listen to. Current limitations include support for only one channel,
no pitch bending, and no support for saving sounds as MIDI files.


License
=======

aeltei is free software under the terms of the GNU Affero General Public
License version 3 (or any later version). The author of aeltei is Niels Serup,
contactable at ns@metanohi.name (for now, just use this address for bug
reports). This is version 0.2.0 of the program.


Dependencies
============

aeltei depends on the ``fluidsynth`` library, the ``mingus`` Python module, the
progam ``sf2text`` from the ``awesfx`` package of programs, and the
availability of a soundfont (free soundfonts come with ``fluidsynth``). When
this README was written, a Python 3 version of mingus was available at
http://code.google.com/r/artdent-mingus-python3/

There's currently no stable version.

Old versions can be downloaded from http://metanohi.name/projects/aeltei/ and
then installed from the downloaded file. To install aeltei this way, run::

  $ tar xzf aeltei-*.tar.gz
  $ cd aeltei-*/
  % python3 setup.py install


Installation
============

aeltei uses Git for code management. To get the latest branch, download it from
gitorious.org::

  $ git clone git://gitorious.org/aeltei/aeltei.git


Use
===

Run ``aeltei --help``.

