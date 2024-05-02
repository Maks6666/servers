import socket

server_address = ('127.0.0.1', 8080)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)


country = input("Enter country: ")
city = input("Enter city: ")
request = f"{country},{city}"
client_socket.send(request.encode())


response = client_socket.recv(1024).decode()
print("Weather:", response)


client_socket.close()
