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
yesorno = str(input('Copy to clipboard? y/n  '))
if yesorno == 'y':
    pyperclip.copy(ciphertext)
    print('The ciphertext has been copied to the clipboard')