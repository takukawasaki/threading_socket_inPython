#!/usr/local/bin/python3

import os
import socket
import threading
import socketserver

HOST = 'localhost'
PORT = 8080
BUF_SIZE = 1024
MSG = "hello"


class Forkedclient():
    def __init__(self,ip,port):
        #create socket
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #connect_to serveer
        self.sock.connect((ip,port))

    def run(self):
        #send the data to the server
        current_process_id = os.getpid()
        print("PID %s sending echo message to the server :'%s' " % \
              (current_process_id,MSG))
        sent_data_length = self.sock.send(MSG.encode())
        print("sent %d characters so far" % sent_data_length)
        #display response serveer
        response = self.sock.recv(BUF_SIZE)
        print("PID %s received %s:" % (current_process_id, response[5:]))
        
    def shutdown(self):
        self.sock.close()

class ForkingserverRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        #send the echo back to the client
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = '%s: %s' % (current_process_id, data)
        print("server sending response [current_proccess_id : data]= [%s]" % response)
        self.request.send(response.encode())
        return

class ForkingServer(socketserver.ForkingMixIn,socketserver.TCPServer):
    #nothing here to heritate from parent
    pass

def main():
    server = ForkingServer((HOST,PORT),ForkingserverRequestHandler)
    ip,port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print("server loop running PID: %s" % os.getpid)

    client1 = Forkedclient(ip,port)
    client1.run()

    client2 = Forkedclient(ip,port)
    client2.run()

    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()

if __name__=='__main__':
    main()    
    
