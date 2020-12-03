P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
P4 = (2, 4, 3, 1)

IP = (2, 6, 3, 1, 4, 8, 5, 7)
IPi = (4, 1, 3, 5, 7, 2, 8, 6)

E = (4, 1, 2, 3, 2, 3, 4, 1)

S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
     ]

S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
     ]


def permute(P, key):
    P_key = ""
    for i in P:
        P_key += key[i-1]
    return P_key


def generate_firstkey(left,right):
    left_ans = left[1:]+left[0:1]
    right_ans = right[1:]+right[0:1]
    key_rot = left_ans+right_ans
    return permute(P8,key_rot)


def generate_secondkey(left,right):
    left_ans = left[3:]+left[0:3]
    right_ans = right[3:]+right[0:3]
    key_rot = left_ans+right_ans
    return permute(P8,key_rot)



def Sbox(ip, sbox):
    row = int((ip[0] + ip[3]),2)
    column = int((ip[1] + ip[2]) ,2)
    return bin(sbox[row][column])[2:].zfill(2)

def F(right,key):
    extendedp = permute(E,right)
    extendedxor = bin(int(extendedp,2) ^ int(key,2))[2:].zfill(8)
    left_xor = extendedxor[:4]
    right_xor = extendedxor[4:]
    left_sbox = Sbox(left_xor,S0)
    right_sbox = Sbox(right_xor,S1)
    return permute(P4,left_sbox+right_sbox)

def f(first1,second1,key):
    left = int(first1,2) ^ int(F(second1,key),2)
    return bin(left)[2:].zfill(4),second1



print("Enter the choice below :")
print("1. Encryption ")
print("2. Decryption ")
n=int(input())
if(n==1):
    print("Enter the plain Text ")
    plain_text = input()[:8]
    print("Enter the 10 bit key ")
    key = input()[:10]
    permutated_key = permute(P10,key)
    left_permutatedkey = permutated_key[:5]
    right_permutatedkey = permutated_key[5:]
    k1 = generate_firstkey(left_permutatedkey,right_permutatedkey)
    k2 = generate_secondkey(left_permutatedkey,right_permutatedkey)
    print(k1)
    print(k2)
    permutated_plaintext = permute(IP,plain_text)
    print(permutated_plaintext)
    first_half = permutated_plaintext[:4]
    second_half = permutated_plaintext[4:]
    print(first_half,second_half)
    left,right = f(first_half,second_half,k1)
    print("SW:" + left + right)
    print(left)
    print(right)
    left1 ,right1 = f(right,left,k2)
    print(left1)
    print(right1)
    print(left1+right1)
    print("Cipher Text is " + permute(IPi,left1+right1))

else:
    print("Enter the cipher text :")
    cipher_text = input()[:8]
    print("Enter the 10 bit key : ")
    key = input()[:10]
    permutated_key = permute(P10,key)
    left_permutatedkey = permutated_key[:5]
    right_permutatedkey = permutated_key[5:]
    k1 = generate_firstkey(left_permutatedkey,right_permutatedkey)
    k2 = generate_secondkey(left_permutatedkey,right_permutatedkey)
    permutated_cipher = permute(IP,cipher_text)
    first_half = permutated_cipher[:4]
    second_half = permutated_cipher[4:]
    print(first_half,second_half)
    left,right = f(first_half,second_half,k2)
    print("SW:" + left + right)
    left1 ,right1 = f(right,left,k1)
    print("Plain Text is " + permute(IPi,left1+right1))    


"""
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/T.E.-College-Work/IS$ python3 sdes.py
Enter the choice below :
1. Encryption
2. Decryption
1
Enter the plain Text 
11110011
Enter the 10 bit key 
1010000010
10100100
01000011
10111101
1011 1101
SW:01001101
0100
1101
1000
0100
10000100
Cipher Text is 01000001
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/T.E.-College-Work/IS$ python3 sdes.py
Enter the choice below :
1. Encryption 
2. Decryption 
2
Enter the cipher text :
01000001
Enter the 10 bit key : 
1010000010
1000 0100
SW:11010100
Plain Text is 11110011
dbagla@DESKTOP-EI8DDFC:/mnt/c/users/divyang/Desktop/T.E.-College-Work/IS$ 
"""

