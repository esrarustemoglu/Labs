import pygame
import sys
from random import randint

pygame.init()

Black = pygame.Color(0, 0, 0)
White = pygame.Color(255, 255, 255)
Grey = pygame.Color(128, 128, 128)
Red = pygame.Color(255, 0, 0)
Blue = pygame.Color(0, 0, 255)
Green = pygame.Color(0, 255, 0)
Yellow = (255, 255, 0)

Width = 600
Height = 600

DISPLAYSURF = pygame.display.set_mode((Width, Height))

Cell = 30

def draw_grid():
    for i in range(Height -3  // Cell):
        for j in range(Width - 3 // Cell ):
            pygame.draw.rect(DISPLAYSURF, Grey, (i * Cell , j * Cell , Cell , Cell ), 1)

def draw_grid_chess():
    colors = [White, Grey]
    for i in range(Height - 3 // Cell ):
        for j in range(Width - 3 // Cell):
            pygame.draw.rect(DISPLAYSURF, colors[(i + j) % 2], (i * Cell , j * Cell , Cell , Cell ))


def draw_borders():
    pygame.draw.rect(DISPLAYSURF, Red, (0, 0, 3, Height))  # Left border (filled)
    pygame.draw.rect(DISPLAYSURF, Red, (Width - 3, 0, 3, Height))  # Right border (filled)
    pygame.draw.rect(DISPLAYSURF, Red, (0, 0, Width, 3))  # Top border (filled)
    pygame.draw.rect(DISPLAYSURF, Red, (0, Height - 3, Width, 3))  # Bottom border (filled)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # checks the right border
        if self.body[0].x > Width // Cell - 1:
            self.body[0].x = 0
        # checks the left border
        if self.body[0].x < 0:
            self.body[0].x = Width // Cell - 1
        # checks the bottom border
        if self.body[0].y > Height // Cell - 1:
            self.body[0].y = 0
        # checks the top border
        if self.body[0].y < 0:
            self.body[0].y = Height // Cell - 1


    def draw(self):
        head = self.body[0]
        pygame.draw.rect(DISPLAYSURF, Red, (head.x * Cell, head.y * Cell, Cell, Cell))
        for segment in self.body[1:]:
            pygame.draw.rect(DISPLAYSURF, Yellow, (segment.x * Cell, segment.y * Cell, Cell, Cell))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos()

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, Green , (self.pos.x * Cell , self.pos.y * Cell , Cell , Cell))

    def generate_random_pos(self):
        self.pos.x = randint(0, Width // Cell - 1)
        self.pos.y = randint(0, Height // Cell - 1)


FPS = 5
clock = pygame.time.Clock()

food = Food()
snake = Snake()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    DISPLAYSURF.fill(Black)
    
    draw_grid()
    draw_grid_chess()
    draw_borders()
    
    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
