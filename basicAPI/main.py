import socket

PORT = 8000
HOST = "127.0.0.1"
conn_opt = (HOST, PORT)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    try:
        server.bind(conn_opt)
        server.listen()
    except OSError:
        print("Port in use")

    client_connection, address = server.accept()

    with client_connection:
        print("Client with ", address, " connected")

        while True:
            data = client_connection.recv(1024)
            if not data: 
                break
            client_connection.sendall(data)
            print(data)
