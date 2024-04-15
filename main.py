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

color = (255, 255, 255)  # Белый фон

font = pygame.font.SysFont(None, 36)


def show_score(x, y):
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (x, y))


def check_collision(mouse_x, mouse_y, target_x, target_y):
    if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
        return True
    return False


running = True
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

    show_score(10, 10)

    screen.blit(pygame.transform.scale(target_img, (target_width, target_height)), (target_x, target_y))

    pygame.display.update()

game_over_text = font.render(f"Игра окончена! Ваш счет: {score}", True, (0, 0, 0))
screen.fill((255, 255, 255))
screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()
