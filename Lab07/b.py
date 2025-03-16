import pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
songs = [
    "/Users/esrarustemoglu/Sezen-Aksu-Kacin-Kurasi.mp3",
    "/Users/esrarustemoglu/Sezen-Aksu-Asktan-Ne-Haber.mp3",
    "/Users/esrarustemoglu/Sezen-Aksu-Aldatildik.mp3"
]
track = 0
paused = False

def playsong():
    pygame.mixer.music.load(songs[track])
    pygame.mixer.music.play()
playsong()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            paused = True
        elif paused:
            pygame.mixer.music.unpause()
            paused = False

    if pressed[pygame.K_s]:
        pygame.mixer.music.stop()
        paused = False

    if pressed[pygame.K_n]:
        pygame.mixer.music.stop()  
        track = (track + 1) % len(songs)
        playsong()
        paused = False

    if pressed[pygame.K_p]:
        pygame.mixer.music.stop()  
        track = (track - 1) % len(songs)
        playsong()
        paused = False

    screen.fill((0, 0, 0))  
    pygame.display.flip()

pygame.quit()
