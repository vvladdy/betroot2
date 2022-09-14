import socket

HOST = socket.gethostbyname(socket.gethostname())

PORT = 45000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.sendall('Hello, Python'.encode('utf-8'))

data = client.recv(1024)
client.close()