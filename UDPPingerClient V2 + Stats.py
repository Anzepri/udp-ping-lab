import time
from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

rtts = []
lost = 0
total = 10

print("Pinging " + serverName + ":" + str(serverPort))

for i in range(1, total + 1):
    sendTime = time.time()
    message = f"Ping {i} {sendTime}"

    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        response, _ = clientSocket.recvfrom(1024)

        rtt = time.time() - sendTime
        rtts.append(rtt)

        print(f"Reply: {response.decode()} | RTT = {round(rtt, 4)} sec")

    except timeout:
        print("Request timed out")
        lost += 1

clientSocket.close()

# ---- Statistics ----
print("\n--- Ping Statistics ---")

received = total - lost
loss_rate = (lost / total) * 100

print(f"Packets: Sent={total}, Received={received}, Lost={lost} ({loss_rate:.1f}% loss)")

if rtts:
    print(f"RTT Min = {min(rtts):.4f} sec")
    print(f"RTT Max = {max(rtts):.4f} sec")
    print(f"RTT Avg = {sum(rtts)/len(rtts):.4f} sec")
else:
    print("No RTT data available")
