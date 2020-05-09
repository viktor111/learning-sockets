import  socket

PORT = 8000
HOST = "127.0.0.1"
conn_opt = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(conn_opt)
    client.sendall(b"Hello from client!")
    data = client.recv(1024)
