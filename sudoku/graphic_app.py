import pygame
import sudoku.utils as utils
from sudoku.difficult_sudoku_gen import main as diff_gen

BLACK = (  0,  0,  0)
RED   = ( 70,  0,  0)
WHITE = (255,255,255)
GREEN = (  0, 70,  0)
GRAY  = (127,127,127)

pygame.font.init()
FONT = pygame.font.SysFont('Tahoma', 26)
s1 = FONT.render('1', False, WHITE)
s2 = FONT.render('2', False, WHITE)
s3 = FONT.render('3', False, WHITE)
s4 = FONT.render('4', False, WHITE)
s5 = FONT.render('5', False, WHITE)
s6 = FONT.render('6', False, WHITE)
s7 = FONT.render('7', False, WHITE)
s8 = FONT.render('8', False, WHITE)
s9 = FONT.render('9', False, WHITE)
f1 = FONT.render('1', False, GRAY)
f2 = FONT.render('2', False, GRAY)
f3 = FONT.render('3', False, GRAY)
f4 = FONT.render('4', False, GRAY)
f5 = FONT.render('5', False, GRAY)
f6 = FONT.render('6', False, GRAY)
f7 = FONT.render('7', False, GRAY)
f8 = FONT.render('8', False, GRAY)
f9 = FONT.render('9', False, GRAY)
USER_NUMBERS = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
FIXED_NUMBERS = [f1,f2,f3,f4,f5,f6,f7,f8,f9]
SCREEN = pygame.display.set_mode((1024, 768))


def grid_to_usual(coord):
    return (coord // 3) * 24 + coord * 80


class Number:

    def __init__(self, number, gx, gy, fixed=False, selected=False):

        self.fixed = fixed
        self.selected = selected
        self.gx = gx
        self.gy = gy
        self.number = number
        self.x = grid_to_usual(self.gx)
        self.y = grid_to_usual(self.gy)
        if not fixed and self.number:
            self.surface = USER_NUMBERS[self.number - 1]
        elif self.number:
            self.surface = FIXED_NUMBERS[self.number - 1]
        else:
            self.surface = None
        if self.selected:
            self.bg_color = GREEN
        else:
            self.bg_color = BLACK


    def draw(self):
        pygame.draw.rect(SCREEN, self.bg_color, [self.x, self.y, 80, 80])
        if self.surface is not None:
            SCREEN.blit(self.surface, (self.x, self.y))


def main(difficulty):
    clock = pygame.time.Clock()
    diff_gen(difficulty)
    strs = utils.read_field('new_field.txt')
    objects = []
    for x in range(9):
        for y in range(9):
            elem = strs[x][y]
            if '1' <= elem <= '9':
                objects.append(Number(int(elem), x, y))
            else:
                objects.append(Number(None, x, y))
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit(0)
        clock.tick(60)
        for obj in objects:
            obj.draw()
        pygame.display.flip()

if __name__ == '__main__':
    main(1)