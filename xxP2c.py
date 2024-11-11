from socket import *
import time
import random
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

print("Running Ping server w delays")

while True:
# Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    # simulating packet loss
    packet_loss_chance = random.randint(1, 100)
    if packet_loss_chance <= 10:
        print("Packet lost")
        continue

    delay = random.randint(10, 20)
    time.sleep(delay / 1000)
# The server responds
    serverSocket.sendto(message, address)

