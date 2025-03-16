import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 600))
red = (255, 0, 0)
clock = pygame.time.Clock()
x = 400
y = 300
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - 25 - 20 >= 0: y -= 20
    if pressed[pygame.K_DOWN] and y + 25 + 20 <= 600: y += 20
    if pressed[pygame.K_LEFT] and x - 25 - 20 >= 0: x -= 20
    if pressed[pygame.K_RIGHT] and x + 25 + 20 <= 800: x += 20
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, red,(x, y), 25)
    pygame.display.update()
    clock.tick(60)