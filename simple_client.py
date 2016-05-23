#!/usr/local/bin/python3

import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host,port)

    print("Connecting to server %s port: %s" % server_address)

    s.connect(server_address)

    #Send Data

    try:
        message = "Test message: this will be echoed"
        print("Sending: %s" % message)
        #message encode data
        mdata = message.encode('utf-8')
        s.sendall(mdata)
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = s.recv(16)
            amount_received += len(data)
            print("Received: %s" % data)

    except socket.errno as e:
        print("Socket error: %s" % e)

    except Exception as e:
        print("Other exception: %s" % e)

    finally:
        print("Closing connection ...")
        s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Socket Server')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)        
