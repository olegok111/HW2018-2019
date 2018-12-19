#coding: utf-8
import socket
import csv

print('Я сервер!')
sock = socket.socket()
sock.bind(('127.0.0.1', 27001))
sock.listen(2)

list_of_cities = []
with open('spisok.csv', 'r', encoding='utf8') as raw_spisok:
    spisok = csv.DictReader(raw_spisok, delimiter=';')
    for row in spisok:
        list_of_cities.append(row['Город'].lower())
print('Список городов загружен')

lives_1 = 3
lives_2 = 3

while True:
    socket_1, address_1 = sock.accept()
    socket_2, address_2 = sock.accept()
    socket_1.sendall(b'b')
    turn = 1
    convoluted = False
    last_city = ''
    while True:
        if turn == 1:
            socket_1.sendall(b'y')
            data_1 = socket_1.recv(1024).decode('utf8')
            ldata_1 = data_1.lower()
            print('ldata_1:', ldata_1)
            if 'а' <= ldata_1[0] <= 'я': # буква ё не учитывается, т.к. не существует городов на Ё
                print(1, data_1)
                if ldata_1 not in list_of_cities:
                    text_to_send = 'Соперник назвал город ' + data_1 + '. Принять?(Да или Нет)'
                    socket_2.sendall(text_to_send.encode())
                    socket_2.sendall(b'y')
                    answer = socket_2.recv(1024).decode().lower()
                    if answer == 'да':
                        turn = 2
                    elif answer == 'нет':
                        turn = 1
                        socket_1.sendall(
                            'Соперник посчитал, что такого города не существует. Назовите другой город.'.encode())
                        lives_1 -= 1
                else:
                    turn = 2
                last_city = ldata_1
            if turn == 2:
                text_to_send = 'Был назван город ' + data_1 + '. Вам на '
                if last_city[-1] in ('ь', 'ъ'):
                    last_city = last_city[:-1]
                text_to_send += last_city[-1].upper() + '!'
                socket_2.sendall(text_to_send.encode())
        elif turn == 2:
            socket_2.sendall(b'y')
            data_2 = socket_2.recv(1024).decode('utf8')
            ldata_2 = data_2.lower()
            print('ldata_2:', ldata_2)
            if 'а' <= ldata_2[0] <= 'я':  # буква ё не учитывается, т.к. не существует городов на Ё
                print(2, data_2)
                if ldata_2 not in list_of_cities:
                    text_to_send = 'Соперник назвал город ' + data_2 + '. Принять?(Да или Нет)'
                    socket_1.sendall(text_to_send.encode())
                    socket_1.sendall(b'y')
                    answer = socket_1.recv(1024).decode().lower()
                    if answer == 'да':
                        turn = 1
                    elif answer == 'нет':
                        turn = 2
                        socket_2.sendall(
                            'Соперник посчитал, что такого города не существует. Назовите другой город.'.encode())
                        lives_2 -= 1
                else:
                    turn = 1
                last_city = ldata_2
            if turn == 1:
                text_to_send = 'Был назван город ' + data_2 + '. Вам на '
                if last_city[-1] in ('ь', 'ъ'):
                    last_city = last_city[:-1]
                text_to_send += last_city[-1].upper() + '!'
                socket_1.sendall(text_to_send.encode())

    socket_1.close()
    socket_2.close()
