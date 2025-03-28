import pygame
import time
import random

pygame.init()

# Colors
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Game settings
snake_block = 10
initial_speed = 15  # Base speed
speed_increase = 2  # Speed increase per level
level_up_score = 3  # Score needed to level up

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def show_score(score, level):
    score_text = score_font.render(f"Score: {score}  Level: {level}", True, yellow)
    dis.blit(score_text, [10, 10])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False
    
    x1, y1 = dis_width / 2, dis_height / 2  # Snake start position
    x1_change, y1_change = 0, 0
    
    snake_list = []
    snake_length = 1
    
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    score = 0
    level = 1
    snake_speed = initial_speed
    clock = pygame.time.Clock()
    
    while not game_over:
        while game_close:
            dis.fill(blue)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            show_score(score, level)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        # Border collision check
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        
        # Draw food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        # Update snake body
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        # Collision with itself
        if snake_head in snake_list[:-1]:  # Проверяем, есть ли голова в теле змеи
             game_close = True
        draw_snake(snake_block, snake_list)
        show_score(score, level)
        pygame.display.update()
        
        # Food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_length += 1
            score += 1
            
            # Level up
            if score % level_up_score == 0:
                level += 1
                snake_speed += speed_increase
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

gameLoop()
