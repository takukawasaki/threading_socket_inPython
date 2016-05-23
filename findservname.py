#!/usr/local/bin/python3

import socket

def find_serv_name():
    protocolname = 'tcp'
    print('\n')
    for port in [80,8000,8080,25,22,21,20,7]:
        print ("Port: {!s} => service.name {!s}".format(
                port, socket.getservbyport(port,protocolname)))
    print ("Port: {!s} => service.name {!s}".format( 
        53, socket.getservbyport(53, 'udp')))

if __name__ == '__main__':
    find_serv_name()                                                
