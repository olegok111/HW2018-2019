#coding: utf-8
import socket

client_sock = socket.socket()
client_sock.connect(('127.0.0.1', 27001))
operation = True
data = client_sock.recv(1024)
beginner = False
if data == b'b':
    beginner = True
EXCLUSIVES = ('ъ', 'ь')

while operation:
    city_accepted = False
    if beginner:
        print('Вы начинаете!')
        city = input('Введите название города:')
        client_sock.sendall(bytes(city, 'utf8'))
    else:
        while not city_accepted:
            other_player_city = client_sock.recv(1024)
            other_player_city = other_player_city.decode('utf8')
            last_letter = other_player_city[-1]
            if last_letter in EXCLUSIVES:
                last_letter = other_player_city[-2]
                if last_letter in EXCLUSIVES:
                    print('Такого города совершенно точно нет!')
                    city_accepted = False
            city_accepted = True
            last_letter = last_letter.upper()
        city = input('Введите название города на', last_letter)
        client_sock.sendall(bytes(city))