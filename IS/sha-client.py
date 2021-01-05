from socket import socket
import sys

import hashlib

# Created a socket object 
s = socket()

print("socket succesfully created")

#connection of the client to the server
port = 6180
s.connect(('127.0.0.1',port))

pas = input("Enter the password : ")
encodedpas = hashlib.sha1(pas.encode())
s.send(encodedpas.hexdigest().encode())

msg = s.recv(1024)

print(msg.decode())

s.close()

'''
$ python sha-client.py
socket succesfully created
Enter the password : mitwpu
Authentication Succesfull !!



$ python sha-client.py
socket succesfully created
Enter the password : mitwpu
Authentication Failed :(
'''