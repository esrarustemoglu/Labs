import pygame
import random

pygame.init()

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

WIDTH = 600
HEIGHT = 600
CELL = 30
FPS = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Verdana", 20)

score = 0
level = 1


def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        global running
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x < 0 or self.body[0].x >= WIDTH // CELL or self.body[0].y < 0 or self.body[0].y >= HEIGHT // CELL:
            running = False

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, foods):
        global score, level, FPS
        head = self.body[0]

        for food in foods[:]:  # iterate over copy
            if head.x == food.pos.x and head.y == food.pos.y:
                if food.type == 'normal':
                    score += 1
                    self.body.append(Point(head.x, head.y))
                elif food.type == 'bonus':
                    score += 3
                    self.body.append(Point(head.x, head.y))
                    self.body.append(Point(head.x, head.y))
                elif food.type == 'poison':
                    score = max(0, score - 2)
                    if len(self.body) > 1:
                        self.body.pop()
                foods.remove(food)

                if score % 3 == 0 and score != 0:
                    level += 1
                    FPS += 1

class Food:
    def __init__(self, snake):
        self.generate_random_pos(snake)
        self.timer = pygame.time.get_ticks()
        self.lifetime = random.randint(3000, 7000)  # 3 to 7 seconds
        self.type = random.choice(['normal', 'bonus', 'poison'])

    def draw(self):
        color = {
            'normal': colorGREEN,
            'bonus': colorBLUE,
            'poison': colorRED
        }[self.type]
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake):
        while True:
            new_x = random.randint(0, WIDTH // CELL - 1)
            new_y = random.randint(0, HEIGHT // CELL - 1)
            if not any(segment.x == new_x and segment.y == new_y for segment in snake.body):
                self.pos = Point(new_x, new_y)
                break

    def is_expired(self):
        return pygame.time.get_ticks() - self.timer > self.lifetime


clock = pygame.time.Clock()
snake = Snake()
foods = []

spawn_delay = 2000  
last_spawn_time = pygame.time.get_ticks()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)
    draw_grid()
    draw_grid_chess()

    snake.move()

    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > spawn_delay:
        foods.append(Food(snake))
        last_spawn_time = current_time

    foods = [food for food in foods if not food.is_expired()]

    snake.check_collision(foods)

    snake.draw()
    for food in foods:
        food.draw()

    score_surf = font.render(f"Score: {score}  Level: {level}", True, colorBLACK)
    screen.blit(score_surf, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
