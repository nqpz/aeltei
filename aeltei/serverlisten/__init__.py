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
# Abstract filename: aeltei.serverlisten.init

import aeltei.udpconnect as udpconnect

class AelteiServerlistener:
    def __init__(self, ip, port):
        self.ip, self.port = ip, port
        self.sender = udpconnect.UDPReceiver()
        self.receiver = udpconnect.UDPReceiver()

    def listen(self):
        self.sender.start()
        self.sender.sendtoone(b'1')
        self.receiver.start()
        for data, addr in self.receiver.receive():
            print(data, addr)
