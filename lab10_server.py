import socket
import threading

clients = []
threads = []

def broadcast(message, sender_conn):
    for client_conn in clients:
        if client_conn != sender_conn:
            try:
                client_conn.send(message.encode('utf-8'))
            except (socket.error, BrokenPipeError):
                clients.remove(client_conn)

def client_thread(conn, addr):
    print(f"Connected by {addr}")
    clients.append(conn)

    try:
        while True:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {addr}: {message}")
            broadcast(f"{addr}: {message}", conn)
    except (socket.error, ConnectionResetError, ConnectionAbortedError) as e:
        print(f"Error with client {addr}: {e}")
    finally:
        conn.close()
        clients.remove(conn)
        print(f"Connection with {addr} closed")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen()

    print("Server listening on port 5555")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=client_thread, args=(conn, addr))
            threads.append(thread)
            thread.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
        for thread in threads:
            thread.join()
        server.close()

if __name__ == "__main__":
    start_server()