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


def antipod(d):
    if d == 'l':
        return 'r'
    elif d == 'r':
        return 'l'
    elif d == 'u':
        return 'd'
    else:
        return 'u'


class Xonix:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.grid = (0,0)
        self.r = 10
        self.color = BLUE
        self.speed = 2
        self.direction = 'l'
        self.dirchg = False
        self.in_land = True
        self.fill_data = []
        self.line_begin = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def fill_area(self):
        for data_piece in self.fill_data:
            fill_direction = data_piece[2]
            grid_x = data_piece[0]
            grid_y = data_piece[1]
            while (grid_x, grid_y) not in land and (grid_x, grid_y) not in line:
                land.append((grid_x, grid_y))
                if fill_direction == 'l':
                    grid_x -= 1
                elif fill_direction == 'r':
                    grid_x += 1
                elif fill_direction == 'u':
                    grid_y -= 1
                else:
                    grid_y += 1

    def param_update(self):
        self.grid = to_grid(self.x, self.y)
        if self.line_begin:
            self.line_begin = False
        if self.grid not in land and self.in_land:
            self.line_begin = True
        self.in_land = self.grid in land

    def motion(self):
        global land, line, available_space
        prsd = pygame.key.get_pressed()
        self.param_update()
        if self.grid not in line:
            grd = self.grid[:]
            if self.line_begin:
                if self.direction in ('l', 'r'):
                    self.fill_data.append((self.grid[0], self.grid[1], 'u'))
                else:
                    self.fill_data.append((self.grid[0], self.grid[1], 'l'))
            else:
                if self.dirchg:
                    while grd not in land and grd not in line:
                        if self.direction == 'l':
                            grd = (grd[0]-1, grd[1])
                        elif self.direction == 'r':
                            grd = (grd[0]+1, grd[1])
                        elif self.direction == 'u':
                            grd = (grd[0], grd[1]-1)
                        else:
                            grd = (grd[0], grd[1]+1)
                        self.fill_data.append((grd[0], grd[1], self.fill_data[-1][2]))
                else:
                    try:
                        if self.fill_data[-1][2] == self.direction:
                            cur_fill_dir = antipod(self.fill_data[-1][2])
                            self.fill_data.append((self.grid[0], self.grid[1], cur_fill_dir))
                            for data_piece in self.fill_data:
                                if data_piece[2] == antipod(cur_fill_dir): # взаимоуничтожение лишних направлений
                                    if cur_fill_dir == 'l' and data_piece[1] == self.grid[1] and data_piece[0] < self.grid[0] or \
                                        cur_fill_dir == 'r' and data_piece[1] == self.grid[1] and data_piece[0] > self.grid[0] or \
                                        cur_fill_dir == 'u' and data_piece[0] == self.grid[0] and data_piece[1] > self.grid[1] or \
                                        cur_fill_dir == 'd' and data_piece[0] == self.grid[0] and data_piece[1] < self.grid[1]:
                                        self.fill_data.remove(data_piece)
                        else:
                            cur_fill_dir = self.fill_data[-1][2]
                            self.fill_data.append((self.grid[0], self.grid[1], cur_fill_dir))
                            for data_piece in self.fill_data:
                                if data_piece[2] == antipod(cur_fill_dir): # взаимоуничтожение лишних направлений
                                    if cur_fill_dir == 'l' and data_piece[1] == self.grid[1] and data_piece[0] < self.grid[0] or \
                                        cur_fill_dir == 'r' and data_piece[1] == self.grid[1] and data_piece[0] > self.grid[0] or \
                                        cur_fill_dir == 'u' and data_piece[0] == self.grid[0] and data_piece[1] > self.grid[1] or \
                                        cur_fill_dir == 'd' and data_piece[0] == self.grid[0] and data_piece[1] < self.grid[1]:
                                        self.fill_data.remove(data_piece)
                        print(cur_fill_dir)
                    except:
                        pass
            line.append(self.grid)
        if self.in_land:
            line = []
            self.fill_area()
            self.fill_data = []
            if prsd[pygame.K_RIGHT]:
                self.x += self.speed
            elif prsd[pygame.K_LEFT]:
                self.x -= self.speed
            elif prsd[pygame.K_DOWN]:
                self.y += self.speed
            elif prsd[pygame.K_UP]:
                self.y -= self.speed
        else:
            if self.dirchg:
                self.dirchg = False
            if prsd[pygame.K_RIGHT]:
                if self.direction != 'r':
                    self.dirchg = True
                self.direction = 'r'
            elif prsd[pygame.K_LEFT]:
                if self.direction != 'l':
                    self.dirchg = True
                self.direction = 'l'
            elif prsd[pygame.K_DOWN]:
                if self.direction != 'd':
                    self.dirchg = True
                self.direction = 'd'
            elif prsd[pygame.K_UP]:
                if self.direction != 'u':
                    self.dirchg = True
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
