import socket
import time

PORT = 5050
BUFF = 1024
FORMAT = 'utf-8'

client =socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)

client_name = socket.gethostname()
ip_addr = socket.gethostbyname(client_name)

print('Insert server address: ')
server_addr = input()

client.connect((server_addr,PORT))
print('Connected to: ' + str(server_addr))

msg = 'message'

print('Sending...')
client.send(msg.encode(FORMAT))
start = time.perf_counter()

data = client.recv(BUFF)
end = time.perf_counter()
print("Received response...")

client.close()

print("delta_time = ", end -start, ' seconds')



