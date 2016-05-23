#!/usr/local/bin/python3


import socket
import sys

def get_remote_ip(remote):
  try:
    print("IP_Address: {!s} => {!s}".format(remote,socket.gethostbyname(remote)))
  except :
    print ("{!s}: {!s}".format(remote, err_msg))

if __name__=="__main__":
  rem = sys.argv[1]
  if rem :
    get_remote_ip(rem)        
  else:
    print("put some address")
