import pygame

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
operation = True
BLUE   = (  0,  0,255)
BLACK  = (  0,  0,  0)
GRAY   = (127,127,127)
LGRAY  = (200,200,200)

def to_grid(x, y):
    grid_x = x//10
    grid_y = y//10
    return grid_x, grid_y

def to_normal(grid_x, grid_y):
    x = grid_x * 10
    y = grid_y * 10
    return x, y

def fill_area(xnx, brd, side='l'):
    for block in brd:
        while block not in land:
            try:
                if block[0] > xnx.right_extremum:
                    break
            except Exception as e:
                print(e)
            land.append(block)
            block_normal = to_normal(block[0], block[1])
            pygame.draw.rect(screen, GRAY, [block_normal[0], block_normal[1], 10, 10])
            if side == 'l':
                block = (block[0] + 1, block[1])
            elif side == 'd':
                block = (block[0], block[1] - 1)

class Xonix:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.grid = (0,0)
        self.r = 10
        self.color = BLUE
        self.speed = 2
        self.direction = 'l'
        self.in_land = True
        self.newfoundland = False
        self.left_border = []
        self.down_border = []
        self.right_extremum = None

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def param_update(self):
        self.grid = to_grid(self.x, self.y)
        if not self.in_land and self.grid in land:
            self.newfoundland = True
            self.in_land = True
        else:
            if self.newfoundland:
                self.newfoundland = False
                self.right_extremum = None
            self.in_land = self.grid in land

    def motion(self):
        global land, line, available_space
        prsd = pygame.key.get_pressed()
        self.param_update()
        if self.grid not in line:
            if self.direction == 'l' or self.direction == 'r':
                '''
                count = 1
                check_grid = self.grid
                while True:
                    if check_grid in land or check_grid in line:
                        break
                    check_grid = (check_grid[0], check_grid[1]-1)
                    count += 1
                line.append((self.grid[0], self.grid[1], 'u', count))'''
            line.append(self.grid)

        if self.newfoundland:
            fill_area(self, self.left_border)
            fill_area(self, self.down_border, side='d')
            print(self.left_border)
            print(self.down_border)

        if self.in_land:
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
                self.down_border.append(self.grid)
            elif self.direction == 'l':
                self.x -= self.speed
                self.down_border.append(self.grid)
            elif self.direction == 'd':
                self.y += self.speed
                self.left_border.append(self.grid)
                try:
                    if self.right_extremum == None:
                        self.right_extremum = self.grid[0]
                    elif self.right_extremum < self.grid[0]:
                        self.right_extremum = self.grid[0]
                except Exception as e:
                    print(e)
            elif self.direction == 'u':
                self.y -= self.speed
                self.left_border.append(self.grid)
                try:
                    if self.right_extremum == None:
                        self.right_extremum = self.grid[0]
                    elif self.right_extremum < self.grid[0]:
                        self.right_extremum = self.grid[0]
                except Exception as e:
                    print(e)
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
