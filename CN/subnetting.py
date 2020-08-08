#Write a python program to implement subnetting to find subnet mask and also find the range of address.

import re

mask = {
    'A': ['255.', 24],
    'B': ['255.255.', 16],
    'C': ['255.255.255.', 8]
}

def convertToDecimal(binary):
    decimal = []
    for i in range(0, len(binary), 8):
        decimal.append(str(int(binary[i:i + 8], 2)))
    return '.'.join(decimal)

ip = list(map(int , input("Enter the ip :").split('.')))

taken_for_subnet = ''
ip_class =''

if(ip[0] <=126):
    ip_class = 'A'
    taken_for_subnet = '.'.join(map(str,ip[:1])) + '.'
elif(128<= ip[0] <192):
    ip_class = 'B'
    taken_for_subnet = '.'.join(map(str,ip[:2])) + '.'
elif(192<= ip[0] <224):
    ip_class = 'C'
    taken_for_subnet = '.'.join(map(str,ip[:3])) + '.'
else:
    print('Specified IP address does not fall under class A, B or C !')
    exit(0)

    
print('The class of ' + '.'.join(map(str,ip)) + ' ip Address is ' + ip_class)

hosts = int(input("Enter the no. of hosts required :")) + 2

pow2 = 1  
while True:
    result = 2 ** pow2
    if (hosts <= result):
        break
    pow2 += 1
    
masks = ('0' * pow2).rjust(mask[ip_class][1], '1')          # Adjusts the given string to the right and fill with extra '1's on the left

n = 2 ** (mask[ip_class][1] - pow2)  # number of ip addresses in each subnet

subnets = []
for k in range(n):
    start = re.sub('1+' , str(bin(k)[2:]) , masks).rjust(mask[ip_class][1] , '0')
    end = start[:-pow2] + '1'*pow2
    subnets.append([start,end])

# print(subnets)
print('\nThe subnet mask is ' + mask[ip_class][0] + convertToDecimal(masks))

print('subnets :')
for i in subnets:
    print(taken_for_subnet + convertToDecimal(i[0]) + '-' + taken_for_subnet + convertToDecimal(i[1]))
    
    

    
#OUTPUT :
# Enter the ip :192.12.12.1
# The class of 192.12.12.1 ip Address is C
# Enter the no. of hosts required :12
# [['00000000', '00001111'], ['00010000', '00011111'], ['00100000', '00101111'], ['00110000', '00111111'], ['01000000', '01001111'], ['01010000', '01011111'], ['01100000', '01101111'], ['01110000', '01111111'], ['10000000', '10001111'], ['10010000', '10011111'], ['10100000', '10101111'], ['10110000', '10111111'], ['11000000', '11001111'], ['11010000', '11011111'], ['11100000', '11101111'], ['11110000', '11111111']]

# The subnet mask is 255.255.255.240
# subnets :
# 192.12.12.0-192.12.12.15
# 192.12.12.16-192.12.12.31
# 192.12.12.32-192.12.12.47
# 192.12.12.48-192.12.12.63
# 192.12.12.64-192.12.12.79
# 192.12.12.80-192.12.12.95
# 192.12.12.96-192.12.12.111
# 192.12.12.112-192.12.12.127
# 192.12.12.128-192.12.12.143
# 192.12.12.144-192.12.12.159
# 192.12.12.160-192.12.12.175
# 192.12.12.176-192.12.12.191
# 192.12.12.192-192.12.12.207
# 192.12.12.208-192.12.12.223
# 192.12.12.224-192.12.12.239
# 192.12.12.240-192.12.12.255


