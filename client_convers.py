import socket

PORT = 5050
BUFF = 1024
FORMAT = 'utf-8'

client =socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)

client_name = socket.gethostname()
ip_addr = socket.gethostbyname(client_name)

print('Insert server address: ')
server_addr = input()

client.connect((server_addr,PORT))
print('Connected to' + str(server_addr))

msg = input()


while msg != 'quit':
    print(str(client_name) + ': ' + msg)
    client.send(msg.encode(FORMAT))
    data = client.recv(BUFF).decode(FORMAT)
    print(str(client_name) + ': ' + data)
    msg = input()

client.close
    


