import socket
import tqdm
import threading
p = threading.Thread()

ports = [] #доступные
N = 100000
for port in tqdm.tqdm(range(1, N + 1)):
    sock = socket.socket()
    try:
        sock.connect(port)
        ports.append(port)
    except:
        continue
    finally:
        sock.close()
for port in ports:
    print(port)
