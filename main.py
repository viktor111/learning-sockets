import socket

PORT = 8000
HOST = socket.gethostname()
conn_opt = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(conn_opt)

server.listen()

conn, address = server.accept()

while True:
    data = conn.recv(1024)
    
    if not data:
        break
    conn.sendall(data)
