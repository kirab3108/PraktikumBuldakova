import socket
import threading
IP = "localhost"
Port = 2000
ADD = (IP, Port)
Disconn = "Exit"
def client(conn, add):
    print("Соединение: {add} установлено")
    while True:
        msg = conn.recv(2000).decode("utf-8")
        if msg == Disconn:
            break
        print("[{add}] {msg}")
        conn.send(msg.encode("utf8"))
    conn.close()
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADD)
    server.listen()
    while True:
        conn, add = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("Количество подключений: {threading.activeCount() - 1}")
if __name__ == "__main__":
    main()
