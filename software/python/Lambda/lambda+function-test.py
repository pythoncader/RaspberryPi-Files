mylambda = lambda x, y: x + y + 10

print(f"First function: {mylambda(10, 5)}")

def myfunction(lambdafunction, numofargs):
    numofargslist = [numofargs for i in range(numofargs)] #get the value that amount of times
    print(f"List: {numofargslist}")
    #print(f"My function to unpack all return values of a for loop:", end=" ")
    #print(*(arg for arg in numofargslist))
    myvar = [arg for arg in numofargslist]
    return lambdafunction(*myvar)

#or
def mysecondfunction(lambdafunction, numofargs):
    numofargslist = [numofargs for i in range(numofargs)]
    #print(f"List: {numofargslist}")
    #print(f"My function to unpack all return values of a for loop:", end=" ")
    #print(*(arg for arg in numofargslist))
    return lambdafunction(*[arg for arg in numofargslist])

#or in one line of code:
def mythirdfunction(lambdafunction, numofargs):
    #print(f"List: {numofargslist}")
    #print(f"My function to unpack all return values of a for loop:", end=" ")
    #print(*(arg for arg in numofargslist))
    return lambdafunction(*[arg for arg in [numofargs for i in range(numofargs)]])

#https://www.geeksforgeeks.org/args-kwargs-python/

#or give it a default value
from typing import Any, Callable #give the lambda function a qualifier as a Callable function and import the Any value for the function
#the "variable: variabletype = defaultvalue" syntax gives a way to tell us what type of arguments the function needs
#the "-> None:" tells us the return type of the function, in this case not specified.
def myfourthfunction(lambdafunction: Callable = lambda x: x+3, numofargs: int = 1, argslist: list = None) -> Any:
    """
    This is the docstring of the function: It explains what the function does to the user.
    This function prints out the value of a given lambda function for the given number of arguments
    """
    if argslist == None:
        return lambdafunction(*[arg for arg in [numofargs for i in range(numofargs)]])
    else:
        return lambdafunction(*argslist)
    

print(myfourthfunction(lambda x, y, z: (x*y)/z, 3, [15, 7, 4]))