# We will need th folling module to generate randomized lost packets
import random
import time
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port num to socket
serverSocket.bind(('', 12000))

print 'Ready to serve...'

while True:
    # Generate random num in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, addr = serverSocket.recvfrom(1024)
    print 'Receive: ', message
    # Capitalize the message from the client
    message = message.upper()

    # If rand is less than 4 , we consider the packetlost and do not respond
    if rand < 4:
        continue

    # Otherwise, the server responses
    serverSocket.sendto(message, addr)
    time.sleep(0.5)
