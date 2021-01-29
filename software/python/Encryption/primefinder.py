import keyboard
import msvcrt
import sys
def primechecker(number) :
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
            factor2 = number/3
        elif number % 2 == 0:
            factor1 = 2
            factor2 = number/2

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
            factor2 = number/i
            ifprimelist.clear()
            ifprimelist.append(False)
            ifprimelist.append(factor1)
            ifprimelist.append(factor2)
            return ifprimelist #it is not prime
        i += 6 #add 6 to the number each time
    ifprimelist.clear()
    ifprimelist.append(True)
    return ifprimelist #otherwise, there are no factors, so it is a prime number

primelist = []
mynumbers = []
start = int(input('Start at: '))
while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        if ord(key_stroke) == 27:
            print('Escaping...')
            sys.exit()
        elif ord(key_stroke) == 32:
            if len(mynumbers) < 2:
                mynumbers.append(primelist[-1])
            if len(mynumbers) == 2:
                break


    ifprimelist = primechecker(start)
    isprime = ifprimelist[0]
    if isprime:
        print('prime number:', start)
        primelist.append(start)

    start +=1
print('\n\nYour chosen numbers are: \np =', mynumbers[0], '\nq =', mynumbers[1])
print('\nHere is your public key:', mynumbers[0] * mynumbers[1])

f = open("key.txt", "w")
f.write(f"Public key: N = {mynumbers[0] * mynumbers[1]} and e = 187 \nPrivate Key: p = {mynumbers[0]} and q = {mynumbers[1]}")
f.close()

#open and read the file after the appending:
f = open("key.txt", "r")
print(f.read())