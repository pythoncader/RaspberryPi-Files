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
