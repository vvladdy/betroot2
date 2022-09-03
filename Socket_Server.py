import socket

PORT = 8001

HEADER = 64

SERVER = socket.gethostbyname(socket.gethostname())

print(SERVER)

ADDRESS = (SERVER, PORT)

ENCODING = 'utf-8'
DISCONNECT = 'exit'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDRESS)


def handle_client(connection, address):
    print(f'New connection - {address}')
    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode('utf-8')
        print(message_length)
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(ENCODING)
            if message == DISCONNECT:
                connected = False

            print(f'[{address}] - {message}')
            connection.send(f'Message receive from {address}'.encode(ENCODING))
    connection.close()


def start():
    server.listen()
    print(f'server listen on {SERVER}')
    while True:
        connection, address = server.accept()
        handle_client(connection, address)


print('Server started')
start()