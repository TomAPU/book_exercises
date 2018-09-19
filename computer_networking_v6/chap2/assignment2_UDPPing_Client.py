from socket import *
import time

COUNT = 10
SERVER = '127.0.0.1'
SERVER_PORT = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1) # 1 second

for i in range(COUNT):
    start_time = time.time()
    ping_msg = "Ping %d %f" % (i, start_time)
    clientSocket.sendto(ping_msg, (SERVER, SERVER_PORT))
    print ping_msg

    try:
        pong_msg, addr = clientSocket.recvfrom(1024)
        end_time = time.time()
        print pong_msg
        print "RTT is %.2f" % (end_time-start_time)
        print
    except timeout:
        print "Request timed out"
        print

clientSocket.close()
