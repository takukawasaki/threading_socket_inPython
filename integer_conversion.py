#!/usr/local/bin/python3

import socket
import sys


def convert_integer():
  data = 1234
  # 32-bit
  print("Original: {!s} => Long  host byte order: {!s}, Network byte order: {!s}".format(data, socket.ntohl(data), socket.htonl(data)))
    # 16-bit
  print("Original: {!s} => Short  host byte order: {!s}, Network byte order: {!s}".format(data, socket.ntohs(data), socket.htons(data)))

    
if __name__ == '__main__':
  convert_integer()
