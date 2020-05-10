import socket
import threading

PORT = 4343
HOST = "127.0.0.1"
ADDRESS = (HOST, PORT)
FORMAT = "utf-8"
DISCONECT_MESSAGE = "[DISCONECT]"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def threaded_client_handler(conn, addr):
    print(f"[CONNECTION] {addr}")

    connected = True
    while connected:
        msg = conn.recv(2064)
        if not msg:
            connected = False
        if msg == DISCONECT_MESSAGE:
            connected = False
            
    print(f"[{addr}] {msg}")
    conn.close()


def server_start():
    print(f"[START] {HOST}:{PORT}")
    server.listen()
    listening = True
    while listening:
        try:
            conn, addr = server.accept()
            thread = threading.Thread(target=threaded_client_handler, args=(conn, addr))
            thread.start()
        except KeyboardInterrupt:
            print("[STOP] Server stoped")
            break

print("[STARTING]")
server_start()
