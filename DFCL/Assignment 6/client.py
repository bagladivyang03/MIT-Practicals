import socket
from PIL import Image
from hashlib import sha384
from imagehash import hash_file

host = '127.0.0.1'
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))



print("Receiving Data..\n")
with open('test1.png', 'wb') as f:
        print('file opened')
        data = s.recv(416545)  #size of the image which is received from server
        f.write(data)
        print(data)
        f.close()
main_hash = hash_file('modified.png')
computed_hash = hash_file('test1.png')
print(main_hash, computed_hash)
if(main_hash == computed_hash):
        print("No Tampering")
else:
        print("Tampering occured!")
with open('test1.png', 'rb') as f:
        im = Image.open(f)
        im.show()

print('Transfer Completed!!!')
s.close()


