from decimal import Decimal
import math


# function to calculate the prime no
def isprime(n):
    if(n==2):
        return 1
    for i in range(2,int(math.sqrt(n))):
        if(n%i==0):
            return 0
    return 1


# function to calculate the gcd 
def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)


while(True):
    # values of prime nos. should be large
    p = int(input('Enter the value of p = ')) 
    q = int(input('Enter the value of q = ')) 
    # if any one of the no is not prime then enter the nos again 
    if(not(isprime(p)) or not(isprime(q))):
        print("Pls try again !!")
        print("Please ensure that both numbers are prime.")
    else:
        break

# values of text that is to be encrypted
no = int(input('Enter the value of text = ')) 
n = p*q 


phi = (p-1)*(q-1)


#calculation of e
for e in range(2,phi):
    if(gcd(e,phi)==1):
        break


#calcluation of d
for i in range(1,10):
    x = 1 + i*phi
    if(x%e==0):
        d = int(x/e)
        break


ctt = Decimal(0)
ctt = pow(no,e)
ct = ctt%n #calculating the cipher text


dtt = Decimal(0)
dtt = pow(ct,d)
dt = dtt%n

print("n : " + str(n))
print("e : "+ str(e))
print("phi : "+ str(phi))
print("d : "+ str(d))
print("Cipher Text : " + str(ct))
print("Decrypted Text : "+ str(dt))


'''
Divyang@DESKTOP-EI8DDFC MINGW64 /c/users/divyang/Desktop/Trimester 8/IS/LA3 (master)
$ python rsa.py
Enter the value of p = 11
Enter the value of q = 13
Enter the value of text = 45
n : 143
e : 7
phi : 120
d : 103
Cipher Text : 111
Decrypted Text : 45
'''