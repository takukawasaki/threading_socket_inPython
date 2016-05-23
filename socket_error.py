#!/usr/local/bin/python3


import socket
import sys


def modify_buff_size(a,b):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    # Get the size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print ("Buffer size [Before]:%d" %bufsize)
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(\
        socket.SOL_SOCKET,\
        socket.SO_SNDBUF,\
        a)
    sock.setsockopt(\
        socket.SOL_SOCKET,\
        socket.SO_RCVBUF,\
        b)\

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print ("Buffer size [After]:{:d}".format(bufsize))
if __name__ == '__main__':
    send = int(sys.argv[1])
    recv = int(sys.argv[2])
    modify_buff_size(send,recv)        
