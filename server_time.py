import ntplib
import socket
import struct

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

ntp_client = ntplib.NTPClient()
response = ntp_client.request('0.pool.ntp.org')
t2 = response.tx_time
#print(t2)

[t1] = struct.unpack('d',data)
#print(t1)

delta_t = t2 - t1

print('delta_time = ',delta_t)

server.close()

