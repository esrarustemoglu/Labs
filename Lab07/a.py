import pygame
from sys import exit
from datetime import datetime
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

clock_surf = pygame.image.load("/Users/esrarustemoglu/clock.png").convert()
sec_hand_surf = pygame.image.load("/Users/esrarustemoglu/sec_hand.png").convert_alpha()
min_hand_surf = pygame.image.load("/Users/esrarustemoglu/min_hand.png").convert_alpha()

def blitRotateCenter(surf, image, pivot, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pivot)
    surf.blit(rotated_image, new_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    now = datetime.now()
    seconds = now.second   
    minutes = now.minute + seconds / 60  

    sec_angle = -((seconds * 6) - 55)  
    min_angle = -((minutes * 6 ) + 45) 

    screen.fill((255, 255, 255))  
    screen.blit(clock_surf, (0, 0))  

    blitRotateCenter(screen, sec_hand_surf, (400, 300), sec_angle)  
    blitRotateCenter(screen, min_hand_surf, (400, 300), min_angle)  

    pygame.display.update()
    clock.tick(60)  