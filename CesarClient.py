import socket
import string

HOST = '192.168.8.102'

PORT = 56000

ADRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADRESS)


def cesar_chifr(x):
    l, count, alpha, q = '', 0, string.ascii_letters, x.split()
    for j in range(len(q)):
        for h in q[j]:
            if h.lower() in alpha:
                count += 1
        for i in q[j]:
            if i.lower() not in alpha:
                l += 1
                continue
            if i.lower() == i:
                l += alpha[(alpha.find(i) + count) % 26]
            elif i.lower() != i:
                l += alpha[(alpha.find(i) + count) % 26].upper()
                count = 0
                l += ' '
    return  l

# x = input('Entre text: ')
# print(cesar_chifr(x))


print(client.recv(1024).decode())
client.send(cesar_chifr(input('Enter text: ')).encode())

client.close()
