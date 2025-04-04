import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

drawing = False
last_pos = None
current_color = BLACK
brush_size = 5
tool = "pen"
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128), (0, 0, 0)]
color_rects = [pygame.Rect(10 + i * 40, 10, 30, 30) for i in range(len(colors))]

running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
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
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "right_triangle"
            elif event.key == pygame.K_q:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_h:
                tool = "rhombus"
    
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
        elif tool == "square":
            side = max(abs(mouse_pos[0] - last_pos[0]), abs(mouse_pos[1] - last_pos[1]))
            top_left = (min(mouse_pos[0], last_pos[0]), min(mouse_pos[1], last_pos[1]))
            pygame.draw.rect(canvas, current_color, (*top_left, side, side), 2)
        elif tool == "right_triangle":
            x1, y1 = last_pos
            x2, y2 = mouse_pos
            points = [(x1, y1), (x2, y2), (x1, y2)]
            pygame.draw.polygon(canvas, current_color, points, 2)
        elif tool == "equilateral_triangle":
            x1, y1 = last_pos
            x2, y2 = mouse_pos
            side = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            height = (3 ** 0.5 / 2) * side
            direction = 1 if y2 >= y1 else -1
            midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
            points = [
                (x1, y2),
                (x2, y2),
                (midpoint[0], y2 - direction * height)
            ]
            pygame.draw.polygon(canvas, current_color, points, 2)
        elif tool == "rhombus":
            x1, y1 = last_pos
            x2, y2 = mouse_pos
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            dx = abs(x2 - x1) // 2
            dy = abs(y2 - y1) // 2
            points = [
                (cx, y1),
                (x2, cy),
                (cx, y2),
                (x1, cy)
            ]
            pygame.draw.polygon(canvas, current_color, points, 2)
    
    for i, rect in enumerate(color_rects):
        pygame.draw.rect(screen, colors[i], rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
    
    pygame.display.flip()

pygame.quit()

# P - Pen
# E - Eraser
# R - Rectangle
# C - Circle
# S - Square
# T - Right Triangle
# Q - Equilateral Triangle
# H - Rhombus
