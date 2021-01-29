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