import socket
client_connection = socket.socket()
port = 12345
client_connection.bind(('', port))
client_connection.listen(5)
print('Waiting for connection...')
to_client, addr = client_connection.accept()


#myloopnum = 0
while True:
    mystr = str(input("You: "))
    #myloopnum += 1
    #mystr = str(0)+',' +str(myloopnum)
    to_client.send(mystr.encode())
    print( "Raspberry Pi:",to_client.recv(1024).decode())
to_client.close()
