#!/usr/bin/env python

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto('\xff'*6 + '\x00\x23\xEA\xAD\xC3\xEA'*16, ('192.168.5.255', 80))
print "Magic Packet sent to lou - Is it alive?";
