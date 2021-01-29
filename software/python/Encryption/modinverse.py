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