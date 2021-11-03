import socket
IP = "localhost"
Port = 2000
ADD = (IP, PORT)
Disconn = "Exit"
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADD)
    print("Клиент подключен к серверу: {IP}:{Port}")
    while True:
        msg = input(" ")
        client.send(msg.encode("utf-8"))
        if msg == Disconn:
            client.send(encode("utf-8"))
            break
        else:
            msg = client.recv(2000).decode("utf-8")
            print("{msg}")
if __name__ == "__main__":
    main()
