import pygame
import random

h = 600  # height of playable screen
w = 600  # width of playable screen
wi = 10  # width of block
he = 10  # height of block
v = 10  # speed

LEVEL_CHANGE_RATE = 10
OBST_BANK_0 = [(i, j) for i in range(0, w, wi) for j in (290, 300)]
OBST_BANK_1 = [(i, j) for i in range(0, w, wi) for j in (290, 300)] + \
              [(i, j) for i in (290, 300) for j in range(0, 290, he)] + \
              [(i, j) for i in (290, 300) for j in range(310, 600, he)]
OBST_BANK_2 = [(i, j) for i in (140,150,290,300,440,450) for j in range(0, h, he)]

fieldw = [i for i in range(0, w, wi)]  # field by width
fieldh = [i for i in range(0, h, he)]  # field by height

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DBLUE = (0, 0, 200)
GREEN = (0, 200, 0)
LGREEN = (230, 255, 230)
RED = (255, 0, 0)


class Body:

    def __init__(self, x, y, w, h, color, v):
        self.x = x
        self.y = y
        self.w = w  # width
        self.h = h  # height
        self.color = color
        self.v = v  # speed

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h], 0)

    def move(self, bod, n):
        bod[n].x = bod[n - 1].x
        bod[n].y = bod[n - 1].y


class Head(Body):

    def mov(self, w, h, nap, bod, obstacles):
        global ad, done, food, lives, dead
        for i in bod:
            if nap == "u":
                if self.y - self.v == i.y and self.x == i.x:
                    lives -= 1
                    if lives == 0:
                        done = True
                    else:
                        body_generate()
                    break
            elif nap == "d":
                if self.y + self.v == i.y and self.x == i.x:
                    lives -= 1
                    if lives == 0:
                        done = True
                    else:
                        body_generate()
                    break
            elif nap == "l":
                if self.x - self.v == i.x and self.y == i.y:
                    lives -= 1
                    if lives == 0:
                        done = True
                    else:
                        body_generate()
                    break
            elif nap == "r":
                if self.x + self.v == i.x and self.y == i.y:
                    lives -= 1
                    if lives == 0:
                        done = True
                    else:
                        body_generate()
                    break
        if (nap == "u" and (self.x, self.y - self.v) in obstacles) or (nap == "d" and (self.x, self.y + self.v) in obstacles) \
                or (nap == "l" and (self.x - self.v, self.y) in obstacles) or (nap == "r" and (self.x + self.v, self.y) in obstacles):
            lives -= 1
            if lives == 0:
                done = True
            else:
                body_generate()
        if not done:
            if nap == "u":
                if self.y - self.v < 0:
                    self.y = h - self.h
                else:
                    self.y -= self.v
            elif nap == "d":
                if self.y + self.v >= h:
                    self.y = 0
                else:
                    self.y += self.v
            elif nap == "l":
                if self.x - self.v < 0:
                    self.x = w - self.w
                else:
                    self.x -= self.v
            elif nap == "r":
                if self.x + self.v >= w:
                    self.x = 0
                else:
                    self.x += self.v
            if self.x == food.x and self.y == food.y:
                food = None
                ad = True
        self.draw()


class Ball:

    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.w, self.h], 0)


def body_generate():
    global bod, nap
    bod = []
    x = random.choice(fieldw)
    y = random.choice(fieldh)
    bod.append(Head(x, y, wi, he, BLACK, v))
    for i in range(10, 21, 10):
        bod.append(Body(x, y + i, wi, he, BLACK, v))
    nap = "r"


def stats_reset():
    global fps, score, level, food_count, level_changed, lives
    fps = 10
    score = 0
    level = 1
    food_count = 0
    level_changed = False
    lives = 3

size = [w + 100, h + 100]
screen = pygame.display.set_mode(size)
pygame.display.set_mode(size)
pygame.display.set_caption("Press Space to start")
clock = pygame.time.Clock()
operation = True
pygame.font.init()
my_font = pygame.font.SysFont('Tahoma', 26)

while operation:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            operation = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        obstacles = OBST_BANK_0
        next_obstacles = OBST_BANK_1
        done = False
        food = None
        body_generate()
        stats_reset()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True

            ad = False
            if food == None:
                a = random.choice(fieldw)
                b = random.choice(fieldh)
                food_position_illegal = True
                while food_position_illegal:  # choosing food location
                    if a == bod[0].x and b == bod[0].y or (a, b) in obstacles:
                        a = random.choice(fieldw)
                        b = random.choice(fieldh)
                    else:
                        food_position_illegal = False
                food = (Ball(a, b, wi, he, RED))

            screen.fill(WHITE)
            pygame.draw.line(screen, BLACK, [w, 0], [w, h], 1)
            pygame.draw.line(screen, BLACK, [0, h], [w, h], 1)  # drawing borders
            food.draw()

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT] and nap != "r":
                nap = "l"
            elif pressed[pygame.K_RIGHT] and nap != "l":
                nap = "r"
            elif pressed[pygame.K_UP] and nap != "d":
                nap = "u"
            elif pressed[pygame.K_DOWN] and nap != "u":
                nap = "d"
            elif pressed[pygame.K_KP_PLUS]:  # only for debug! This should be deleted in release.
                score += level
                food_count += 1
                level_changed = False

            predx = bod[len(bod) - 1].x
            predy = bod[len(bod) - 1].y

            for i in range(len(bod) - 1, 0, -1):
                bod[i].move(bod, i)

            bod[0].mov(w, h, nap, bod, obstacles)

            if ad:
                bod.append(Body(predx, predy, wi, he, BLACK, v))
                fps += 1
                score += level
                food_count += 1
                level_changed = False
            if food_count % LEVEL_CHANGE_RATE == 0 and food_count != 0 and not level_changed:
                level += 1
                fps = 10
                level_changed = True
                obstacles = next_obstacles
                if level == 2:
                    next_obstacles = OBST_BANK_2

            for n_obst in next_obstacles:
                pygame.draw.rect(screen, GREEN, [n_obst[0]+4, n_obst[1]+4, 2, 2])
            for obst in obstacles:
                pygame.draw.rect(screen, GREEN, [obst[0], obst[1], wi, he])
            for bod_block in bod:
                bod_block.draw()

            level_text_surface = my_font.render('LEVEL:' + str(level), False, DBLUE)
            score_text_surface = my_font.render('SCORE:' + str(score), False, DBLUE)
            lives_text_surface = my_font.render('LIVES:' + str(lives), False, RED)
            screen.blit(level_text_surface, (20, 620))
            screen.blit(score_text_surface, (170, 620))
            screen.blit(lives_text_surface, (320, 620))
            clock.tick(fps)
            pygame.display.flip()
    screen.fill(BLACK)
    pygame.display.flip()
pygame.quit()
