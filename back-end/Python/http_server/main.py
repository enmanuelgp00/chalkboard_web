import socket
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)
print("Listening on port {0}".format(SERVER_PORT))


def handle_request(client_socket) :
    request = client_socket.recv(1024).decode()
    print(request)
    headers = request.split('\n')
    fileName = headers[0].split()[1]
    
    if fileName == '/' :
        fileName = '/index.html'

    try :
        file = open('.' + fileName)
        content = file.read()
        file.close()            
        if fileName.endswith('.js') :
            mime_type = 'application/javascript'
        elif fileName.endswith('.html') :
            mime_type = 'text/html'
        else :
            mime_type = 'text/plain'
        response = f'HTTP/1.1 200 OK \n Content-Type: {mime_type} \n\n {content}'

    except FileNotFoundError:
        response = f'HTTP/1.1 404 NOT FOUND \n\n File not found'    
    
    client_socket.sendall(response.encode())
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    handle_request(client_socket)