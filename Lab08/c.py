import pygame

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Variables
drawing = False
last_pos = None
current_color = BLACK
brush_size = 5
tool = "pen"  # "pen", "rectangle", "circle", "eraser"
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Color Palette
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128), (0, 0, 0)]
color_rects = [pygame.Rect(10 + i * 40, 10, 30, 30) for i in range(len(colors))]

# Main loop
running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                for i, rect in enumerate(color_rects):
                    if rect.collidepoint(event.pos):
                        current_color = colors[i]
                        tool = "pen"
                        break
                else:
                    drawing = True
                    last_pos = event.pos
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_p:
                tool = "pen"
            elif event.key == pygame.K_e:
                tool = "eraser"
    
    if drawing and pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        
        if tool == "pen":
            pygame.draw.line(canvas, current_color, last_pos, mouse_pos, brush_size)
            last_pos = mouse_pos
        elif tool == "eraser":
            pygame.draw.line(canvas, WHITE, last_pos, mouse_pos, brush_size * 2)
            last_pos = mouse_pos
        elif tool == "rectangle":
            rect_width = abs(mouse_pos[0] - last_pos[0])
            rect_height = abs(mouse_pos[1] - last_pos[1])
            rect_top_left = (min(mouse_pos[0], last_pos[0]), min(mouse_pos[1], last_pos[1]))
            pygame.draw.rect(canvas, current_color, (*rect_top_left, rect_width, rect_height), 2)
        elif tool == "circle":
            radius = int(((mouse_pos[0] - last_pos[0]) ** 2 + (mouse_pos[1] - last_pos[1]) ** 2) ** 0.5)
            pygame.draw.circle(canvas, current_color, last_pos, radius, 2)
    
    # Draw color palette
    for i, rect in enumerate(color_rects):
        pygame.draw.rect(screen, colors[i], rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
    
    pygame.display.flip()

pygame.quit()