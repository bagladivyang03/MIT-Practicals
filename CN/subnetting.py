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
    
    
    
# OUTPUT :-
# Enter the ip :192.168.1.1
# The class of 192.168.1.1 ip Address is C
# Enter the no. of hosts required :12

# The subnet mask is 255.255.255.240
# subnets :
# 192.168.1.0-192.168.1.15
# 192.168.1.16-192.168.1.31
# 192.168.1.32-192.168.1.47
# 192.168.1.48-192.168.1.63
# 192.168.1.64-192.168.1.79
# 192.168.1.80-192.168.1.95
# 192.168.1.96-192.168.1.111
# 192.168.1.112-192.168.1.127
# 192.168.1.128-192.168.1.143
# 192.168.1.144-192.168.1.159
# 192.168.1.160-192.168.1.175
# 192.168.1.176-192.168.1.191
# 192.168.1.192-192.168.1.207
# 192.168.1.208-192.168.1.223
# 192.168.1.224-192.168.1.239
# 192.168.1.240-192.168.1.255

    


