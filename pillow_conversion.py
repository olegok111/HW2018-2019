from PIL import Image
import easygui


def zeros_and_ones(filename:str, zero='0', one='1'):
    im = Image.open(filename)
    im = im.convert('1')
    size = im._size
    for y in range(size[1]):
        for x in range(size[0]):
            if im.getpixel((x, y)):
                print(one, end='')
            else:
                print(zero, end='')
        print()

n = easygui.fileopenbox(msg='Open an image you wish to convert')
setting = easygui.multenterbox(msg='Выберите, какое значение будет нулём, а какое - единицей', fields=['0:', '1:'])
zeros_and_ones(n, setting[0], setting[1])
