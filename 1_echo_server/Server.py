import socket
import time
print('Запуск сервера')
Port = 2000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', Port))
try:
    while True:
        server.listen(1)
        client_socket, address = server.accept()
        print('Пользователь {address} подсоединен')
        client_socket.send(encode('utf-8'))
        while True:
            try:
                data = client_socket.recv(2048).decode('utf-8')
            except OSError:
                data = None
            time.sleep(3)
            if data:
                print(data)
            msg = input('Введите текст').encode('utf-8')
            client_socket.send(msg)
            if msg == 'exit'.encode('utf-8'):
                time.sleep(2)
                print('До свиания!')
                server.shutdown(socket.SHUT_WR)
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server.bind(('127.0.0.1', 2000))
                break
except KeyboardInterrupt:
    server.shutdown(socket.SHUT_WR)
except BrokenPipeError:
    server.shutdown(socket.SHUT_WR)
