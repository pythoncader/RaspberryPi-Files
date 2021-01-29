import sys

def isprime(number) :
    ifprimelist = []
    if (number <= 1) : #if the number is negative, zero, or 1, it is not prime
        #print('The number is negative, zero, or one')
        ifprimelist.clear()
        ifprimelist.append(False)
        return ifprimelist

    if (number <= 3) : #if the number is less than or equal to 3, it is prime, since we have already checked whether it is negative, zero or one
        #print('The number is 2 or 3')
        ifprimelist.clear()
        ifprimelist.append(True)
        return ifprimelist

    if (number % 2 == 0 or number % 3 == 0) : #if the number is divisible by 2 or 3, it is not prime
        #print('The number is divisible by 2 or 3')
        if number % 3 == 0:
            factor1 = 3
            factor2 = number//3
        elif number % 2 == 0:
            factor1 = 2
            factor2 = number//2

        ifprimelist.clear()
        ifprimelist.append(False)
        ifprimelist.append(factor1)
        ifprimelist.append(factor2)
        return ifprimelist


    i = 5 #start at 5
    while(i * i <= number) : #while the factors multiplied together are not above the number
        #print('i = ', i)
        if (number % i == 0 or number % (i + 2) == 0) : #if the number is able to be divided evenly by i or i + 2
            factor1 = i
            factor2 = number//i
            ifprimelist.clear()
            ifprimelist.append(False)
            ifprimelist.append(factor1)
            ifprimelist.append(factor2)
            return ifprimelist #it is not prime
        i += 6 #add 6 to the number each time
    ifprimelist.clear()
    ifprimelist.append(True)
    return ifprimelist #otherwise, there are no factors, so it is a prime number


# Python code to demonstrate naive 
# method to compute gcd ( Euclidean algorithm ) 
def computeGCD(x, y): 
    originalx = x
    originaly = y
    while(y): #non-zero values are true
        if x != originalx:
            pass
            #print('the GCD of', originalx, 'and', originaly, 'is the same as the gcd of', x, 'and', y)
        x, y = y, x % y #the remainder of the first number, x divided by the second number, y, becomes the second number, y, and the old second number, y becomes the first number, x. This repeats until y = 0
    return x
    
#the equivalent of this:
'''
while y != 0:
    oldy = y
    y = x % y
    x = oldy
return x
'''

# Iterative Python 3 program to find 
# modular inverse using extended 
# Euclid algorithm 
  
# Returns modulo inverse of e with 
# respect to phi using extended Euclid 
# Algorithm Assumption: e and phi are 
# coprimes, i.e., gcd(e, phi) = 1 
def inverse(e, phi) : 
    m0 = phi 
    y = 0
    x = 1
  
    if (phi == 1) : 
        return 0
  
    while (e > 1) : 
  
        # q is quotient 
        q = e // phi 
  
        t = phi 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        phi = e % phi 
        e = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 
  
  
'''# Driver program to test above function 
a = 3
m = 11
print("Modular multiplicative inverse is", 
    inverse(a, m)) 
  
# This code is contributed by Nikita tiwari. '''

encodeordecode = str(input('Do you want to encode or decode? '))
if 'decode' in encodeordecode:
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
    print('\n\nHere is your message:', decodedmessage)


elif 'encode' in encodeordecode:
    import pyperclip
    N = int(input('Please write the value of N: \n'))
    e = int(input('Please write the value of e:\n'))
    mymessage = str(input('Please write your message: \n'))
    mymessagelist = list(mymessage)
    asciimessagelist = []
    myencodedlist = []
    ciphertextlist = []
    for i in mymessagelist:
        myascii = ord(i)
        asciimessagelist.append(myascii)

    for i in range(0, len(asciimessagelist)):
        M = asciimessagelist[i]
        Mtothee = M ** e
        C = Mtothee % N
        myencodedlist.append(C)
    print(myencodedlist)
    myencodedliststrings = []
    for i in range(0, len(myencodedlist)):
        myencodedliststrings.append(str(myencodedlist[i]))

    ciphertext = ", ".join(myencodedliststrings)
    print(ciphertext)
    yesorno = str(input('\nCopy to clipboard? y/n  '))
    if yesorno == 'y':
        pyperclip.copy(ciphertext)
        print('The ciphertext has been copied to the clipboard')