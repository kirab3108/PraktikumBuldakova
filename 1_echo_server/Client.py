import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(input('Введите здесь номер порта'))
host = input('Введите здесь имя хоста')
try:
    client.connect((host, port))
except (ConnectionRefusedError, socket.gaierror):
    print("Соединение сейчас недоступно. Хотите установить значения по умолчанию? Y\\N")
    if input() == "Y":
        client.connect(('127.0.0.1', 2000))
    else:
        print('Попробуйте снова')
        exit()
print(client.recv(2048).decode('utf-8'))
try:
        while True:
            client.send(input('Введите текст для сервера:').encode('utf-8'))
            data = client.recv(2048).decode('utf-8')
            time.sleep(3)
            if data.lower() == 'exit':
                print('До свидания!')
                client.send(encode('utf-8')
                client.shutdown(socket.SHUT_WR)
                exit()
            if data:
                print(data)
except KeyboardInterrupt:
    client.shutdown(socket.SHUT_WR)
except BrokenPipeError:
    server.shutdown(socket.SHUT_WR)
