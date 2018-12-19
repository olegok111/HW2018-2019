#coding: utf-8
import socket

client_sock = socket.socket()
client_sock.connect(('127.0.0.1', 27001))
operation = True
my_turn = False
while operation:
    data = client_sock.recv(1024).decode('utf8')
    if not (data == '' or data == 'b' or data == 'y'):
        print(data)
    if data == 'b':
        print('Ваш ход первый! Назовите город')
        my_turn = True
    if data == 'y':
        my_turn = True
    if my_turn:
        ct = input()
        client_sock.sendall(ct.encode())
        my_turn = False
