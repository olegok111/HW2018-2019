import pygame
from random import randint as randint
from math import pi as pi
from math import radians as rad
from math import sin as sin
from math import cos as cos
# to do: dying at bottom, monsters, bonuses
GRAY       = (128, 128, 128)
BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)
LIGHT_BLUE = (166, 202, 240)
GREEN      = ( 50, 200,  50)
YELLOW     = (200, 200,  50)
RED        = (200,  50,  50)
PURPLE     = (200,  50, 200)
DEEP_PURPLE = (120,  50, 120)
COLOR_GRADES = (BLACK, LIGHT_BLUE, GREEN, YELLOW, RED, PURPLE, DEEP_PURPLE)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


class Ball:

    def __init__(self):
        self.x1 = 380
        self.y1 = 280
        self.real_x1 = 380.0
        self.real_y1 = 280.0
        self.r = 10
        self.x2 = self.x1 + 2*self.r
        self.y2 = self.y1 + 2*self.r
        self.screen = screen
        self.hitbox = pygame.Rect((self.x1, self.y1), (self.x1 + 2*self.r, self.y1 + 2*self.r))
        self.angle = rad(randint(0, 359))
        self.alive = True
        self.score = 0

    def draw(self):
        pygame.draw.circle(self.screen, GRAY, (self.x1 + self.r, self.y1 + self.r), self.r)

    def overlaps(self, some_rect:pygame.Rect):
        if (some_rect.left <= self.x1 <= some_rect.right or some_rect.left <= self.x2 <= some_rect.right) \
                and self.y1 <= some_rect.bottom < self.y2:
            self.real_y1 = float(some_rect.bottom)
            self.param_update()
            return 'v'
        elif (some_rect.left <= self.x1 <= some_rect.right or some_rect.left <= self.x2 <= some_rect.right) \
                and self.y1 < some_rect.top <= self.y2:
            self.real_y1 = float(some_rect.top - 2*self.r)
            self.param_update()
            return 'v'
        elif (some_rect.top <= self.y1 <= some_rect.bottom or some_rect.top <= self.y2 <= some_rect.bottom) \
                and self.x1 <= some_rect.right < self.x2:
            self.real_x1 = float(some_rect.right - 2*self.r)
            self.param_update()
            return 'h'
        elif (some_rect.top <= self.y1 <= some_rect.bottom or some_rect.top <= self.y2 <= some_rect.bottom) \
                and self.x1 < some_rect.left <= self.x2:
            self.real_x1 = float(some_rect.left)
            self.param_update()
            return 'h'
        else:
            return None

    def reflect(self, side):
        if side == 'v':  # vertical reflection
            self.angle = (pi - self.angle) % (2*pi)
        elif side == 'h':  # horizontal reflection
            self.angle = 2*pi - self.angle
        else:
            pass

    def param_update(self):
        self.x1 = round(self.real_x1)
        self.y1 = round(self.real_y1)
        self.hitbox = pygame.Rect(self.x1, self.y1, self.x1 + 2 * self.r, self.y1 + 2 * self.r)
        self.x2 = self.x1 + 2 * self.r
        self.y2 = self.y1 + 2 * self.r

    def move(self):
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
            self.alive = False
        self.real_x1 += 5 * sin(self.angle)
        self.real_y1 += 5 * cos(self.angle)
        self.param_update()
        for rect in rects:
            reflect_value = self.overlaps(rect.hitbox)
            self.reflect(reflect_value)
            try:
                if reflect_value:
                    rect.ruin()
                    self.score += 5
            except AttributeError:
                pass
        self.draw()


class Paddle:

    def __init__(self):
        self.x1 = 0
        self.y1 = 500
        self.width = 120
        self.height = 25
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        self.hitbox = pygame.Rect(self.x1, self.y1, self.width, self.height)
        self.key_pressed_left = False
        self.key_pressed_right = False

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.hitbox)

    def param_update(self):
        self.hitbox = pygame.Rect(self.x1, self.y1, self.width, self.height)
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.key_pressed_left = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.key_pressed_right = True
                elif event.key == pygame.K_SPACE:
                    self.key_pressed_left = False
                    self.key_pressed_right = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.key_pressed_left = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.key_pressed_right = False
        if self.key_pressed_left:
            self.x1 -= 5
        if self.key_pressed_right:
            self.x1 += 5
        if self.x1 < 0:
            self.x1 = 0
        elif self.x1 + self.width > 800:
            self.x1 = 800 - self.width
        self.param_update()
        self.draw()


class Brick:

    def __init__(self, x1, y1, grade):
        self.x1 = x1
        self.y1 = y1
        self.width = 100
        self.height = 25
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        self.hitbox = pygame.Rect(self.x1, self.y1, self.width, self.height)
        self.color = COLOR_GRADES[grade]
        self.grade = grade

    def ruin(self):
        self.grade -= 1
        self.color = COLOR_GRADES[self.grade]
        if self.grade == 0:
            rects.remove(self)
        self.draw()

    def draw(self):
        pygame.draw.rect(screen, self.color, self.hitbox)


class Life:

    def __init__(self, index):
        self.index = index
        self.x1 = 770
        self.y1 = 570 - (self.index * 30)

    def draw(self):
        pygame.draw.rect(screen, RED, [self.x1, self.y1, 20, 20])


ball = Ball()
paddle = Paddle()
rects = [paddle]
for _x1 in range(0, 800, 100):
    for _y1 in range(50, 150, 25):
        b = Brick(_x1, _y1, 4)
        rects.append(b)
lives = []
for lvi in range(3):
    l = Life(lvi)
    lives.append(l)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if not lives:
        exit()
    clock.tick(60)
    screen.fill(BLACK)
    if not ball.alive:
        del ball
        ball = Ball()
        screen.fill(RED)
        lives.pop()
    for l in lives:
        l.draw()
    ball.move()
    paddle.move()
    for rct in rects:
        rct.draw()
    print(ball.score)
    pygame.display.flip()