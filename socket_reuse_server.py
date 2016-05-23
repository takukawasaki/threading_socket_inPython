#!/usr/local/bin/python3

import sys
import socket
import threading
import time



def main(arg1,arg2):

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    oldstate =s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)

    print("Old state : {!s}".format(oldstate))

    s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    newstate = s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print("New state : {!s}".format(newstate))

    print("Listening Port : {!s}".format(arg2))
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind( (arg1, arg2) )
    srv.listen(1)

    while True:
        try:
            connection,addr = srv.accept()
            print("Connected by {!s}:{!s}".format(addr[0],addr[1]))
        except  KeyboardInterrupt:
            break
        except socket.error as msg:
            print("error: {!s}".fromat(msg))
            
        t = threading.Thread(target = threadfunc, args = [connection])
        t.setDaemon(1)
        t.start()

    
def threadfunc(sock):
    print ('{!s} is created!'.format(threading.currentThread().getName()))
    while True:
        rcvmsg = sock.recv(1024)
        time.sleep(1)
        if rcvmsg == '':
            break
        else:
            print ('{!s} received -> {!s}'.format(threading.currentThread().getName(), rcvmsg))
    sock.close()
    print('{!s} is terminated!'.format(threading.currentThread().getName()))
                        

if __name__ == '__main__':
    a1 = sys.argv[1]
    a2 = int(sys.argv[2])
    main(a1,a2)
