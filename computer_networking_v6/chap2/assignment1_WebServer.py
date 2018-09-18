from socket import *

port = 8080

def response404():
    lines = [
        "HTTP/1.1 404 Not Found",
        "Server: 127.0.0.1:" + str(port),
        "Content-Type: text/html; charset=utf-8"
            ]

    content = '''<html>
    404
    File not found
    </html>
    '''

    return '\r\n'.join(lines) + '\r\n\r\n' + content

def response200_header(byteCount):
    lines = [
        "HTTP/1.1 200 OK",
        "Connection: close",
        "Server: 127.0.0.1:" + str(port),
        "Content-Type: text/html; charset=utf-8",
        "Content-Length: " + str(byteCount)
        ]

    return '\r\n'.join(lines) + '\r\n\r\n'

def main(port, listen_count):

    # prepare a server socket
    welcomeSocket = socket(AF_INET, SOCK_STREAM)
    welcomeSocket.bind(('', port))
    welcomeSocket.listen(listen_count)

    print 'Ready to server...'

    while True:
        clientSocket, addr = welcomeSocket.accept()

        # request message example:
        #GET /hello.html HTTP/1.1
        #Host: 127.0.0.1:8080
        #Connection: keep-alive
        #Cache-Control: max-age=0
        #Upgrade-Insecure-Requests: 1
        #User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36
        #Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        #Accept-Encoding: gzip, deflate, br
        #Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6
        #Cookie: csrftoken=fAD2BxHI7xowQOkM323GqzsxfbETbKZOsvdu8iYxdStP4LhckPbTRjaulGyDwMuX
        request = clientSocket.recv(2048)
        lines = request.split('\r\n')
        method, path, protocol = lines[0].split(' ')
        _, host = lines[1].split(': ')

        print method, path, protocol, host

        filename = path[1:]
        try:
            f = open(filename)
            data = f.read()
            byteCount = len(data)
            clientSocket.send(response200_header(byteCount))

            for i in xrange(0, byteCount):
                clientSocket.send(data[i])

        except IOError:
            clientSocket.send(response404())

        clientSocket.close()
        break

    welcomeSocket.close()

if __name__ == "__main__":
    main(port, 1)
