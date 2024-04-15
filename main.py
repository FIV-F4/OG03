import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра ТИР (FIV)")
icon = pygame.image.load("img/logo_fiv.ico")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80
hit_sound = pygame.mixer.Sound("sound/hit_sound.wav")

score = 0
level = 1
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 0.1
target_speed_y = 0.1
color = (255, 255, 255)  # Белый фон
font = pygame.font.SysFont(None, 36)
timer_start = 100


def show_score(x, y):
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (x, y))


def show_timer(x, y, time_left):
    timer_text = font.render(f"Время: {time_left}", True, (0, 0, 0))
    screen.blit(timer_text, (x, y))


def check_collision(mouse_x, mouse_y, target_x, target_y):
    return target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height


def move_target():
    global target_x, target_y, target_speed_x, target_speed_y

    target_x += target_speed_x
    target_y += target_speed_y


    if target_x + target_width > SCREEN_WIDTH or target_x < 0:
        target_speed_x = -target_speed_x
    if target_y + target_height > SCREEN_HEIGHT or target_y < 0:
        target_speed_y = -target_speed_y


def game_over():
    screen.fill((255, 255, 255))
    game_over_text = font.render(f"Игра окончена! Ваш счет: {score}", True, (0, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(3000)



running = True
start_ticks = pygame.time.get_ticks()
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if check_collision(mouse_x, mouse_y, target_x, target_y):
                hit_sound.play()
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                if score % 10 == 0:
                    level += 1
                    target_width = max(20, target_width - 10)
                    target_height = max(20, target_height - 10)
                target_speed_x = random.choice(
                    [ -0.3, -0.2, 0.2, 0.3])
                target_speed_y = random.choice([-0.3, -0.2, 0.2, 0.3])

    move_target()

    show_score(10, 10)
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Как долго идет игра
    time_left = max(timer_start - seconds, 0)  # Оставшееся время
    show_timer(SCREEN_WIDTH - 130, 10, int(time_left))

    screen.blit(pygame.transform.scale(target_img, (target_width, target_height)), (target_x, target_y))
    if time_left == 0:
        game_over()
        running = False


    pygame.display.update()

game_over_text = font.render(f"Игра окончена! Ваш счет: {score}", True, (0, 0, 0))
screen.fill((255, 255, 255))
screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()
