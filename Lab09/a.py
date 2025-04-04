import pygame
import sys, time
import os
from random import randint
from pygame.locals import *
pygame.init()

Black = pygame.Color(0, 0, 0)
White = pygame.Color(255, 255, 255)
Grey = pygame.Color(128, 128, 128)
Red = pygame.Color(255, 0, 0)
Blue = pygame.Color(0, 0, 255)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, Black)
 
background = pygame.image.load("/Users/esrarustemoglu/PygameTutorial_3_0/AnimatedStreet.png")

FPS = pygame.time.Clock()
fps = 60

SPEED = 5

SCORE = 0

Width = 400
Height = 600
DISPLAYSURF = pygame.display.set_mode((Width, Height))
DISPLAYSURF.fill(White)

pygame.display.set_caption("Racer")
def get_random_position(existing_rects):
    while True:
        pos = (randint(40, Width - 40), 0)
        new_rect = pygame.Rect(0, 0, 30, 30)
        new_rect.center = pos
        if not any(r.colliderect(new_rect) for r in existing_rects):
            return pos
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/esrarustemoglu/PygameTutorial_3_0/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, Width - 40), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0, 10)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (randint(30, Width - 30), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/esrarustemoglu/PygameTutorial_3_0/PLayer.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.left > 0:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, images):
        super().__init__()
        self.image = pygame.image.load(images)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, Width - 40), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0, 10)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (randint(30, Width - 30), 0) 
P1 = Player()
E1 = Enemy()
existing_rects = [E1.rect]


C1 = Coin("/Users/esrarustemoglu/PygameTutorial_3_0/coin.png")
C1.rect.center = get_random_position(existing_rects)
existing_rects.append(C1.rect)

C2 = Coin("/Users/esrarustemoglu/PygameTutorial_3_0/coin2.png")
C2.rect.center = get_random_position(existing_rects)
existing_rects.append(C2.rect)

C3 = Coin("/Users/esrarustemoglu/PygameTutorial_3_0/coin3.png")
C3.rect.center = get_random_position(existing_rects)
existing_rects.append(C3.rect)


enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(C2)
all_sprites.add(C3)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, Black)
    DISPLAYSURF.blit(scores, (10, 10))
    
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound("/Users/esrarustemoglu/PygameTutorial_3_0/crash.wav").play()
          time.sleep(0.5)

          DISPLAYSURF.fill(Red)
          DISPLAYSURF.blit(game_over, (30, 250))

          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()  
    if pygame.sprite.collide_rect(P1, C1):
        SCORE += 1
        C1.rect.center = get_random_position([E1.rect, C2.rect, C3.rect])

    if pygame.sprite.collide_rect(P1, C2):
        SCORE += 2
        C2.rect.center = get_random_position([E1.rect, C1.rect, C3.rect])

    if pygame.sprite.collide_rect(P1, C3):
        SCORE += 3
        C3.rect.center = get_random_position([E1.rect, C1.rect, C2.rect])


    pygame.display.update()
    FPS.tick(fps)