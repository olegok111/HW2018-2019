import pygame
import utils as utils
from difficult_sudoku_gen import main as diff_gen

BLACK = (  0,  0,  0)
RED   = ( 70,  0,  0)
WHITE = (255,255,255)
GREEN = (  0, 70,  0)
GRAY  = (127,127,127)
LGREEN = (50, 180, 50)
LRED = (180, 50, 50)

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
CORRECT_SOLUTION_TEXT = FONT.render('Correct!', False, LGREEN)
WRONG_SOLUTION_TEXT = FONT.render('Wrong!', False, LRED)
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

    def exist(self):
        self.draw()
        if self.selected:
            self.bg_color = GREEN
        else:
            self.bg_color = BLACK
        if not self.fixed and self.number:
            self.surface = USER_NUMBERS[self.number - 1]
        elif self.number:
            self.surface = FIXED_NUMBERS[self.number - 1]
        else:
            self.surface = None


class Cursor:

    def __init__(self):
        self.gx = 0
        self.gy = 0
        self.x = grid_to_usual(self.gx)
        self.y = grid_to_usual(self.gy)
        self.color = (15, 20, 117)
        self.hold_count = 0
        self.number_pressed = False
        self.number = None

    def exist(self):
        prsd = pygame.key.get_pressed()
        if any(prsd):
            self.hold_count += 1
            if self.hold_count == 1 or self.hold_count > 25:
                if prsd[pygame.K_RIGHT] or prsd[pygame.K_d]:
                    self.gx += 1
                elif prsd[pygame.K_LEFT] or prsd[pygame.K_a]:
                    self.gx -= 1
                if prsd[pygame.K_DOWN] or prsd[pygame.K_s]:
                    self.gy += 1
                elif prsd[pygame.K_UP] or prsd[pygame.K_w]:
                    self.gy -= 1
                if not self.number_pressed:
                    if prsd[pygame.K_1]:
                        self.number = 1
                    elif prsd[pygame.K_2]:
                        self.number = 2
                    elif prsd[pygame.K_3]:
                        self.number = 3
                    elif prsd[pygame.K_4]:
                        self.number = 4
                    elif prsd[pygame.K_5]:
                        self.number = 5
                    elif prsd[pygame.K_6]:
                        self.number = 6
                    elif prsd[pygame.K_7]:
                        self.number = 7
                    elif prsd[pygame.K_8]:
                        self.number = 8
                    elif prsd[pygame.K_9]:
                        self.number = 9
                    elif prsd[pygame.K_DELETE] or prsd[pygame.K_0] or prsd[pygame.K_SPACE]:
                        self.number = 'd'
                    self.number_pressed = True
            self.gx %= 9
            self.gy %= 9
        else:
            self.number_pressed = False
            self.number = None
            if self.hold_count:
                self.hold_count = 0


def main(difficulty):
    clock = pygame.time.Clock()
    diff_gen(difficulty)
    strs = utils.read_field('new_field.txt')
    objects = []
    cur = Cursor()
    prev_sel = (0, 0)
    for x in range(9):
        row = []
        for y in range(9):
            elem = strs[x][y]
            if '1' <= elem <= '9':
                row.append(Number(int(elem), x, y, fixed=True))
            else:
                row.append(Number(None, x, y))
        objects.append(row)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                exit(0)
        clock.tick(20)
        cur.exist()
        objects[prev_sel[0]][prev_sel[1]].selected = False
        objects[cur.gx][cur.gy].selected = True
        #print(cur.number)
        if not objects[cur.gx][cur.gy].fixed and cur.number_pressed and cur.number:
            if cur.number == 'd':
                objects[cur.gx][cur.gy].number = None
            else:
                objects[cur.gx][cur.gy].number = cur.number
        prev_sel = (cur.gx, cur.gy)
        for row in objects:
            for obj in row:
                obj.exist()
        pygame.display.flip()


if __name__ == '__main__':
    main(1)
