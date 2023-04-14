import pygame
from sys import exit
import random


def display_score():
    score_text = font.render(f'SCORE: {real_score_1}', False, 'black')
    score_rect = score_text.get_rect(center=(550, 155))
    screen.blit(score_text, score_rect)


def display_score_1():
    score_1 = pygame.font.Font(None, 150)
    score_1_rend = score_1.render(f'SCORE: {real_score_1}', False, 'white')
    score_1_rect = score_1_rend.get_rect(center=(550, 320))
    screen.blit(score_1_rend, score_1_rect)


def restart():
    restart_text = pygame.font.Font(None, 40)
    restart_rend = restart_text.render('PRESS \'R\' TO RESTART', False, 'white')
    restart_rect = restart_rend.get_rect(center=(550, 400))
    screen.blit(restart_rend, restart_rect)


def start():
    plain_surface.fill('blue')


def game_name():
    game_name = pygame.font.Font(None, 50)
    game_name_rend = game_name.render('DRAGON BALL Z', False, 'yellow')
    game_name_rect = game_name_rend.get_rect(center=(355, 150))
    screen.blit(game_name_rend, game_name_rect)


def start_command():
    start_command = pygame.font.Font(None, 50)
    start_command_rend = start_command.render('PRESS \'SPACE\' TO START', False, 'yellow')
    start_command_rect = start_command_rend.get_rect(center=(355, 450))
    screen.blit(start_command_rend, start_command_rect)


pygame.init()
screen = pygame.display.set_mode((1070, 600),
                                 pygame.RESIZABLE)
pygame.display.set_caption('DRAGON BALL Z')
clock = pygame.time.Clock()

plain_surface = pygame.image.load('pygame/terrain (Custom) .jpg').convert()
text = pygame.image.load('pygame/dragon ball text.png').convert()
goku = pygame.image.load('pygame/goku.png').convert_alpha()
frieza = pygame.image.load('pygame/frieza1.png').convert_alpha()
dragon_ball = pygame.image.load('pygame/dragon ball.png').convert_alpha()
goku_2 = pygame.image.load('pygame/goku2.png').convert_alpha()
goku_black = pygame.image.load('pygame/goku black.png').convert_alpha()
kid_buu = pygame.image.load('pygame/kid buu.png').convert_alpha()
boss = pygame.image.load('pygame/boss.png').convert_alpha()


# random moves
moves_lst_frieza = [1900, 3000, 2500, 1500]
moves_lst_buu = [4000, 4800, 5500, 7000]
moves_lst_goku_black = [9000, 20000, 10000]
moves_lst_dragon_ball = [6000, 7000, 4000, 5500]

# health bar
heart_1 = pygame.image.load('pygame/hearts.png')
heart_2 = pygame.image.load('pygame/hearts.png')
heart_3 = pygame.image.load('pygame/hearts.png')
heart_1_rect = heart_1.get_rect(center=(20, 30))
heart_2_rect = heart_2.get_rect(center=(30, 30))
heart_3_rect = heart_3.get_rect(center=(40, 30))

font = pygame.font.Font(None, 30)
pygame.mixer.init()
pygame.mixer.music.load("game music.mp3")
pygame.mixer.music.set_volume(9)
pygame.mixer.music.play()

goku_rect = goku.get_rect(midbottom=(130, 430))
frieza_rect = frieza.get_rect(midbottom=(1100, 435))
goku_2_rect = goku_2.get_rect()
dragon_ball_rect = dragon_ball.get_rect(midbottom=(1100, 200))
goku_black_rect = goku_black.get_rect(midbottom=(8000, 435))
kid_buu_rect = kid_buu.get_rect(midbottom=(5000, 438))
boss_rect = boss.get_rect(midbottom=(100000, 550))

gravity = 0
score = 0
real_score = 0
game_active = True
real_score_1 = 0
hearts = 0
hearts_count = 0
real_hearts = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                if goku_rect.right <= 1055:
                    goku_rect.right += 50
            elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                if goku_rect.left >= 10:
                    goku_rect.left -= 50
            elif event.key == pygame.K_SPACE:
                if goku_rect.bottom >= 430:
                    gravity = -23
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if goku_rect.collidepoint(mouse_pos):
                if goku_rect.bottom >= 430:
                    gravity = -25

        if not game_active:
            screen.fill('black')
            display_score_1()
            restart()
            pygame.mixer.music.stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                frieza_rect.left = 2200
                kid_buu_rect.left = 6000
                goku_black_rect.left = 25000
                dragon_ball_rect.left = 8000
                boss_rect.left = 70000
                goku_rect.left = 130
                real_score_1 = 0
                game_active = True
                pygame.mixer.music.play()
                hearts = 3
    if game_active:
        frieza_random = random.choice(moves_lst_frieza)
        buu_random = random.choice(moves_lst_buu)
        goku_black_random = random.choice(moves_lst_dragon_ball)
        dragon_ball_random = random.choice(moves_lst_dragon_ball)
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.rewind()
        frieza_rect.left -= 9
        if frieza_rect.right <= 0:
            frieza_rect.left = frieza_random

        dragon_ball_rect.left -= 9
        if dragon_ball_rect.right <= 0:
            dragon_ball_rect.left = dragon_ball_random

        goku_black_rect.left -= 10
        if goku_black_rect.right <= 0:
            goku_black_rect.left = goku_back_random

        kid_buu_rect.left -= 9
        if kid_buu_rect.right <= 0:
            kid_buu_rect.left = buu_random

        boss_rect.left -= 10
        if boss_rect.right <= -100:
            boss_rect.left = 60000

        if frieza_rect.colliderect(goku_rect):
            hearts_count += 1
            real_hearts = hearts_count - (hearts_count - 1)
            frieza_rect.left = frieza_random
            if not frieza_rect.colliderect(goku_rect):
                hearts += real_hearts
                hearts_count = 0
                real_hearts = 0

        if goku_black_rect.colliderect(goku_rect):
            hearts_count += 1
            real_hearts = hearts_count - (hearts_count - 1)
            goku_black_rect.left = goku_black_random
            if not goku_black_rect.colliderect(goku_rect):
                hearts += real_hearts
                hearts_count = 0
                real_hearts = 0

        if kid_buu_rect.colliderect(goku_rect):
            hearts_count += 1
            real_hearts = hearts_count - (hearts_count - 1)
            kid_buu_rect.left = buu_random
            if not kid_buu_rect.colliderect(goku_rect):
                hearts += real_hearts
                hearts_count = 0
                real_hearts = 0

        if boss_rect.colliderect(goku_rect):
            game_active = False

        if goku_rect.colliderect(dragon_ball_rect):
            score += 1
            real_score = score - (score - 1)
            dragon_ball_rect.left = dragon_ball_random
        if not goku_rect.colliderect(dragon_ball_rect):
            real_score_1 += real_score
            real_score = 0
            score = 0

        screen.blit(plain_surface, (0, 0))
        screen.blit(text, (450, 30))
        screen.blit(goku, goku_rect)
        screen.blit(frieza, frieza_rect)
        screen.blit(dragon_ball, dragon_ball_rect)
        screen.blit(goku_black, goku_black_rect)
        screen.blit(kid_buu, kid_buu_rect)
        screen.blit(boss, boss_rect)

    match hearts:
        case 0:
            screen.blit(heart_3, heart_3_rect)
            screen.blit(heart_2, heart_2_rect)
            screen.blit(heart_1, heart_1_rect)
        case 1:
            screen.blit(heart_2, heart_2_rect)
            screen.blit(heart_1, heart_1_rect)
        case 2:
            screen.blit(heart_1, heart_1_rect)
        case 3:
            game_active = False

    display_score()
    gravity += 1
    goku_rect.y += gravity
    if goku_rect.bottom >= 432:
        goku_rect.bottom = 430

    pygame.display.update()
    clock.tick(30)
