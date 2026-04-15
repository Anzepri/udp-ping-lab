from socket import *
import time

serverName = "127.0.0.1"
serverPort = 12000

# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set timeout to 1 second
clientSocket.settimeout(1)

print("Pinging server...\n")

for i in range(1, 11):
    sendTime = time.time()
    message = f"Ping {i} {sendTime:.6f}"

    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        response, serverAddress = clientSocket.recvfrom(1024)
        receiveTime = time.time()

        rtt = receiveTime - sendTime

        print(f"Reply: {response.decode()}")
        print(f"RTT: {rtt:.4f} seconds\n")

    except (timeout, ConnectionResetError):
        print("Request timed out\n")

clientSocket.close()