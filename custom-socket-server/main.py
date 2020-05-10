import socket
import threading

HOST = "127.0.0.1"
PORT = 8888
SERVER_CONNECTION = (HOST, PORT) 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(SERVER_CONNECTION)


def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")

def start_server():
    server.listen()
    print(f"[LISTENING] {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        

start_server()
