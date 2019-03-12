import random
import utils


def set_difficulty(field_rows:list, difficulty:int):
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
            field_rows[row][i] = 'X'

    return field_rows



def main():
    field = utils.read_field()
    d = int(input('Enter difficulty (1-3):'))
    new_field = set_difficulty(field, d)
    utils.write_to_txt(new_field, 'new_field.txt')
