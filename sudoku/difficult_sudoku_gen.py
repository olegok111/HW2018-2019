import random


def read_field(file='field.txt'):
    with open(file, 'r', encoding='utf8') as field_file:
        lines = field_file.readlines()
        rows = []
        for line in lines:
            row = line.split()
            rows.append(row)
    return rows


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


def write_to_txt(rows, filename):
    with open(filename, 'w', encoding='utf8') as file:
        for field_row in rows:
            for field_elem in field_row:
                print(field_elem, end=' ', file=file)
            print(file=file)


def main():
    field = read_field()
    d = int(input('Enter difficulty (1-3):'))
    new_field = set_difficulty(field, d)
    write_to_txt(new_field, 'new_field.txt')
