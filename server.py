# 1

# Реалізуйте клієнт-серверний додаток з можливістю
# зворотного обміну повідомленнями. Для початку спілкування встановіть з’єднання.
# Після з’єднання використайте текстовий формат. У бесіді беруть участь лише дві
# особи. Після завершення спілкування сервер переходить
# до очікування нового учасника розмови.

import socket
import json

def write_data(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file)

def upload_data(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(1)

data = {
    "Ukraine": {
        "Kyiv": "Sunny",
        "Kharkiv": "Cold",
        "Lviv": "Cloudy"
    },

    "USA": {
        "New York": "Rainy",
        "Los Angeles": "Sunny",
        "Chicago": "Snowy"
    }

}
write_data(data, 'data.json')
upload_data("data.json")

while True:
    client_socket, address = server.accept()
    print(f"Connection from {address}")

    request = client_socket.recv(1024).decode()
    country, city = request.split(",")

    if country in data and city in data[country]:
        response = data[country][city]
    else:
        response = "Weather data not available"

    client_socket.send(response.encode())
    client_socket.close()