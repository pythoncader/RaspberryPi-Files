import pyperclip
import math
import sys

def stringtoint(mystring):
    #this converts the string to ascii integers and returns it as a list
    return [ord(character) for character in mystring]

def inttostring(mylistofints): 
    #this takes a list of ascii integers and converts it to a string
    mylistofcharacters = []
    for integer in mylistofints:
        mylistofcharacters.append(chr(integer))
    mystring = "".join(mylistofcharacters)
    return mystring

def modinv(e, phi):
    for i in range(1, phi):
        if (e * i) % phi == 1: 
            #example: if e = 7 and phi = 160, then it loops through until it finds the number
            #(in this case 23) that satisfies this equation: 7*23=161 divided by 160 is 1 remainder 1
            return i
    return None

encodeordecodeinput = str(input("\n\nEncode or Decode?\n"))
encodeordecodeinput = encodeordecodeinput.lower()
if "e" == encodeordecodeinput[0]:

    intcipherlist = stringtoint(str(input("\nPlease write your message: \n")))

    mystringlist = []
    for i in intcipherlist:
        stringer = str(i)
        mystringlist.append(stringer)
    myintstring = ", ".join(mystringlist)
    print("Your message as ASCII:", myintstring)
    N = int(input("Please give the value of N:\n"))
    e = int(input("Please give the value of e:\n"))
    mycodedlist = []
    for i in intcipherlist:
        codedintcharacter = (i**e) % N #Encoding formula is C = M^e mod N
        mycodedlist.append(codedintcharacter)

    print(inttostring(mycodedlist))
    yesorno = str(input('\nCopy to clipboard? y/n  '))
    if yesorno == 'y':
        for i in range(len(mycodedlist)):
            mycodedlist[i] = str(mycodedlist[i])
        mycodedlist = ", ".join(mycodedlist)
        pyperclip.copy(mycodedlist)
        print('The ciphertext has been copied to the clipboard')

else:
    C = str(input("Please write the ciphertext: \n"))
    p = int(input("Please write your value of p: \n"))
    q = int(input("Please write your value of q: \n"))
    e = int(input("Please write your value of e: \n"))

    N = p*q
    print(f"Calculating N... {N}")

    stringcipherlist = C.split(', ') #split the string of integers by the comma and space to give a list
    print(f"Splitting string into a list...{stringcipherlist}")

    intcipherlist = []
    for i in stringcipherlist: #convert each number in the list to an integer
        intcipherlist.append(int(i))
    print(f"Converting ciphertext to integers...{intcipherlist}")

    phi = (p-1)*(q-1)
    print(f"Calculating phi...{phi}")

    mygcd = math.gcd(e, phi)
    print(f"This should be one: {mygcd}")
    if mygcd != 1:
        sys.exit("Invalid value of e (Make sure that it is coprime to phi)")

    d = modinv(e, phi)
    print(f"Calculating d...{d}")

    for i in range(len(intcipherlist)):
        intcipherlist[i] = (intcipherlist[i] ** d) % N
    print(f"Decoding message...{intcipherlist}")

    decodedmessage = inttostring(intcipherlist)
    print(f"Converting decoded message to characters...{decodedmessage}")

    print(f"Here is your message: {decodedmessage}")


    yesorno = str(input('\nCopy to clipboard?\n'))
    if 'y' in yesorno or "s" in yesorno:
        pyperclip.copy(decodedmessage)
        print('The ciphertext has been copied to the clipboard')