import pygame
import random

DARK_LEAF   = (163,  56,  10)
MID_LEAF    = (212,  72,  13)
BRIGHT_LEAF = (242,  96,  34)
GOLD        = (255, 200,   0)
WHITE       = (255, 255, 255)
COLORS = (DARK_LEAF, MID_LEAF, BRIGHT_LEAF, GOLD)
G = 10
leaves = []

class Leaf():

    def __init__(self, x1, y1, color, screen):
        self.x1 = x1
        self.y1 = y1
        self.surface = screen
        self.width = 20
        self.height = 10
        self.age = 0
        self.color = color
        self.falling = True
        self.x2 = self.x1 + self.width

    def draw(self):
        x2 = self.x1 + self.width
        y2 = self.y1 + self.height
        pygame.draw.polygon(self.surface, self.color, [(self.x1, self.y1), (self.x1, y2), (x2, y2), (x2, self.y1)])

    def fall(self):
        if self.falling:
            self.y1 += G * self.age * self.age / 2
            y2 = self.y1 + self.width
            #self.x1 += wind
            if y2 >= 600:
                self.y1 = 600 - self.height
                self.falling = False
            for lf in leaves:
                if lf != self and y2 >= lf.y1 and (lf.x1 <= self.x1 <= lf.x2 or lf.x1 <= self.x2 <= lf.x2):
                    self.y1 = lf.y1 - self.height
                    self.falling = False
            self.age += 0.01


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
operation = True
block_ticks = 0
prev_pos = 0
#wind = 0

while operation:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            operation = False
        '''
        elif event.type == pygame.KEYUP:
            wind += 5
        elif event.type == pygame.KEYDOWN:
            wind -= 5
        '''
    clock.tick(60)
    block_ticks += 1
    if block_ticks == 60:
        block_ticks = 0
        if len(leaves) < 100:
            new_leaf = Leaf(random.randint(0, 780), 0, random.choice(COLORS), screen)
            leaves.append(new_leaf)
    screen.fill(WHITE)
    #print(wind)
    for lf in leaves:
        lf.fall()
        lf.draw()
        if lf.y1 < 0:
            leaves.remove(lf)
    pygame.display.flip()