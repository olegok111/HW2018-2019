import pygame

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
RED   = (255,000,000)
BLACK = (000,000,000)
GRAY  = (127,127,127)

class Ship:

    def __init__(self):
        self.x = 0
        self.y = 570
        self.width = 80
        self.height = 20

    def draw(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.width, self.height])

    def move(self, direction):
        if direction == 'l':
            self.x -= 5
            if self.x < 0:
                self.x = 0
        elif direction == 'r':
            self.x += 5
            if self.x + self.width > 1024:
                self.x = 1024 - self.width


class Bullet:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 2

    def draw(self):
        pygame.draw.circle(screen, GRAY, (self.x, self.y), self.r)

    def move(self):
        self.y -= 5


class Enemy:
    pass


class Bomb:
    pass

operation = True
ship = Ship()
unplayable_objects = []
while operation:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            operation = False
    clock.tick(60)
    screen.fill(BLACK)
    prsd = pygame.key.get_pressed()
    if prsd[pygame.K_LEFT]:
        ship.move('l')
    elif prsd[pygame.K_RIGHT]:
        ship.move('r')
    if prsd[pygame.K_SPACE]:
        unplayable_objects.append(Bullet(ship.x + (ship.width // 2), ship.y))
    ship.draw()
    for upo in unplayable_objects:
        upo.move()
        upo.draw()
    pygame.display.flip()