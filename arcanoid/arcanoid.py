import pygame
from random import randint as randint
from math import pi as pi
from math import radians as rad
from math import sin as sin
from math import cos as cos

GRAY  = (128, 128, 128)
BLACK = (  0,   0,   0)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


class Ball:

    def __init__(self):
        self.x1 = 380
        self.y1 = 280
        self.real_x1 = 380.0
        self.real_y1 = 280.0
        self.r = 10
        self.screen = screen
        self.hitbox = pygame.Rect((self.x1, self.y1), (self.x1 + 2*self.r, self.y1 + 2*self.r))
        self.angle = rad(randint(0, 359))

    def draw(self):
        pygame.draw.circle(self.screen, GRAY, (self.x1 + self.r, self.y1 + self.r), self.r)

    def overlaps(self, some_rect):
        return self.hitbox.colliderect(some_rect)

    def reflect(self, side):
        if side == 'v':  # vertical reflection
            self.angle = (pi - self.angle) % (2*pi)
        elif side == 'h':  # horizontal reflection
            self.angle = 2*pi - self.angle

    def move(self):
        self.real_x1 += 5 * sin(self.angle)
        self.real_y1 += 5 * cos(self.angle)
        self.x1 = round(self.real_x1)
        self.y1 = round(self.real_y1)
        self.hitbox = pygame.Rect((self.x1, self.y1), (self.x1 + 2 * self.r, self.y1 + 2 * self.r))
        if self.x1 < 0:
            self.x1 = 0
            self.reflect('h')
        elif self.x1 + 2*self.r > 800:
            self.x1 = 800 - 2*self.r
            self.reflect('h')
        if self.y1 < 0:
            self.y1 = 0
            self.reflect('v')
        elif self.y1 + 2*self.r > 600:
            self.y1 = 600 - 2*self.r
            self.reflect('v')

ball = Ball()
#screen.fill(BLACK)
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
    clock.tick(60)
    screen.fill(BLACK)
    ball.move()
    ball.draw()
    pygame.display.flip()
