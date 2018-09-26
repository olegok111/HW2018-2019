import field

def comp_turn(game_field):
    combs = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    turn_was_made = False
    for comb in combs:
        marks = [game_field[i] for i in comb]
        s = sum(marks)
        if s == 2 or s == -2:
            for fld_index in comb:
                if game_field[fld_index] == 0:
                    game_field[fld_index] = 1
                    print('Мой ход', fld_index + 1)
                    turn_was_made = True
                    break
        if turn_was_made:
            break
    if not turn_was_made:  # "центровая стратегия"
        if game_field[4] == -1:
            for fld_index in [0, 2, 6, 8]:
                if game_field[fld_index] == 0:
                    game_field[fld_index] = 1
                    print('Мой ход', fld_index + 1)
                    turn_was_made = True
                    break
    if not turn_was_made:  # "ставим в центр"
        if game_field[4] == 0:
            game_field[4] = 1
            print('Мой ход 5')
            turn_was_made = True
    if not turn_was_made:  # крайний случай
        for comb in combs:
            marks = [game_field[i] for i in comb]
            s = sum(marks)
            if s == 0 or s == -1:
                for fld_index in comb:
                    if game_field[fld_index] == 0:
                        game_field[fld_index] = 1
                        print('Мой ход', fld_index + 1)
                        turn_was_made = True
                        break
            if turn_was_made:
                break
    return game_field


def man_turn(game_field):
    human_turn = field.check_human_next_move(game_field)
    game_field[human_turn - 1] = -1
    return game_field


def game():
    game_field = field.create_field()
    turn = 'm'
    end_game = False
    while not end_game:
        if turn == 'm':
            game_field = man_turn(game_field)
            turn = 'c'
        elif turn == 'c':
            game_field = comp_turn(game_field)
            turn = 'm'
        if not field.check_winner(game_field):
            end_game = True
        elif 0 not in game_field:
            print('Ничья.')
            end_game = True
        field.print_field(game_field)


if __name__ == '__main__':
    print("""
    =========Крестики-Нолики ver 1.0OG=========
    =   Теперь тут нет громких заявлений...   =
    ===========================================
    """)
    print('Вы ходите первым!')
    print('1 2 3')
    print('4 5 6')
    print('7 8 9')
    game()