#!/usr/local/bin/python3

import socket
import select
import argparse


HOST = 'localhost'

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'

SERVER_RESPONSE  = b"""HTTP/1.1 200 OK\r\nDate: Mon, 1 Apr 2013 01:01:01 GMT\r\nContent-Type: text/plain\r\nContent-Length: 25\r\n\r\n
Hello from Epoll Server!"""

class EpollServer(object):
  """socket server using epoll"""

  def __init__(self,host=HOST,port=0):
    self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    self.sock.bind((host,port))
    self.sock.listen(1)
    self.sock.setblocking(0)
    self.sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
    print("Started Epoll Server: {!s}.{!s}".format(host,port))
    self.epoll = select.epoll()
    self.epoll.register(self.sock.fileno().select.EPOLLIN)

  def run(self):
    """Execute epoll server operation"""
    try:
      connections = {}
      request = {}
      response = {}

      while True:
        events = self.epoll.poll(1)
        for fileno,event in events:
          if fileno == self.sock.fileno():
            connection,address = self.sock.accept()
            connection.setblocking(0)
            self.epoll.register(connection.fileno(),select.EPOLLIN)
            connections[connection.fileno()] = b''
            response[connection.fileno()] = SERVER_RESPONSE
          elif event and select.EPOLLIN:
            requests[fileno] += connections[fileno].recv(1024)
            if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
              self.epoll.modify(fileno,select.EPOLLOUT)
              print('-'*40 + '\n' + requests[fileno].decode()[:-2])

          elif event and select.EPOLLOUT:
            byteswritten = connections[fileno].send(response[fileno])
            response[fileno] = response[fileno][byteswritten]
            if len(response[fileno]) == 0:
              self.epoll.modify(fileno,0)
              connections[fileno].shutdown(socket.SHUT_RDWR)
          elif event and select.EPOLLHUP:
            self.epoll.unregister(fileno)
            connections[fileno].close()
            del connections[fileno]
    finally:
      self.epoll.unregister(self.sock.fileno())
      self.epoll.close()
      self.sock.close()


if __name__=='__main__':
  parser = argparse.ArgumentParser(description='Simple Socket Server  with Epoll')
  parser.add_argument('--host',action="store",dest="host",required=True)
  parser.add_argument('--port', action="store", dest="port",type =int, required=True)
  given_args = parser.parse_args()
  host = given_args.host
  port = given_args.port
  server = EpollServer(host=host, port=port)
  server.run()    
      
