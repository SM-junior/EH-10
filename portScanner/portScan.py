import socket

# target=input('Enter IP to scan: ')
# ports=[22,80,443,8080]

# for port in ports:
#     sock=socket.socket()
#     sock.settimeout(1)
#     result=sock.connect_ex((target, port))

#     if result:
#         print(f'fort: {port} is open')
#     else:
#         print(f'port: {port} is closed')
#     sock.close()


#................. 1 to 100 port scanning...................
# target=input('Enter IP to scan: ')

# for port in range(1,101):
#     sock=socket.socket()
#     sock.settimeout(1)
#     result=sock.connect_ex((target, port))

#     if result:
#         print(f'fort: {port} is open')
#     else:
#         print(f'port: {port} is closed')
#     sock.close()

#...................65535 (all) port scanning....................

target=input('Please enter IP to scan..')
print(f'Scanning {target}...')

for port in range(1,65536):
    try:
        sock=socket.socket()
        sock.settimeout(0.3)
        result=sock.connect_ex((target, port))

        if result==0:
            print(f'port {port} is OPEN')
        else:
            print(f'port {port} is CLOSED')
        sock.close()
        
    except KeyboardInterrupt:
        print('\n scan interrupted by user')
        break
    except socket.error:
        print('count not connect to server')
        break