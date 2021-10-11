import socket

PORT = 5050
BUFF = 1024
FORMAT = 'utf-8'

server =socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)

host_name = socket.gethostname()
ip_addr = socket.gethostbyname(host_name)
print(ip_addr)

server.bind((ip_addr,PORT))

server.listen()
print('Server is listening...')

conn, addr = server.accept()
print('Connection from: ' + str(addr))

data = conn.recv(BUFF)
print('Data received...')
conn.send(data)
print('Resending data...')

conn.close()