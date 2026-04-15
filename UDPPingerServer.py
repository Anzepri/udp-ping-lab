import random
from socket import *

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind to port 12000
serverSocket.bind(('', 12000))

print("Server is ready...")

while True:
    # Random number for packet loss simulation
    rand = random.randint(0, 10)

    # Receive message
    message, address = serverSocket.recvfrom(1024)

    # Convert to uppercase
    message = message.upper()

    # Simulate packet loss (30%)
    if rand < 4:
        continue

    # Send response
    serverSocket.sendto(message, address)