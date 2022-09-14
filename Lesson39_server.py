# TASK 3

# Create a socket echo server that handles each connection using the
# multiprocessing library.

import socket
import multiprocessing

def conn():
    HOST = socket.gethostbyname(socket.gethostname())
    print(HOST)
    PORT = 45000
    ADRESS = (HOST, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT)) # должен быть кортеж, важно что 1 элемент
    #server.bind(ADRESS)        # или вот так

    print(f'Socket success binded to port {PORT}')
    return server

def start_server(server):

    print('Server listen...')
    server.listen()
    connection, addr = server.accept()

    while True:
        print(f'New connection {addr}')
        data = connection.recv(1024)
        if not data:
            break
        connection.send(data)
        print(data.decode('utf-8'))
    connection.close()

if __name__ == '__main__':
    # p1 = multiprocessing.Process(target=conn)
    p2 = multiprocessing.Process(target=start_server, args=(conn(),))
    p2.start()
    # p1.start()
    # p1.join()