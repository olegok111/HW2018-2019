import pygame
import random


h = 600  # height
w = 600  # width
wi = 10  # width
he = wi  # height
v = 10  # speed
fps = 10
score = 0
level = 1

fieldw = [(i) for i in range(0, w, wi)]  # field by width
fieldh = [(i) for i in range(0, h, he)]  # field by height

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
DBLUE = (  0,   0, 200)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
colors = []
for i in range(256):
    colors.append((i,0,0))  # colors from black to full-red (why?)


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
        bod[n].x = bod[n-1].x
        bod[n].y = bod[n-1].y


class Head(Body):
    
    def mov(self, w, h, nap, food_queue, bod):
        global ad, done
        for i in bod:
            if nap == "u":
                if self.y - self.v == i.y and self.x == i.x:
                    done = True
                    break
            elif nap == "d":
                if self.y + self.v == i.y and self.x == i.x:
                    done = True
                    break
            elif nap == "l":
                if self.x - self.v == i.x and self.y == i.y:
                    done = True
                    break
            elif nap == "r":
                if self.x + self.v == i.x and self.y == i.y:
                    done = True
                    break
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
            if self.x == food_queue[0].x and self.y == food_queue[0].y:
                food_queue.pop(0)  # deleting the first element of Food Queue(TM)
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


size = [w+100, h+100]
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
        bod = []
        food_queue = []  # initialization of Food Queue(TM)
        nap = "u"  # direction = "up"
        done = False
        x = random.choice(fieldw)
        y = random.choice(fieldh)    
        bod.append(Head(x, y, wi, he, BLACK, v))
        for i in range(10, 31, 10):
            bod.append(Body(x, y+i, wi, he, BLACK, v))        
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True

            ad = False
            if len(food_queue) == 0:
                a = random.choice(fieldw)
                b = random.choice(fieldh)
                flag = True
                while flag:  # choosing food location
                    for i in bod:
                        if a == i.x and b == i.y:
                            a = random.choice(fieldw)
                            b = random.choice(fieldh)
                            break
                        else:
                            flag = False
                            break
                food_queue.append(Ball(a, b, wi, he, RED))  # adding to Food Queue(TM)
            
            screen.fill(WHITE)
            pygame.draw.line(screen, BLACK, [w, 0], [w, h], 1)
            pygame.draw.line(screen, BLACK, [0, h], [w, h], 1)  # drawing borders
            food_queue[0].draw()  # drawing the first element of Food Queue(TM)
            
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT] and nap != "r":
                nap = "l"
            elif pressed[pygame.K_RIGHT] and nap != "l":
                nap = "r"
            elif pressed[pygame.K_UP] and nap != "d":
                nap = "u"
            elif pressed[pygame.K_DOWN] and nap != "u":
                nap = "d"
            
            predx = bod[len(bod)-1].x
            predy = bod[len(bod)-1].y
            
            for i in range(len(bod)-1, 0, -1):
                bod[i].move(bod, i)
                
            bod[0].mov(w, h, nap, food_queue, bod)
            
            if ad:
                bod.append(Body(predx, predy, wi, he, BLACK, v))
                fps += 1
                
            for i in range(0, len(bod)):
                bod[i].draw()    

            level_text_surface = my_font.render('LEVEL:' + str(level), False, DBLUE)
            score_text_surface = my_font.render('SCORE:' + str(score), False, DBLUE)
            screen.blit(level_text_surface, (20, 20))
            screen.blit(score_text_surface, (20, 45))
            clock.tick(fps)
            pygame.display.flip()
    screen.fill(BLACK)
    pygame.display.flip()
pygame.quit()
