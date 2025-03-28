import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    mode = 'draw'  # 'rectangle', 'circle', 'eraser'
    color = (0, 0, 255)  # Default color is blue
    start_pos = None
    shapes = []
    drawing = False
    
    while True:
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = (255, 0, 0)  # Red
                    print("Red color selected")
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)  # Green
                    print("Green color selected")
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)  # Blue
                    print("Blue color selected")
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                    print("Eraser mode selected")
                elif event.key == pygame.K_c:
                    mode = 'circle'
                    print("Circle mode selected")
                elif event.key == pygame.K_t:
                    mode = 'rectangle'
                    print("Rectangle mode selected")
                elif event.key == pygame.K_d:
                    mode = 'draw'
                    print("Draw mode selected")
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                drawing = True
                print(f"Mouse down at {start_pos}, mode: {mode}")
                if mode == 'draw':
                    shapes.append(('line', start_pos, start_pos, color))
                elif mode == 'eraser':
                    shapes.append(('line', start_pos, start_pos, (255, 255, 255)))
            
            if event.type == pygame.MOUSEMOTION and drawing:
                if mode == 'draw' or mode == 'eraser':
                    shapes.append(('line', shapes[-1][2], event.pos, color if mode == 'draw' else (255, 255, 255)))
                    print(f"Drawing line from {shapes[-1][1]} to {event.pos}")
            
            if event.type == pygame.MOUSEBUTTONUP and start_pos:
                end_pos = event.pos
                print(f"Mouse up at {end_pos}, mode: {mode}")
                if mode == 'rectangle':
                    shapes.append(('rectangle', start_pos, end_pos, color))
                elif mode == 'circle':
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    shapes.append(('circle', start_pos, radius, color))
                drawing = False
                start_pos = None
        
        for shape in shapes:
            if shape[0] == 'rectangle':
                pygame.draw.rect(screen, shape[3], pygame.Rect(shape[1], (shape[2][0] - shape[1][0], shape[2][1] - shape[1][1])))
            elif shape[0] == 'circle':
                pygame.draw.circle(screen, shape[3], shape[1], shape[2])
            elif shape[0] == 'line':
                pygame.draw.line(screen, shape[3], shape[1], shape[2], 3)
        
        pygame.display.flip()
        clock.tick(60)

main()
