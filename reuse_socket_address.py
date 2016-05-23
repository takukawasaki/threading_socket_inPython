#!/usr/local/bin/python3

import sys
import socket

def reuse_socket_addr(arg1,arg2):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    oldstate =s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)

    print("Old state : %s" % oldstate)

    s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    newstate = s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print("New state : %s" % newstate)

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind( (arg1, arg2) )
    srv.listen(1)

    print("Listening Port : %s" % arg2)

    while True:
        try:
            connection,addr = srv.accept()
            print("Connected by %s:%s"% (addr[0],addr[1]))
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print("%s" % (msg,))


if __name__ == '__main__':
    a1 = sys.argv[1]
    a2 = int(sys.argv[2])
    reuse_socket_addr(a1,a2)                       
