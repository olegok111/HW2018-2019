import pygame

screen = pygame.display.set_mode((799, 799))
# grid : 25 * 25 (32 * 32 block)
# 1 block : 0 - 31
clock = pygame.time.Clock()

block_size = 32
YELLOW = (255,255,0)
BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (127,127,127)
RTRICOORDS = [(20, 16), (12, 12), (12, 20)]
LTRICOORDS = [(12, 16), (20, 12), (20, 20)]
UTRICOORDS = [(12, 20), (20, 20), (16, 12)]
DTRICOORDS = [(12, 12), (20, 12), (16, 20)]
OBST_BANK = [(j, i) for i in range(16, 800, 16) for j in (16, 784)] + \
            [(i, j) for i in range(16, 800, 16) for j in (16, 784)] + \
            [(i, j) for i in (176, 272) for j in range(48, 400, 32)] + \
            [(i, j) for i in (624, 528) for j in range(432, 800, 32)] + \
            [(i, 304) for i in range(304, 465, 32)] + [(i, 496) for i in range(496, 335, -32)]


def to_triag(cx, cy, r, coords):
    x = cx - r
    y = cy - r
    newc = []
    for crd in coords:
        newc.append((crd[0]+x, crd[1]+y))
    return newc


def grid_to_coord(grid_c):
    x = (grid_c - 1) * block_size
    return x


class Pacman:

    def __init__(self):
        self.cx = 400
        self.cy = 400
        self.r = 16
        self.color = YELLOW
        self.direction = ''
        self.movement = 4
        self.tri_coords = []
        self.hitbox = pygame.Rect(self.cx - self.r, self.cy - self.r, 2 * self.r, 2 * self.r)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.cx, self.cy), self.r)
        try:
            pygame.draw.polygon(screen, RED, self.tri_coords)
        except:
            pass

    def exist(self):
        self.move()

    def move(self):
        if self.direction == 'left':
            self.cx -= self.movement
        elif self.direction == 'right':
            self.cx += self.movement
        elif self.direction == 'up':
            self.cy -= self.movement
        elif self.direction == 'down':
            self.cy += self.movement
        for f in foods:
            if f.hitbox.colliderect(self.hitbox):
                foods.remove(f)


class Food:

    def __init__(self, x, y):
        self.cx = x
        self.cy = y
        self.r = 2
        self.color = GRAY
        self.hitbox = pygame.Rect(self.cx - self.r, self.cy - self.r, 2 * self.r, 2 * self.r)

    def exist(self):
        pass

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.cx, self.cy), self.r)


class Obstacle:

    def __init__(self, x, y):
        self.cx = x
        self.cy = y
        self.r = 16
        self.color = GRAY

    def exist(self):
        pass

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.cx - self.r, self.cy - self.r, 2 * self.r, 2 * self.r))


pac_man = Pacman()
objects = [pac_man]
obstacles = []
foods = []
for o in OBST_BANK:
    obstacles.append(Obstacle(o[0], o[1]))
for i in range(16, 800, 32):
    for j in range(16, 800, 32):
        if (i, j) not in OBST_BANK:
            foods.append(Food(i, j))
objects += obstacles + foods
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    prsd = pygame.key.get_pressed()
    if prsd[pygame.K_LEFT]:
        pac_man.direction = 'left'
        pac_man.tri_coords = to_triag(pac_man.cx, pac_man.cy, pac_man.r, LTRICOORDS)
    elif prsd[pygame.K_RIGHT]:
        pac_man.direction = 'right'
        pac_man.tri_coords = to_triag(pac_man.cx, pac_man.cy, pac_man.r, RTRICOORDS)
    elif prsd[pygame.K_UP]:
        pac_man.direction = 'up'
        pac_man.tri_coords = to_triag(pac_man.cx, pac_man.cy, pac_man.r, UTRICOORDS)
    elif prsd[pygame.K_DOWN]:
        pac_man.direction = 'down'
        pac_man.tri_coords = to_triag(pac_man.cx, pac_man.cy, pac_man.r, DTRICOORDS)
    else:
        pac_man.direction = ''
        pac_man.tri_coords = []
    if prsd[pygame.K_ESCAPE]:
        exit(0)
    clock.tick(60)
    screen.fill(BLACK)
    for obj in objects:
        obj.draw()
        obj.exist()
    pygame.display.flip()