import socket

server_socket = socket.socket()
server_socket.bind(('192.168.194.231', 2345))
server_socket.listen(1)
print("Server is listening on port 2345...")

conn, addr = server_socket.accept()
print("Got connection from", addr)

while True:
    #get client message first
    client_msg = conn.recv(1024).decode()
    #if client message not exists then break
    if not client_msg:
        break
    #if client message exists then print it
    print("Client:", client_msg)

    if client_msg.strip().lower() == 'bye':
        print("Client ended the chat.")
        break

    #take input from server
    reply = input("Server: ")
    #send reply to client
    conn.send(reply.encode())

    if reply.strip().lower() == 'bye':
        print("Server ended the chat.")
        break

conn.close()
server_socket.close()



chat with multiple clients

import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            print(f"{address}: {message}")
            if message.strip().lower() == "bye":
                print(f"[-] Client {address} disconnected.")
                break

            reply = input(f"Reply to {address}: ")
            client_socket.send(reply.encode())

            if reply.strip().lower() == "bye":
                print(f"[-] You ended chat with {address}.")
                break

        except:
            break

    client_socket.close()

# Main server setup
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 2345))
server_socket.listen(5)

print("[*] Server listening on port 2345...")

while True:
    client, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client, addr))
    thread.start()



import socket
server_socket=socket.socket()
server_socket.bind('192.168.0.1', 1234)
server_socket.listen(2)

conn, address=server_socket.accept()

while True:
    msg=conn.recv(1024).decode()
    print('client: ', msg)
    if msg.lower()=='bye':
        print('client left chatting')
        break
    
    reply=input('server: ')
    conn.send(reply.encode())
    if reply.lower()=='bye':
        print('server left chatting')
        break

    conn.close()
    server_socket.close()

import socket
import threading

def handleClient(conn, address):
    print(f'New connection from {address}')

    while True:
        try:
            msg=conn.recv(1024).decode()
            if not msg:
                break

            print(f'{address}: ', msg)
            if msg.lower()=='bye':
                print(f'{address} left chatting')
                break

            reply=input(f'reply to {address}: ')
            conn.send(reply.encode())
            if reply.lower()=='bye':
                print(f'You left chatting with {address}')
                break
        except:
            break

    conn.close()

server_socket=socket.socket()
server_socket.bind(('0.0.0.0', 1234))
server_socket.listen(2)
print('server is listening on port 1234')

while True:
    conn, address=server_socket.accept()
    thread=threading.Thread(target=handleClient, args=(conn, address))
    thread.start()

