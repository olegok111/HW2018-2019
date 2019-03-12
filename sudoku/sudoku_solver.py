import utils
import copy

def main(pole_strs):
    new_strs = copy.deepcopy(pole_strs)
    new_cols = utils.adjust_cols_from_rows(new_strs)
    all_pole_elems = set()
    for Str in new_strs:
        for elem in Str:
            all_pole_elems.add(elem)
    solved = len({'x', 'X', '0', 0} & all_pole_elems) == 0
    something_marked = False
    while not solved:
        for x in range(9):
            for y in range(9):
                the_elem = new_strs[x][y]
                neighbors = set(new_strs[x] + new_cols[y])
                neighbors.update(utils.get_square_elements(x, y, new_strs))
                neighbors -= {'x', 'X', '0', 0}
                if len(neighbors) == 8 and not ('1' <= str(the_elem) <= '9'):
                    something_marked = True
                    mark = ({str(i) for i in range(1,10)} ^ neighbors).pop()
                    new_strs[x][y] = mark
                    print(f'marked ad {mark}')
        all_pole_elems = set()
        for Str in new_strs:
            for elem in Str:
                all_pole_elems.add(elem)
        solved = len({'x', 'X', '0', 0} & all_pole_elems) == 0
        utils.write_to_txt(new_strs, 'thordo.txt')
        new_cols = utils.adjust_cols_from_rows(new_strs)
        if not something_marked:
            break
    if not something_marked:
        print('unsolveable')

if __name__ == '__main__':
    main(utils.read_field('new_field.txt'))