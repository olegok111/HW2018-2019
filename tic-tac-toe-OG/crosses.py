import field
import random

def game():
    game_field = field.create_field()#создание поля
    field.print_field(game_field)#вывод поля на экран
    print ('my first move, cell number 5')
    move_number:int = 1 #номер ходов
    game_field[4] = 1 #ставлю крестик в середину, как наиболее понятный ход
    field.print_field(game_field)
    move_number += 1
    player_move = field.check_human_next_move(game_field) #первый ход игрока
    game_field[player_move - 1] = -1
    move_number +=1
    field.print_field(game_field)
    if move_number == 3:#если ход второй, то нужно ставить в любой угол
        corners_to_move = [0,2,6,8]
        while True:
            pc_move = random.choice(corners_to_move)
            if game_field[pc_move] == 0:
                game_field[pc_move] = 1
                field.print_field(game_field)
                print (pc_move)
                break
    move_number += 1
    player_move = field.check_human_next_move(game_field) #второй ход игрока
    game_field[player_move - 1] = -1
    field.print_field(game_field)

    game_state = True
    while game_state:#игровой цикл всех остальных ходов
        move_number += 1
        pc_move = field.check_next_pc_move(game_field,side='X')
        game_field[pc_move] = 1
        field.print_field(game_field)
        game_state = field.check_winner(game_field)
        if move_number < 9 and game_state:
            move_number += 1
            player_move = field.check_human_next_move(game_field) #другой ход игрока
            game_field[player_move - 1] = -1
            field.print_field(game_field)
            game_state = field.check_winner(game_field)
        if move_number == 9:
            print ('draw')
            break