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

connection = True

while connection:
    data = conn.recv(BUFF).decode(FORMAT)
    print(str(host_name) + ': ' + data)
    msg  = input()
    conn.send(msg.encode(FORMAT))
    print(str(host_name) + ': ' + msg)

    if msg == 'quit':
       connection = False
    
conn.close()





        
    

    

