import socket
import sys

s = socket.socket()
s.connect(('10.50.0.121', 12345))
while True:
    rcvdData = s.recv(1024).decode()
    #rcvdData = rcvdData.split(',')
    #rcvdData[0] = float(rcvdData[0])
    #rcvdData[1] = float(rcvdData[1])
    #mypoint = "("+str(rcvdData[0])+", "+str(rcvdData[1])+")"
    #print(mypoint)
    print("Windows: "+rcvdData)
    sendData = str(input("You: "))
    #sendData = 'thanks'
    s.send(sendData.encode())
s.close()
sys.exit('Connection ended!')
