import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 27001))
sock.listen(2)

while True:
    socket_1, address_1 = sock.accept()
    socket_2, address_2 = sock.accept()
    socket_1.sendall(b'b')
    while True:
        print('accepted')
        data_1 = socket_1.recv(1024)
        socket_2.sendall(data_1)
        print('A:', data_1)
        data_2 = socket_2.recv(1024)
        socket_1.sendall(data_2)
        print('B:', data_2)
        if not (data_1 or data_2):
            # Кто-то закончил игру
            break

    socket_1.close()
    socket_2.close()