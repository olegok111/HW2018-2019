import pygame
from random import randint as randint
from math import pi as pi
from math import radians as rad
from math import sin as sin
from math import cos as cos
import socket

VIOLET = (100,  0,100)
ORANGE = (255,165,  0)
BLACK  = (  0,  0,  0)
ASPRGS = (123,160, 91)
SCR_WIDTH = 800
SCR_HEIGHT = 600
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
clock = pygame.time.Clock()
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))


class Paddle:

    def __init__(self, player:int=1):
        if player == 1:
            self.x1 = 20
            self.color = VIOLET
            self.mode = 'keyboard'
        elif player == 2:
            self.x1 = 760
            self.color = ORANGE
            self.mode = 'internet'
        self.y1 = 250
        self.width = 20
        self.height = 100
        self.movement = 5
        self.hitbox = pygame.Rect(self.x1, self.y1, self.width, self.height)

    def param_update(self):
        self.hitbox = pygame.Rect(self.x1, self.y1, self.width, self.height)

    def motion(self):
        global ball_angle
        prsd = pygame.key.get_pressed()
        if self.mode == 'keyboard':
            if prsd[pygame.K_DOWN] and prsd[pygame.K_UP]:
                client_sock.sendall(b'0')
            elif prsd[pygame.K_DOWN]:
                self.y1 += self.movement
                client_sock.sendall(b'd')
            elif prsd[pygame.K_UP]:
                self.y1 -= self.movement
                client_sock.sendall(b'u')
            else:
                client_sock.sendall(b'0')
        elif self.mode == 'internet':
            data = client_sock.recv(1024)
            if data == b'u':
                self.y1 -= self.movement
            elif data == b'd':
                self.y1 += self.movement
        if self.y1 < 0:
            self.y1 += self.movement
        elif self.y1 + self.height > SCR_HEIGHT:
            self.y1 -= self.movement
        self.param_update()

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x1, self.y1, self.width, self.height])


class Ball:

    def __init__(self):
        self.x1 = 380
        self.y1 = 280
        self.real_x1 = 380.0
        self.real_y1 = 280.0
        self.r = 10
        self.x2 = self.x1 + 2*self.r
        self.y2 = self.y1 + 2*self.r
        self.hitbox = pygame.Rect((self.x1, self.y1), (self.x1 + 2*self.r, self.y1 + 2*self.r))
        self.angle = rad(randint(0, 359))
        self.goal = ''
        self.l_score = 0
        self.r_score = 0

    def draw(self):
        pygame.draw.circle(screen, ASPRGS, (self.x1 + self.r, self.y1 + self.r), self.r)

    def reflect(self, side:str):
        if side == 'v':  # vertical reflection
            self.angle = (pi - self.angle) % (2*pi)
        elif side == 'h':  # horizontal reflection
            self.angle = 2*pi - self.angle

    def overlaps(self, some_rect:pygame.Rect):
        if (some_rect.left <= self.x1 <= some_rect.right or some_rect.left <= self.x2 <= some_rect.right) \
                and self.y1 < some_rect.bottom <= self.y2:
            self.real_y1 = float(some_rect.bottom)
            self.param_update()
            return 'v'
        elif (some_rect.left <= self.x1 <= some_rect.right or some_rect.left <= self.x2 <= some_rect.right) \
                and self.y1 <= some_rect.top < self.y2:
            self.real_y1 = float(some_rect.top - 2*self.r)
            self.param_update()
            return 'v'
        elif (some_rect.top <= self.y1 <= some_rect.bottom or some_rect.top <= self.y2 <= some_rect.bottom) \
                and some_rect.left <= self.x1 < some_rect.right:
            self.real_x1 = float(some_rect.right)
            self.param_update()
            return 'h'
        elif (some_rect.top <= self.y1 <= some_rect.bottom or some_rect.top <= self.y2 <= some_rect.bottom) \
                and some_rect.left < self.x2 <= some_rect.right:
            self.real_x1 = float(some_rect.left - 2*self.r)
            self.param_update()
            return 'h'
        else:
            return None

    def param_update(self):
        self.x1 = round(self.real_x1)
        self.y1 = round(self.real_y1)
        self.hitbox = pygame.Rect(self.x1, self.y1, self.x1 + 2 * self.r, self.y1 + 2 * self.r)
        self.x2 = self.x1 + 2 * self.r
        self.y2 = self.y1 + 2 * self.r

    def motion(self):
        if self.x1 < 0:
            self.goal = 'left'
        elif self.x1 + 2*self.r > SCR_WIDTH:
            self.goal = 'right'
        if self.y1 < 0:
            self.y1 = 0
            self.reflect('v')
        elif self.y1 + 2*self.r > SCR_HEIGHT:
            self.y1 = SCR_HEIGHT - 2*self.r
            self.reflect('v')
        self.real_x1 += 5 * sin(self.angle)
        self.real_y1 += 5 * cos(self.angle)
        self.param_update()
        for rect in rects:
            reflect_value = self.overlaps(rect.hitbox)
            self.reflect(reflect_value)
        #print(self.x1, self.x2, self.y1, self.y2)

def regen_ball():
    global ball
    del ball
    ball = Ball()
    ba = 'b' + str(ball.angle)
    client_sock.sendall(bytes(ba, 'utf8'))
    objects.append(ball)

pdl = Paddle()
pdl2 = Paddle(2)
ball = Ball()
cmd = ''
while cmd != b's':
    client_sock.sendall(b's')
    cmd = client_sock.recv(1024)
ba = 'b' + str(ball.angle)
client_sock.sendall(bytes(ba, 'utf8'))
objects = [pdl, pdl2, ball]
rects = [pdl, pdl2]
score_left = 0
score_right = 0
pygame.font.init()
my_font = pygame.font.SysFont('Tahoma', 26)
pygame.display.set_caption('Internet Pong v1.0 (player one)')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()
    clock.tick(60)
    screen.fill(BLACK)
    for obj in objects:
        obj.motion()
        obj.draw()
    if ball.goal == 'left':
        score_right += 1
        regen_ball()
    elif ball.goal == 'right':
        score_left += 1
        regen_ball()
    score_left_surface = my_font.render(str(score_left), False, VIOLET)
    score_right_surface = my_font.render(str(score_right), False, ORANGE)
    screen.blit(score_left_surface, (360, 20))
    screen.blit(score_right_surface, (440, 20))
    pygame.display.flip()
    if score_left == 5:
        print('Player one wins! That\'s me!')
        exit()
    elif score_right == 5:
        print('Player two wins! That\'s not me...')
        exit()