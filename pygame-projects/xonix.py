import pygame

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
operation = True
BLUE  = (  0,  0,255)
BLACK = (  0,  0,  0)
GRAY  = (127,127,127)
LGRAY = (200,200,200)

def to_grid(x, y):
    grid_x = x//10
    grid_y = y//10
    return grid_x, grid_y

def to_normal(grid_x, grid_y):
    x = grid_x * 10
    y = grid_y * 10
    return x, y

class Xonix:

    def __init__(self):

        self.x = 400
        self.y = 300
        self.grid = (40,30)
        self.r = 10
        self.color = BLUE
        self.speed = 2
        self.direction = 'l'
        self.in_land = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def param_update(self):
        self.grid = to_grid(self.x, self.y)
        self.in_land = self.grid in land

    def motion(self):
        global land, line
        prsd = pygame.key.get_pressed()
        self.param_update()
        if self.grid not in line:
            line.append(self.grid)
        if self.in_land:
            land.extend(line)
            line = []
            if prsd[pygame.K_RIGHT]:
                self.x += self.speed
            elif prsd[pygame.K_LEFT]:
                self.x -= self.speed
            elif prsd[pygame.K_DOWN]:
                self.y += self.speed
            elif prsd[pygame.K_UP]:
                self.y -= self.speed
        else:
            if prsd[pygame.K_RIGHT]:
                self.direction = 'r'
            elif prsd[pygame.K_LEFT]:
                self.direction = 'l'
            elif prsd[pygame.K_DOWN]:
                self.direction = 'd'
            elif prsd[pygame.K_UP]:
                self.direction = 'u'
            if self.direction == 'r':
                self.x += self.speed
            elif self.direction == 'l':
                self.x -= self.speed
            elif self.direction == 'd':
                self.y += self.speed
            elif self.direction == 'u':
                self.y -= self.speed
        self.draw()

xnx = Xonix()
land = [(i,j) for i in range(80) for j in (0,1,58,59)] + [(i,j) for i in (0,1,78,79) for j in range(60)]
line = []
while operation:
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            operation = False
            break
    clock.tick(60)
    screen.fill(BLACK)
    for l in land:
        l = to_normal(l[0], l[1])
        pygame.draw.rect(screen, GRAY, [l[0], l[1], 10, 10])
    for l in line:
        l = to_normal(l[0], l[1])
        pygame.draw.rect(screen, LGRAY, [l[0], l[1], 10, 10])
    xnx.draw()
    xnx.motion()
    pygame.display.flip()
