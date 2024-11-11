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

    delay = random.randint(10, 20)
    time.sleep(delay / 1000)
# The server responds
    serverSocket.sendto(message, address)

