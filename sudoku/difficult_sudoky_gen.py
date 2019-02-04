import random

# def read_field(): ...

def set_difficulty(pole_rows:list, difficulty:int):
    for row in range(9):
        indexes = [i for i in range(9)]
        random.shuffle(indexes)
        if difficulty == 1:
            indexes_to_erase = indexes[:3]
        elif difficulty == 2:
            indexes_to_erase = indexes[:5]
        elif difficulty == 3:
            if row % 2 == 0:
                indexes_to_erase = indexes[:7]
            else:
                indexes_to_erase = indexes[:6]
        for i in indexes_to_erase:
            pole_rows[row][i] = 'X'

    return pole_rows

# if __name__ == '__main__': ...
