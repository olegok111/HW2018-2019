
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

def print_pole(rows):
    for az in rows:
        for buki in az:
            print(buki, end=' ')
        print()

def get_square_elements(x, y, strs): # int -> int -> list(list(int)) -> set(int)
    str_coords = [i for i in range(x // 3 * 3, (x + 3) // 3 * 3)]
    col_coords = [i for i in range(y // 3 * 3, (y + 3) // 3 * 3)]
    res = []
    for str_coord in str_coords:
        for col_coord in col_coords:
            res.append(strs[str_coord][col_coord])
    return set(res)

def read_field(file='field.txt'):
    with open(file, 'r', encoding='utf8') as field_file:
        lines = field_file.readlines()
        rows = []
        for line in lines:
            row = line.split()
            rows.append(row)
    return rows

def write_to_txt(rows, filename):
    with open(filename, 'w', encoding='utf8') as file:
        for field_row in rows:
            for field_elem in field_row:
                print(field_elem, end=' ', file=file)
            print(file=file)