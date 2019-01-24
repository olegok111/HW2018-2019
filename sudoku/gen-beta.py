import random


def adjust_strs_from_cols(cols: list, strs: list):
    new_strs = strs[:]
    for col_index in range(9):
        for elem_index in range(9):
            strs[elem_index][col_index] = cols[col_index][elem_index]
    return new_strs


def adjust_cols_from_strs(cols: list, strs: list):
    new_cols = cols[:]
    for str_index in range(9):
        for elem_index in range(9):
            cols[elem_index][str_index] = strs[str_index][elem_index]
    return new_cols
    

def generate_field():
    pole_strs = []
    pole_cols = []
    cur_column = -1
    for i in range(9):
        pole_cols.append([])

    for _ in range(9):
        pst = []
        for __ in range(9):
            cur_column = (cur_column + 1) % 9
            if _ <= 2:
                value = (_*3 + __ + 1) % 9
            elif 3 <= _ <= 5:
                value = (_*3 + __ + 2) % 9
            else:
                value = (_*3 + __ + 3) % 9
            if value == 0:
                value = 9
            pst.append(value)
            pole_cols[cur_column].append(value)
        pole_strs.append(pst)

    str_block0 = pole_strs[:3]
    random.shuffle(str_block0)
    str_block1 = pole_strs[3:6]
    random.shuffle(str_block1)
    str_block2 = pole_strs[6:]
    random.shuffle(str_block2)
    str_blocks = [str_block0, str_block1, str_block2]
    random.shuffle(str_blocks)

    new_pole_strs = []
    new_pole_cols = []
    for str_block in str_blocks:
        new_pole_strs.extend(str_block)
    pole_strs = new_pole_strs
    pole_cols = adjust_cols_from_strs(pole_cols, pole_strs)

    col_block0 = pole_cols[:3]
    random.shuffle(col_block0)
    col_block1 = pole_cols[3:6]
    random.shuffle(col_block1)
    col_block2 = pole_cols[6:]
    random.shuffle(col_block2)
    col_blocks = [col_block0, col_block1, col_block2]
    random.shuffle(col_blocks)

    for col_block in col_blocks:
        new_pole_cols.extend(col_block)
    pole_cols = new_pole_cols
    pole_strs = adjust_strs_from_cols(pole_cols, pole_strs)

    return pole_strs


def print_pole(strs):
    for az in strs:
        for buki in az:
            print(buki, end=' ')
        print()


def write_to_txt(strs):
    with open('field.txt', 'w', encoding='utf8') as file:
        for pole_str in strs:
            for pole_elem in pole_str:
                print(pole_elem, end=' ', file=file)
            print(file=file)
        print('---', file=file)


if __name__ == '__main__':
    field_strs = generate_field()
    print_pole(field_strs)
    write_to_txt(field_strs)
