## Client

import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 8080))

while True:

    data = input("Text here: ")

    client.send(data.encode())

    if data == 'stop':
        break

    response = client.recv(1024).decode()
    if not response:
        print("Server closed the connection.")
        break
    print(response)

client.close()