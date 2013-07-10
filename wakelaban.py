#!/usr/bin/env python
#00-50-8D-B5-EA-4B

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto('\xff'*6 + '\x00\x50\x8D\xB5\xEA\x4B'*16, ('192.168.5.255', 80))
print "Magic Packet sent! Is it alive?";
