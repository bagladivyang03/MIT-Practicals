from socket import socket
import sys

import hashlib

# Created a socket object 
s = socket()

print("socket succesfully created")

#connection of the client to the server
port = 6180
s.connect(('127.0.0.1',port))

#start receving the msgs and the hashed password 
msg = s.recv(1024)

while msg:
    print("Received : ",msg.decode())
    passwordHash = msg.decode()
    msg = s.recv(1024)

#enter the password for authentication 
authMsg = input("Enter Password : ")
encodedMsg = hashlib.sha1(authMsg.encode())
if passwordHash == encodedMsg.hexdigest():
    print("Authentication Succesfull !!")
else:
    print("Aurhentication failed!")


#close the connection
s.close()



'''
OUTPUT:-

$ python sha-client.py
socket succesfully created
Received :  Password received
Received :  b266d0891d98a1e5910a028b0883da898192c624
Enter Password : mitwpu
Authentication Succesfull !!


$ python sha-client.py
socket succesfully created
Received :  Password received
Received :  5977a55c75bb4612004451a56b0b4c22d9d3311d
Enter Password : Mit
Aurhentication failed!
'''