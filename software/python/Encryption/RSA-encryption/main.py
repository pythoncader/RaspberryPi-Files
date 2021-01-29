import pyperclip
import math
import sys
import primefinder
from font import textcolors

def closefiles():
    try:
        contactwriter.close()
        #print("contactwriter closed")
    except:
        pass
    try:
        contactreader.close()
        #print("contactreader closed")
    except:
        pass
    try:
        userwriter.close()
        #print("userwriter closed")
    except:
        pass
    try:
        userreader.close()
        #print("userreader closed")
    except:
        pass



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


try:
    encodeordecodeinput = str(input("\n\nEncode, Decode, Print Info or Create New User?\n"))
    encodeordecodeinput = encodeordecodeinput.lower()
    if "e" == encodeordecodeinput[0]:

        intcipherlist = stringtoint(str(input("\nPlease write your message: \n")))

        mystringlist = []
        for i in intcipherlist:
            stringer = str(i)
            mystringlist.append(stringer)
        myintstring = ", ".join(mystringlist)
        print(textcolors.okblue, "\n\nYour message as ASCII:\n", myintstring, textcolors.endc)

        foundcontact = None

        while foundcontact == None:
            contactname = str(input("\nWrite a contact's name or write 'other' to add a new contact:\n"))
            contactname = contactname.lower()
            if contactname == "other":
                Ne = str(input("\nPlease give the public key (N and e separated by a comma and a space):\n"))
                N = int(Ne.split(", ")[0])
                e = int(Ne.split(", ")[1])
                name = str(input("\nPlease write the contact's name:\n"))
                contactreader = open("contacts.cadersa", "r")
                contactfilelist = contactreader.readlines()

                if len(contactfilelist) == 0:
                    contactwriter = open("contacts.cadersa", "w")
                    contactwriter.write(f"{name}:\n{N}, {e}")
                else:
                    contactwriter = open("contacts.cadersa", "a")
                    contactwriter.write(f"\n{name}:\n{N}, {e}")
                print("\nContact added!\n")
                foundcontact = True
            else:
                contactreader = open("contacts.cadersa", "r")
                currentcontacts = contactreader.readlines()
                for i in range(len(currentcontacts)):
                    currentcontacts[i] = currentcontacts[i].rstrip("\n")
                    currentcontacts[i] = currentcontacts[i].rstrip(":")
                    currentcontacts[i] = currentcontacts[i].lower()

                for i in range(len(currentcontacts)):
                    if i % 2 != 0:
                        continue
                    else:
                        if contactname == currentcontacts[i]:
                            foundcontact = i+1
                            break
                
                if foundcontact != None:
                    contactdetails = currentcontacts[foundcontact].split(", ")
                    print(f"\n{currentcontacts[foundcontact-1]}'s Public Key: {contactdetails}\n")
                    N = int(contactdetails[0])
                    e = int(contactdetails[1])
                else:
                    print("\nContact not found...")


        mycodedlist = []
        for i in intcipherlist:
            codedintcharacter = (i**e) % N #Encoding formula is C = M^e mod N
            mycodedlist.append(codedintcharacter)

        for i in range(len(mycodedlist)):
            mycodedlist[i] = str(mycodedlist[i])
        mycodedstring = ", ".join(mycodedlist)

        print("\nCoded Message:", mycodedstring)
        yesorno = str(input('\nCopy to clipboard? y/n  '))
        if yesorno == 'y':
            pyperclip.copy(mycodedstring)
            print('The ciphertext has been copied to the clipboard')

    elif "d" == encodeordecodeinput[0]: #decode the message
        username = str(input("\nWrite your first name:\n"))
        password = str(input("\nEnter your password:\n"))

        userreader = open("users.cadersa", "r")
        userlist = userreader.readlines()

        for i in range(len(userlist)):
            userlist[i] = userlist[i].rstrip("\n")
            userlist[i] = userlist[i].rstrip(":")
            userlist[i] = userlist[i].lower()

        loggedinas = None
        for i in range(len(userlist)):
            if i % 6 != 0:
                continue
            else:
                if userlist[i] == username.lower():
                    loggedinas = i
                    if userlist[i+1].lower() == password.lower():
                        print("\nLogged in successfully!\n")
                        loggedinas = i
                        break
                    else:
                        print("Incorrect password...")
                        sys.exit()

        if loggedinas != None:
            pq = userlist[loggedinas+5]
            p = int(pq.split(", ")[0])
            q = int(pq.split(", ")[1])
            Ne = userlist[loggedinas+3]
            e = int(Ne.split(", ")[1])
        else:
            print("\nThat doesn't match any users...\nCreate new user?")
            yesorno = str(input())
            yesorno = yesorno.lower()
            if "y" in yesorno or "s" in yesorno:
                publicandprivate = primefinder.getprimes()
                publickeystring = str(publicandprivate[0])+", "+str(publicandprivate[1])
                privatekeystring = str(publicandprivate[2])+", "+str(publicandprivate[3])
                userfilelist = userreader.readlines()
                if len(userfilelist) == 0:
                    userwriter = open("users.cadersa", "w")
                    userwriter.write(f"{username}:\n{password}\nPublic key:\n{publickeystring}\nPrivate key:\n{privatekeystring}")
                else:
                    userwriter = open("users.cadersa", "a")
                    userwriter.write(f"\n{username}:\n{password}\nPublic key:\n{publickeystring}\nPrivate key:\n{privatekeystring}")


                contactreader = open("contacts.cadersa", "r")
                contactfilelist = contactreader.readlines()
                if len(contactfilelist) == 0:
                    contactwriter = open("contacts.cadersa", "w")
                    contactwriter.write(f"{username}:\n{publickeystring}")
                else:
                    contactwriter = open("contacts.cadersa", "a")
                    contactwriter.write(f"\n{username}:\n{publickeystring}")

                print("\nSuccessfully created a new user!\n")

            sys.exit()
        C = str(input("Please enter the coded message: \n"))

        N = p*q
        print(textcolors.okblue, f"\n\n\nCalculating N... {N}")

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

        print(textcolors.endc, f"\n\nHere is your message: {decodedmessage}")


        yesorno = str(input('\nCopy to clipboard?\n'))
        if 'y' in yesorno or "s" in yesorno:
            pyperclip.copy(decodedmessage)
            print('The ciphertext has been copied to the clipboard')


    elif "p" == encodeordecodeinput[0]:
        print("\nPlease log in...")
        username = str(input("\nWrite your first name:\n"))
        password = str(input("\nEnter your password:\n"))

        userreader = open("users.cadersa", "r")
        userlist = userreader.readlines()

        for i in range(len(userlist)):
            userlist[i] = userlist[i].rstrip("\n")
            userlist[i] = userlist[i].rstrip(":")
            userlist[i] = userlist[i].lower()

        loggedinas = None
        for i in range(len(userlist)):
            if i % 6 != 0:
                continue
            else:
                if userlist[i] == username.lower():
                    loggedinas = i
                    if userlist[i+1].lower() == password.lower():
                        print("\nLogged in successfully!\n")
                        loggedinas = i
                        break
                    else:
                        print("Incorrect password...")
                        sys.exit()
    

        if loggedinas != None:
            pq = userlist[loggedinas+5]
            p = int(pq.split(", ")[0])
            q = int(pq.split(", ")[1])
            Ne = userlist[loggedinas+3]
            e = int(Ne.split(", ")[1])
            print(f"Public Key: \nN = {p*q}\ne = {e}\n\nPrivate Key:\np = {p}\nq = {q}")
            
            yesorno = str(input('\nCopy Public Key to clipboard?\n'))

            if 'y' in yesorno or "s" in yesorno:
                pyperclip.copy(Ne)
                print('\nSuccessfully copied!\n')

        else:
            print("\nIncorrect user or password...\n")
            sys.exit()
    
    else:
        username = str(input("\nWrite your first name:\n"))
        password = str(input("\nEnter your password:\n"))

        userreader = open("users.cadersa", "r")
        userlist = userreader.readlines()

        for i in range(len(userlist)):
            userlist[i] = userlist[i].rstrip("\n")
            userlist[i] = userlist[i].rstrip(":")
            userlist[i] = userlist[i].lower()

        for i in range(len(userlist)):
            if i % 6 != 0:
                continue
            else:
                if userlist[i] == username.lower():
                    print("\nUser already exists!\n")
                    sys.exit()

        userwriter = open("users.cadersa", "a")
        publicandprivate = primefinder.getprimes()
        publickeystring = str(publicandprivate[0])+", "+str(publicandprivate[1])
        privatekeystring = str(publicandprivate[2])+", "+str(publicandprivate[3])

        userfilelist = userreader.readlines()
        if len(userfilelist) == 0:
            userwriter = open("users.cadersa", "w")
            userwriter.write(f"{username}:\n{password}\nPublic key:\n{publickeystring}\nPrivate key:\n{privatekeystring}")
        else:
            userwriter = open("users.cadersa", "a")
            userwriter.write(f"\n{username}:\n{password}\nPublic key:\n{publickeystring}\nPrivate key:\n{privatekeystring}")

        contactreader = open("contacts.cadersa", "r")
        contactfilelist = contactreader.readlines()
        if len(contactfilelist) == 0:
            contactwriter = open("contacts.cadersa", "w")
            contactwriter.write(f"{username}:\n{publickeystring}")
        else:
            contactwriter = open("contacts.cadersa", "a")
            contactwriter.write(f"\n{username}:\n{publickeystring}")

        print("\nSuccessfully created a new user!\n")



except KeyboardInterrupt:
    closefiles()
    print(textcolors.bold, textcolors.fail, "\nProgram stopped...")
    print(textcolors.endc)
except:
    closefiles()
    print(textcolors.bold, textcolors.fail, "\nError Occurred...")
    print(textcolors.endc)