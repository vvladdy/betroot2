import socket

HOST = socket.gethostbyname(socket.gethostname())
print(HOST)

PORT = 56000

ADRESS = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADRESS)
print(f'Socket sucsess binded to port {PORT}')

def handle_client(connection, adress):
    print(f'New connection - {adress}')
    connection.send('Thank you for connecting'.encode())
    messagecl = connection.recv(1024).decode()
    print('Text coding Cesar code: ', messagecl)
    connection.close()

def start():
    server.listen()
    print(f'server listen on {HOST}')
    connection, address = server.accept()
    handle_client(connection, address)
print('Server started...')
start()
