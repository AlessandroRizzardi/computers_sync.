import ntplib
import socket
import struct

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

ntp_client = ntplib.NTPClient()
response = ntp_client.request('0.pool.ntp.org')

t1 = response.tx_time
#print(t1)

data = struct.pack('d',t1)
client.send(data)

client.close()
