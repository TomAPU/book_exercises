from socket import *

serverPort = 12000

welcomeSocket = socket(AF_INET, SOCK_STREAM)
welcomeSocket.bind(('', serverPort))
welcomeSocket.listen(1)
print 'The proxy is ready to receive'

while 1:
    connectionSocket, address = welcomeSocket.accept()
    message = connectionSocket.recv(2048)
    print message
    connectionSocket.close()
