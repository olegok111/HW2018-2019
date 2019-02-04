import random


def adjust_rows_from_cols(cols: list):
    rows = []
    for i in range(9):
        _row = []
        for j in range(9):
            _row.append(0)
        rows.append(_row)
    for col_index in range(9):
        for elem_index in range(9):
            rows[elem_index][col_index] = cols[col_index][elem_index]
    return rows


def adjust_cols_from_rows(rows: list):
    cols = []
    for i in range(9):
        col = []
        for j in range(9):
            col.append(0)
        cols.append(col)

    for row_index in range(9):
        for elem_index in range(9):
            cols[elem_index][row_index] = rows[row_index][elem_index]
    return cols


def generate_primary_field():
    decset = [i for i in range(1,10)]
    random.shuffle(decset)
    pole_rows = []

    for _ in range(9):
        pst = []
        for __ in range(9):
            if _ <= 2:
                value = (_ * 3 + __ + 1) % 9
            elif 3 <= _ <= 5:
                value = (_ * 3 + __ + 2) % 9
            else:
                value = (_ * 3 + __ + 3) % 9
            if value == 0:
                value = 9
            pst.append(decset[value-1])
        pole_rows.append(pst)

    return pole_rows


def generate_field():
    pole_rows = generate_primary_field()
    # shuffling rows
    row_block0 = pole_rows[:3]
    random.shuffle(row_block0)
    row_block1 = pole_rows[3:6]
    random.shuffle(row_block1)
    row_block2 = pole_rows[6:]
    random.shuffle(row_block2)
    row_blocks = [row_block0, row_block1, row_block2]
    random.shuffle(row_blocks)
    # setting new rows and columns
    new_pole_rows = []
    new_pole_cols = []
    for row_block in row_blocks:
        new_pole_rows.extend(row_block)
    pole_rows = new_pole_rows
    pole_cols = adjust_cols_from_rows(pole_rows)
    # shuffling columns
    col_block0 = pole_cols[:3]
    random.shuffle(col_block0)
    col_block1 = pole_cols[3:6]
    random.shuffle(col_block1)
    col_block2 = pole_cols[6:]
    random.shuffle(col_block2)
    col_blocks = [col_block0, col_block1, col_block2]
    random.shuffle(col_blocks)
    # setting new rows and columns
    for col_block in col_blocks:
        new_pole_cols.extend(col_block)
    pole_cols = new_pole_cols
    pole_rows = adjust_rows_from_cols(pole_cols)

    return pole_rows


def print_pole(rows):
    for az in rows:
        for buki in az:
            print(buki, end=' ')
        print()


def write_to_txt(rows, filename):
    with open(filename, 'w', encoding='utf8') as file:
        for pole_row in rows:
            for pole_elem in pole_row:
                print(pole_elem, end=' ', file=file)
            print(file=file)


def main():
    field_rows = generate_field()
    write_to_txt(field_rows, 'field.txt')
