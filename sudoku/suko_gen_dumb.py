import random

pole = []
for _ in range(9):
    pst = []
    for __ in range(9):
        if _ <= 2:
            value = (_*3 + __ + 1) % 9
        elif 3 <= _ <= 5:
            value = (_*3 + __ + 2) % 9
        else:
            value = (_*3 + __ + 3) % 9
        if value == 0:
            value = 9
        pst.append(value)
    pole.append(pst)
for az in pole:
    for buki in az:
        print(buki, end=' ')
    print()
