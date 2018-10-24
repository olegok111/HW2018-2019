import pygame
import random

screen = pygame.display.set_mode((800, 600))

RED   = (255,   0,   0)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)


def grid_to_coords(grid_x:int, grid_y:int):
    x1 = (grid_x - 1) * 40
    y1 = (grid_y - 1) * 40
    block_width = 40
    block_height = 40
    return x1, y1, block_width, block_height


class Snake:

    def __init__(self):
        self.head_x = 10
        self.head_y = 8
        self.direction = 'right'
        self.body = [(self.head_x, self.head_y)]
        self.score = 0
        self.lives = 3
        self.hold = False

    def respawn(self):
        global available_space
        available_space = [(i, j) for i in range(1, 21) for j in range(1, 16)]
        self.head_x = 10
        self.head_y = 8
        self.direction = 'right'
        self.body = [(self.head_x, self.head_y)]
        self.hold = True

    def head_update(self):
        self.head_x = self.body[-1][0]
        self.head_y = self.body[-1][1]

    def move(self):
        if not self.hold:
            future_head = ()
            if self.direction == 'right':
                future_head = (self.head_x+1, self.head_y)
            elif self.direction == 'down':
                future_head = (self.head_x, self.head_y+1)
            elif self.direction == 'left':
                future_head = (self.head_x-1, self.head_y)
            elif self.direction == 'up':
                future_head = (self.head_x, self.head_y-1)
            if future_head[0] == 21:
                future_head = (1, future_head[1])
            elif future_head[0] == 0:
                future_head = (20, future_head[1])
            if future_head[1] == 16:
                future_head = (future_head[0], 1)
            elif future_head[1] == 0:
                future_head = (future_head[0], 15)

            if future_head in self.body:
                self.lives -= 1
                self.respawn()
            else:
                available_space.remove(future_head)
                self.body.append(future_head)
                self.head_update()
                if future_head != (apple.x, apple.y):
                    available_space.append(self.body[0])
                    self.body.pop(0)
                else:
                    apple.respawn()
                    self.score += 1
        self.draw()

    def draw(self):
        for body_block in self.body:
            body_block_coords = grid_to_coords(body_block[0], body_block[1])
            pygame.draw.rect(screen, WHITE, [body_block_coords[i] for i in range(4)])
        head_coords = grid_to_coords(self.body[-1][0], self.body[-1][1])
        if self.direction == 'right':
            pygame.draw.polygon(screen, RED, [(head_coords[0]+8, head_coords[1]+8), (head_coords[0]+8, head_coords[1]+32), (head_coords[0]+32, head_coords[1]+20)])
        elif self.direction == 'down':
            pygame.draw.polygon(screen, RED, [(head_coords[0]+8, head_coords[1]+8), (head_coords[0]+32, head_coords[1]+8), (head_coords[0]+20, head_coords[1]+32)])
        elif self.direction == 'left':
            pygame.draw.polygon(screen, RED, [(head_coords[0]+32, head_coords[1]+8), (head_coords[0]+32, head_coords[1]+32), (head_coords[0]+8, head_coords[1]+20)])
        elif self.direction == 'up':
            pygame.draw.polygon(screen, RED, [(head_coords[0]+8, head_coords[1]+32), (head_coords[0]+32, head_coords[1]+32), (head_coords[0]+20, head_coords[1]+8)])


class Apple:

    def __init__(self):
        self.pos = random.choice(available_space)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.coords = grid_to_coords(self.x, self.y)

    def respawn(self):
        self.pos = random.choice(available_space)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.coords = grid_to_coords(self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, RED, [self.coords[i] for i in range(4)])


clock = pygame.time.Clock()
available_space = [(i, j) for i in range(1, 21) for j in range(1, 16)]
snake = Snake()
apple = Apple()
pygame.font.init()
my_font = pygame.font.SysFont('Tahoma', 26)
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != 'left':
                snake.direction = 'right'
            elif event.key == pygame.K_DOWN and snake.direction != 'up':
                snake.direction = 'down'
            elif event.key == pygame.K_LEFT and snake.direction != 'right':
                snake.direction = 'left'
            elif event.key == pygame.K_UP and snake.direction != 'down':
                snake.direction = 'up'
            elif event.key == pygame.K_ESCAPE:
                exit(0)
            elif event.key == pygame.K_RETURN:
                game_over = False
            snake.hold = False
    clock.tick(7)
    screen.fill(BLACK)
    if snake.lives == 0 or game_over:
        game_over = True
        game_over_ts = my_font.render('Game over. Press ENTER to restart game, ESC or EXIT to quit game.', False, GREEN)
        screen.blit(game_over_ts, (0, 250))
        snake.respawn()
        snake.lives = 3
    else:
        snake.move()
        apple.draw()
        score_text_surface = my_font.render('SCORE:' + str(snake.score), False, GREEN)
        lives_text_surface = my_font.render('LIVES:' + str(snake.lives), False, GREEN)
        screen.blit(score_text_surface, (20, 20))
        screen.blit(lives_text_surface, (20, 45))
    pygame.display.flip()
