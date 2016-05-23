#!/usr/local/bin/python3

import sys
import socket
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
    # Create a TCP socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Enable reuse address/port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Starting up echo server  on %s port %s" % server_address)
    s.bind(server_address)
    # Listen to clients, backlog argument specifies the max no.
    s.listen(backlog)
    while True:
        print("Waiting receive from the clients")
        client,address = s.accept()
        data = client.recv(data_payload)
        if data:
            print("data: %s" % data)
            client.send(data)
            print("sent %s bytes back to %s" % (data, address))
        # end connection
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Socket Server ')
    parser.add_argument('--port', action="store", dest="port",type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)


    
