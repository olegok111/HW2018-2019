import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)

while True:
    # Бесконечно обрабатываем входящие подключения
    socket_a, address_a = serv_sock.accept() # блокирующий метод
    socket_b, address_b = serv_sock.accept()

    while True:
        print('accepted')
        data_a = socket_a.recv(1024)
        socket_b.sendall(data_a)
        print('A:', data_a)
        data_b = socket_b.recv(1024)
        socket_a.sendall(data_b)
        print('B:', data_b)
        if not (data_a or data_b):
            # Кто-то закончил игру
            break

    socket_a.close()
    socket_b.close()