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


receivedMsg = c.recv(1024)
authMsg = receivedMsg.decode()


# send password to the client after
# encoding into binary string
message = input('Enter the message to be encoded: ')
encodedMsg = hashlib.sha1(message.encode())

if encodedMsg.hexdigest()==authMsg:
    c.send(b"Authentication Succesfull !!")
else:
    c.send(b"Authentication Failed :(")


c.close()


'''
$ python sha-server.py
socket succesfully created
Socket binded to 6180
Socket is listening
Got connection from  ('127.0.0.1', 60659)
Enter the message to be encoded: mitwpu


$ python sha-server.py
socket succesfully created
Socket binded to 6180
Socket is listening
Got connection from  ('127.0.0.1', 60687)
Enter the message to be encoded: mitWpu

'''

