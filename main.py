import socket
import sys

try:
    socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket is created successfully")
except socket.error as err:
    print("socket creation is fail with error {err}")



