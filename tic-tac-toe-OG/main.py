import random
import field
import crosses
import zeroes


def decision():
    side = input('choose zeroes - 0 or crosses - 1 you will play')
    while side != '0' and side != '1':
        side = input('choose zeroes - 0 or crosses - 1 you will play')
    return side


if __name__ == '__main__':
    side:str = decision() #выбор стороны
    #side = "1"  # test
    if side == '1':
        crosses.game()
    else:
        zeroes.game()
