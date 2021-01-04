from socket import socket
import hashlib

# Created a socket object 
s = socket()

print("socket succesfully created")

port = 6180

# connect server to client
s.bind(("",port))
print(f"Socket binded to {port}")

# maximum 5 connection to the server
s.listen(5)
print("Socket is listening")

# accept the connection from client 
c, addr = s.accept()
print("Got connection from ",addr)

#send the hashed password to the client 
msg = input("Enter the message to be encoded : ")
c.send(b"Password received")

encodedMsg = hashlib.sha1(msg.encode())

# encoding the password using SHA1 and sending 
c.send(encodedMsg.hexdigest().encode())

# closing the connection 
c.close()




'''
OUTPUT:-

$ python sha-server.py
socket succesfully created
Socket binded to 6180
Socket is listening
Got connection from  ('127.0.0.1', 51626)
Enter the message to be encoded : mitwpu



$ python sha-server.py
socket succesfully created
Socket binded to 6180
Socket is listening
Got connection from  ('127.0.0.1', 51640)
Enter the message to be encoded : mit
'''
