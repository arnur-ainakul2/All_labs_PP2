import pygame
import datetime

pygame.init()

# Размер окна
W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey Mouse Clock")

# Загрузка циферблата
clock_face = pygame.image.load("clock.png")
clock_face = pygame.transform.scale(clock_face, (600, 600))

# Загрузка рук Микки Мауса (800x600)
hands = {
    "minute": pygame.transform.scale(pygame.image.load("min_hand.png"), (800, 600)),  # Правая рука (минутная)
    "second": pygame.transform.scale(pygame.image.load("sec_hand.png"), (800, 600)),   # Левая рука (секундная)
}

clock = pygame.time.Clock()
FPS = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minute, second = now.minute, now.second

    # Угол поворота (минутная = -6° за каждую минуту, секундная = -6° за каждую секунду)
    angles = {
        "minute": -minute * 6,
        "second": -second * 6,
    }

    screen.fill((255, 255, 255))
    screen.blit(clock_face, (100, 100))

    for name, img in hands.items():
        rotated = pygame.transform.rotate(img, angles[name])
        rect = rotated.get_rect(center=(W // 2, H // 2))  # Центр вращения — центр экрана
        screen.blit(rotated, rect.topleft)

    # Рисуем центр часов (точку)
    pygame.draw.circle(screen, (0, 0, 0), (W // 2, H // 2), 10)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()