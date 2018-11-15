import pygame

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
operation = True
BLUE  = (  0,  0,255)
BLACK = (  0,  0,  0)


class Xonix:

    def __init__(self):

        self.x = 512
        self.y = 364
        self.r = 10
        self.color = BLUE
        self.speed = 2

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def motion(self):
        prsd = pygame.key.get_pressed()
        if prsd[pygame.K_RIGHT]:
            self.x += self.speed
        elif prsd[pygame.K_LEFT]:
            self.x -= self.speed
        elif prsd[pygame.K_DOWN]:
            self.y += self.speed
        elif prsd[pygame.K_UP]:
            self.y -= self.speed
        self.draw()

xnx = Xonix()

while operation:
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            operation = False
            break
    clock.tick(60)
    screen.fill(BLACK)
    xnx.draw()
    xnx.motion()
    pygame.display.flip()