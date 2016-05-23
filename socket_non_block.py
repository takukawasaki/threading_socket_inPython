#!/usr/local/bin/python3
#ソケットノンブロッキング

import sys
import socket

def test_socket_mode(IN,PORT):
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.setblocking(0)
  s.settimeout(0.5)
  s.bind((IN,PORT))
  socket_address = s.getsockname()
  print ("Trivial Server launched on socket: {!s}".format(str(socket_address)))
  while (1):
    s.listen(1)

if __name__ == "__main__":
  host = sys.argv[1]
  port = int(sys.argv[2])
  test_socket_mode(host,port)
