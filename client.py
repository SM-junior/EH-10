import socket

client_socket = socket.socket()
#connect to server
client_socket.connect(('localhost', 2345))
# if connection is successful then..
while True:
    #take input from client
    msg = input("Client: ")
    #sent this to server
    client_socket.send(msg.encode())

    if msg.strip().lower() == 'bye':
        print("You ended the chat.")
        break
    
    #receive reply from server
    reply = client_socket.recv(1024).decode()
    # print server reply
    print("Server:", reply)

    if reply.strip().lower() == 'bye':
        print("Server ended the chat.")
        break

client_socket.close()

 

import socket

client_socket = socket.socket()
client_socket.connect(('192.168.0.102', 2345))  # or use server IP

while True:
    msg = input("Shahin: ")
    client_socket.send(msg.encode())

    if msg.lower().strip() == "bye":
        print("You ended the chat.")
        break

    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

    if reply.lower().strip() == "bye":
        print("Server ended the chat.")
        break

client_socket.close()


import socket
client_socket=socket.socket()
client_socket.connect('192.168.0.1', 1234)

while True:
    msg=input('Client: ')
    client_socket.send(msg.encode())

    if msg.lower()=='bye':
        print('You left chatting')
        break

    reply=client_socket.recv(1024).decode()
    print('server: ',reply)
    if reply.lower()=='bye':
        print('server left chatting')
        break

    client_socket.close()