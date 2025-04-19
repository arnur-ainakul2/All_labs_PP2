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
FOOD_TIME_LIMIT = 5000  # Время жизни еды в миллисекундах (5000мс = 5 секунд)

# Screen dimensions
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Game settings
snake_block = 10  # размер каждого блока змеи
initial_speed = 15  # начальная скорость
speed_increase = 2  # увеличение скорости за уровень
level_up_score = 3  # Количество очков для повышения уровня

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

class Food:
    def __init__(self):
        self.x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        self.time_created = pygame.time.get_ticks()  # Время создания еды

    def draw(self):
        pygame.draw.rect(dis, green, [self.x, self.y, snake_block, snake_block])

    def is_expired(self):
        # Проверка, прошло ли 5 секунд с момента создания еды
        if pygame.time.get_ticks() - self.time_created > FOOD_TIME_LIMIT:
            return True
        return False

def gameLoop():
    game_start_time = pygame.time.get_ticks()  
    game_over = False
    game_close = False
    
    x1, y1 = dis_width / 2, dis_height / 2  # Начальная позиция змеи
    x1_change, y1_change = 0, 0
    
    snake_list = []
    snake_length = 1
    
    food = Food()  # Создаем объект еды
    
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
        
        # Проверка на столкновение с границами
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        
        # Рисуем еду
        food.draw()

        # Проверяем, не истекло ли время жизни еды
        if food.is_expired():
            food = Food()  # Создаем новую еду, если старая исчезла
        
        # Обновляем тело змеи
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        # Проверка на столкновение с собой
        if snake_head in snake_list[:-1]:  # Проверяем, есть ли голова в теле змеи
             game_close = True
        draw_snake(snake_block, snake_list)
        show_score(score, level)
        pygame.display.update()
        
        # Столкновение с едой
        if x1 == food.x and y1 == food.y:
            food = Food()  # Создаем новую еду
            snake_length += 1
            score += random.randint(0, 10)
            
            # Повышение уровня
            if score % level_up_score == 0:
                level += 1
                snake_speed += speed_increase
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

gameLoop()