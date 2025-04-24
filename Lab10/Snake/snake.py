import pygame
import random
import time
import psycopg2

conn = psycopg2.connect( 
    host="localhost",
    database="postgres",
    user="postgres",
    password="4511"
)
def add_user(conn, username):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO \"user\" (username) VALUES (%s) RETURNING id;", (username,))
        user_id = cursor.fetchone()[0]
        conn.commit()
    return user_id


def get_user_score(conn, user_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT score, level FROM user_score WHERE user_id = %s;", (user_id,))
        result = cursor.fetchone()
        if result:
            return result
        else:
            return 0, 1  

def save_user_score(conn, user_id, score, level):
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO user_score (user_id, score, level)
            VALUES (%s, %s, %s)
            ON CONFLICT (user_id) 
            DO UPDATE SET score = EXCLUDED.score, level = EXCLUDED.level;
        """, (user_id, score, level))
        conn.commit()

pygame.init()

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)
colorORANGE = (255, 165, 0)
colorBROWN = (150, 75, 0)
colorPINK = (255, 105, 180)
colorVIOLET =(134, 1, 175)

WIDTH = 600
HEIGHT = 600
point = 0
level = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 48)

CELL = 30
game_over = font.render("Game Over", True, colorBLACK)


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

    def __str__(self):
        return f"{self.x}, {self.y}"

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
            screen.fill(colorRED)
            screen.blit(game_over, (30, 250))
            draw_text()
            pygame.display.update()
            time.sleep(2)
            running = False

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        global point, level
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos()
            point += 1
            if 5 <= point < 10:
                level = 2
            elif 10 <= point < 15:
                level = 3
            elif 15 <= point < 20:
                level = 4
            elif 20 <= point < 25:
                level = 5
            elif point >= 25:
                level = 6
def background():
    if level == 1:
        screen.fill(colorBLACK)
    if level == 2:
        screen.fill(colorWHITE)
    if level == 3:
        screen.fill(colorBLUE)
    if level == 4:
        screen.fill(colorORANGE)
    if level == 5:
        screen.fill(colorBROWN)
    if level == 6:
        screen.fill(colorPINK)
class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, WIDTH // CELL - 1)
        self.pos.y = random.randint(0, HEIGHT // CELL - 1)

def draw_text():
    
    point_text = small_font.render(f"Points: {point}", True, colorVIOLET)
    screen.blit(point_text, (10, HEIGHT - 30))

    level_text = big_font.render(f"Level {level}", True, colorBLACK if level != 1 else colorWHITE)
    screen.blit(level_text, ((WIDTH - level_text.get_width()) // 2, 10))
FPS = 5
clock = pygame.time.Clock()

username = input("Enter your username: ")


with conn.cursor() as cursor:
    cursor.execute("SELECT id FROM \"user\" WHERE username = %s;", (username,))
    user = cursor.fetchone()
    if user:
        user_id = user[0]
        point, level = get_user_score(conn, user_id)
        print(f"Welcome back {username}! Your current score is {point} and level is {level}.")
    else:
        user_id = add_user(conn, username)
        point, level = 0, 1  
        print(f"Welcome {username}! Your game starts now.")


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

    background()
    draw_grid()

    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()
    draw_text()
    pygame.display.flip()
    clock.tick(FPS)
save_user_score(conn, user_id, point, level)
pygame.quit()

