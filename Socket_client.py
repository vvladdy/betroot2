import socket

PORT = 8001

HEADER = 64

SERVER = '192.168.8.102'

# print(SERVER)

ADDRESS = (SERVER, PORT)

ENCODING = 'utf-8'
DISCONNECT = 'exit'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDRESS)


def send(message):
    message = message.encode(ENCODING) # coding information
    message_length = len(message)
    send_length = str(message_length).encode(ENCODING)
    send_length += b'' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(ENCODING))


while (message := input('Enter message: ')) != DISCONNECT:
    send(message)
