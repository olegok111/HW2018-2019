# -*- coding: utf-8 -*-
import random

# все горизонтали и ветикали и диогонали
POSITIONS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def create_field():  # создание поля
    field = [0 for i in range(9)]
    return field # out : [0,0,0,0,0,0,0,0,0]


def print_field(f):  # печать поля
    for i in range(9):
        if f[i] == -1:
            elem = '0'
        elif f[i] == 0:
            elem = '8'
        elif f[i] == 1:
            elem = 'X'
        print(elem, end=' ')
        if (i + 1) % 3 == 0:
            print()
    print()


def check_human_next_move(game_field):  # проверка хода человека на правильность
    check_status = False
    while not check_status:
        cell = input('Введите номер клетки ещё раз ')
        check_status = True
        if not (cell.isdigit()):
            check_status = False
            continue
        if not (1 <= int(cell) <= 9):
            check_status = False
            continue
        if game_field[int(cell) - 1] != 0:
            check_status = False
            continue
    return int(cell) # out : num of human field


def check_next_pc_move(f, side):  # проверка хода компьютера
    if side == 'X':
        pc_win_sum = 2
    else:
        pc_win_sum = -2
    for grups in POSITIONS:
        # print (sum([f[grups[0]],f[grups[1]],f[grups[2]]]),grups)
        if sum([f[grups[0]], f[grups[1]], f[grups[2]]]) == pc_win_sum:
            if f[grups[0]] == 0:
                return grups[0]
            elif f[grups[1]] == 0:
                return grups[1]
            elif f[grups[2]] == 0:
                return grups[2]
    for grups in POSITIONS:
        if sum([f[grups[0]], f[grups[1]], f[grups[2]]]) == pc_win_sum * (-1):
            if f[grups[0]] == 0:
                return grups[0]
            elif f[grups[1]] == 0:
                return grups[1]
            elif f[grups[2]] == 0:
                return grups[2]
    while True:
        move = random.randint(0, 8)
        if f[move] == 0:
            return move


def check_winner(f):
    for items in POSITIONS:
        if sum([f[items[0]], f[items[1]], f[items[2]]]) == 3:
            print('Победа крестиков')
            return False
        elif sum([f[items[0]], f[items[1]], f[items[2]]]) == -3:
            print('Победа ноликов')
            return False
    return True

