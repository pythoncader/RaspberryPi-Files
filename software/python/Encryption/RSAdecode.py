import sys
from prime import isprime
from modinverse import inverse
from gcdcomputer import computeGCD

p = int(input('Please enter your value for p: '))

ifprime = isprime(p)
if ifprime[0] == False:
    print("The number is not prime:\nThe factors found for the number are:", ifprime[1], 'and', ifprime[2])
    sys.exit('The value is not valid')
elif ifprime[0] == True:
    pass
    #print('The number is prime')

q = int(input('Please enter your value for q: '))

ifprime = isprime(p)
if ifprime[0] == False:
    print("The number is not prime:\nThe factors found for the number are:", ifprime[1], 'and', ifprime[2])
    sys.exit('The value is not valid')
elif ifprime[0] == True:
    pass
    #print('The number is prime')

N = p*q

phi = (p-1) * (q-1)
e = int(input('Please enter your value for e: (less than and coprime to '+ str(phi)+'): '))
print('\nYour public values are: \nN =', N, '\ne =', e)

print('What is the message you want to decode?')
ciphertext = str(input())
cipherlist = ciphertext.split(', ')


#find GCD of e and phi

gcd = computeGCD(e, phi)
#print ("The gcd of e and phi is : ",end="") 
#print(gcd) 
if gcd == 1:
    pass
    #print("You're good to go!")
else:
    sys.exit('Your value for e is not valid')

d = inverse(e, phi)
#print('d =', d)
myasciilist = []
for i in cipherlist:
    C = int(i)
    Ctothed = C ** d
    M = Ctothed % N
    myasciilist.append(M)
decodedmessage = ''
for i in myasciilist:
    decodedmessage += chr(i)
print('Here is your message:', decodedmessage)