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


def game_name():
    game_name_1 = pygame.font.Font(None, 50)
    game_name_rend = game_name_1.render('DRAGON BALL Z', False, 'yellow')
    game_name_rect = game_name_rend.get_rect(center=(555, 130))
    screen.blit(game_name_rend, game_name_rect)


def start_command():
    start_command_1 = pygame.font.Font(None, 50)
    start_command_rend = start_command_1.render('PRESS \'ANY KEY\' TO START', False, 'yellow')
    start_command_rect = start_command_rend.get_rect(center=(555, 530))
    screen.blit(start_command_rend, start_command_rect)


def start():
    screen.fill('blue')
    game_name()
    screen.blit(game_poster, game_poster_rect)
    start_command()


pygame.init()
screen = pygame.display.set_mode((1070, 600),
                                 pygame.RESIZABLE)
pygame.display.set_caption('DRAGON BALL Z')
clock = pygame.time.Clock()

text = pygame.image.load('pygame/dragon ball text.png').convert()
goku = pygame.image.load('pygame/goku.png').convert_alpha()
frieza = pygame.image.load('pygame/frieza1.png').convert_alpha()
goku_2 = pygame.image.load('pygame/goku2.png').convert_alpha()
goku_black = pygame.image.load('pygame/goku black.png').convert_alpha()
kid_buu = pygame.image.load('pygame/kid buu.png').convert_alpha()
zamasu = pygame.image.load('pygame/zamasu.png').convert_alpha()
game_poster = pygame.image.load('pygame/game poster.png').convert_alpha()
kamehameha = pygame.image.load("pygame/kamehameha.png").convert_alpha()
kamehameha_icon = pygame.image.load("pygame/kamehameha.png").convert_alpha()
kamehameha_icon_reload = pygame.image.load("pygame/kamehameha icon black.png").convert()

# random moves
moves_lst_frieza = [2000, 3000, 1800, 2400]
moves_lst_buu = [2000, 4000, 5500, 4800]
moves_lst_goku_black = [4000, 3500, 2000]
moves_lst_dragon_ball = [2400, 2000, 2700, 1900]
moves_lst_zamasu = [5000, 4000, 6000, 3000]

# health bar
heart_1 = pygame.image.load('pygame/hearts.png')
heart_2 = pygame.image.load('pygame/hearts.png')
heart_3 = pygame.image.load('pygame/hearts.png')
heart_1_rect = heart_1.get_rect(center=(20, 30))
heart_2_rect = heart_2.get_rect(center=(30, 30))
heart_3_rect = heart_3.get_rect(center=(40, 30))

# maps
planet_namek = pygame.image.load('pygame/planet namek.png').convert()
planet_kai = pygame.image.load('pygame/kai planet.png').convert()
future_trunks_city = pygame.image.load('pygame/future trunks city.png').convert()

# dragon balls
dragon_ball = pygame.image.load('pygame/dragon ball.png').convert_alpha()
dragon_ball_rect = dragon_ball.get_rect(midbottom=(1100, 200))
namekian_dragon_ball = pygame.image.load('pygame/namekian dragon ball.png').convert_alpha()
namekian_dragon_ball_rect = namekian_dragon_ball.get_rect(midbottom=(1100, 200))
super_dragon_ball = pygame.image.load('pygame/super dragon ball.png').convert_alpha()
super_dragon_ball_rect = super_dragon_ball.get_rect(midbottom=(1100, 200))
game_poster_rect = game_poster.get_rect(center=(555, 330))

font = pygame.font.Font(None, 30)
pygame.mixer.init()
pygame.mixer.music.load("game music.mp3")
pygame.mixer.music.set_volume(15)
pygame.mixer.music.play(4)

# rect
goku_rect = goku.get_rect(midbottom=(130, 430))
frieza_rect = frieza.get_rect(midbottom=(1100, 435))
goku_2_rect = goku_2.get_rect()
goku_black_rect = goku_black.get_rect(midbottom=(4000, 435))
kid_buu_rect = kid_buu.get_rect(midbottom=(5000, 438))
zamasu_rect = zamasu.get_rect(midbottom=(3000, 435))
kamehameha_rect = kamehameha.get_rect(center=(-100, 90))

# values
gravity = 0
score = 0
real_score = 0
game_active = False
real_score_1 = 0
hearts = 3
hearts_count = 0
real_hearts = 0
map_count = 0
start_true = True
check_state = False
check = 0
right = False
left = False
kamehameha_throw = False

# timer
check_button = 0
button_pressed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RCTRL) or (event.key == pygame.K_LCTRL):
                goku_pos = goku_rect.center
                if check_button - button_pressed >= 15000:
                    button_pressed = pygame.time.get_ticks()
                    kamehameha_pos = goku_pos
                    kamehameha_rect.center = kamehameha_pos
                    kamehameha_throw = True
                else:
                    kamehameha_throw = False
            elif event.key == pygame.K_RIGHT:
                right = True
            elif event.key == pygame.K_LEFT:
                left = True
            elif event.key == pygame.K_SPACE:
                if goku_rect.bottom >= 430:
                    gravity = -23
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            elif event.key == pygame.K_LEFT:
                left = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if goku_rect.collidepoint(mouse_pos):
                if goku_rect.bottom >= 430:
                    gravity = -23

        # game start
        if start_true:
            start()
            if event.type == pygame.KEYDOWN:
                game_active = True
                check_state = True
                start_true = False
                pygame.mixer.music.set_volume(15)
        # game stop
        elif not game_active:
            screen.fill('black')
            display_score_1()
            restart()
            pygame.mixer.music.stop()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                frieza_rect.left = 2200
                kid_buu_rect.left = 6000
                goku_black_rect.left = 3000
                dragon_ball_rect.left = 4000
                zamasu_rect.left = 70000
                goku_rect.left = 130
                check_button = 0
                button_pressed = 0
                real_score_1 = 0
                game_active = True
                pygame.mixer.music.play(5)
                hearts = 3
                map_count = 0
    # game activation

    if game_active:
        check_button = pygame.time.get_ticks()
        if right:
            if goku_rect.right <= 1065:
                goku_rect.right += 10
        elif left:
            if goku_rect.left >= 10:
                goku_rect.left -= 10

        if kamehameha_throw:
            kamehameha_rect.left += 8
        frieza_random = random.choice(moves_lst_frieza)
        buu_random = random.choice(moves_lst_buu)
        goku_black_random = random.choice(moves_lst_dragon_ball)
        dragon_ball_random = random.choice(moves_lst_dragon_ball)
        zamasu_random = random.choice(moves_lst_zamasu)

        if real_score_1 == 11:
            map_count = 1
        elif real_score_1 == 21:
            map_count = 2
        elif real_score_1 == 31:
            map_count = 3
        elif real_score_1 == 41:
            map_count = 4
        elif real_score_1 == 51:
            map_count = 5

        # villains movement

        frieza_rect.left -= 9
        if frieza_rect.right <= 0:
            frieza_rect.left = frieza_random

        if goku_rect.colliderect(frieza_rect):
            hearts_count = 1
            frieza_rect.left = frieza_random
            if not goku_rect.colliderect(frieza_rect):
                hearts -= hearts_count
                hearts_count = 0

        if goku_black_rect.colliderect(goku_rect):
            hearts_count = 1
            goku_black_rect.left = goku_black_random
            if not goku_black_rect.colliderect(goku_rect):
                hearts -= hearts_count
                hearts_count = 0

        if kid_buu_rect.colliderect(goku_rect):
            hearts_count = 1
            kid_buu_rect.left = buu_random
            if not kid_buu_rect.colliderect(goku_rect):
                hearts -= hearts_count
                hearts_count = 0

        if zamasu_rect.colliderect(goku_rect):
            hearts_count = 1
            if not zamasu_rect.colliderect(goku_rect):
                hearts -= hearts_count
                hearts_count = 0

        # dragon balls movement
        if goku_rect.colliderect(dragon_ball_rect):
            score = 1
            dragon_ball_rect.left = dragon_ball_random
            if not goku_rect.colliderect(dragon_ball_rect):
                real_score_1 += score
                score = 0

        if goku_rect.colliderect(namekian_dragon_ball_rect):
            score = 1
            namekian_dragon_ball_rect.left = dragon_ball_random
            if not goku_rect.colliderect(namekian_dragon_ball_rect):
                real_score_1 += score
                score = 0

        if goku_rect.colliderect(super_dragon_ball_rect):
            score = 1
            super_dragon_ball_rect.left = dragon_ball_random
            if not goku_rect.colliderect(super_dragon_ball_rect):
                real_score_1 += score
                score = 0

        # attacks
        if kamehameha_rect.colliderect(frieza_rect):
            frieza_rect.left = frieza_random
            kamehameha_rect.left = -100
            kamehameha_throw = False

        elif kamehameha_rect.colliderect(kid_buu_rect):
            kid_buu_rect.left =  buu_random
            kamehameha_rect.left = -100
            kamehameha_throw = False

        elif kamehameha_rect.colliderect(zamasu_rect):
            zamasu_rect.left = zamasu_random
            kamehameha_rect.left = -100
            kamehameha_throw = False

        elif kamehameha_rect.colliderect(goku_black_rect):
            goku_black_rect.left = goku_black_random
            kamehameha_rect.left = -100
            kamehameha_throw = False

        elif kamehameha_rect.left > 1300:
            kamehameha_rect.left = -100
            kamehameha_throw = False

        screen.blit(planet_namek, (0, 0))
        screen.blit(goku, goku_rect)
        screen.blit(frieza, frieza_rect)
        screen.blit(text, (455, 40))

        if map_count == 0:
            screen.blit(dragon_ball, dragon_ball_rect)
            screen.blit(kamehameha, kamehameha_rect)
            screen.blit(kamehameha_icon, (100, 10))
            dragon_ball_rect.left -= 9
            if dragon_ball_rect.right <= 0:
                dragon_ball_rect.left = dragon_ball_random
        elif map_count == 1:
            screen.blit(planet_kai, (0, 0))
            screen.blit(goku, goku_rect)
            screen.blit(kid_buu, kid_buu_rect)
            screen.blit(frieza, frieza_rect)
            screen.blit(kamehameha, kamehameha_rect)
            screen.blit(text, (455, 40))
            screen.blit(namekian_dragon_ball, namekian_dragon_ball_rect)
            namekian_dragon_ball_rect.left -= 9
            if namekian_dragon_ball_rect.right <= 0:
                namekian_dragon_ball_rect.left = dragon_ball_random
            kid_buu_rect.left -= 9
            if kid_buu_rect.right <= 0:
                kid_buu_rect.left = buu_random
        elif map_count == 2:
            screen.blit(future_trunks_city, (0, 0))
            screen.blit(goku, goku_rect)
            screen.blit(kid_buu, kid_buu_rect)
            screen.blit(frieza, frieza_rect)
            screen.blit(text, (455, 40))
            screen.blit(super_dragon_ball, super_dragon_ball_rect)
            screen.blit(goku_black, goku_black_rect)
            screen.blit(zamasu, zamasu_rect)
            super_dragon_ball_rect.left -= 9
            if super_dragon_ball_rect.right <= 0:
                super_dragon_ball_rect.left = dragon_ball_random
            kid_buu_rect.left -= 9
            if kid_buu_rect.right <= 0:
                kid_buu_rect.left = buu_random
            goku_black_rect.left -= 9
            if goku_black_rect.right <= 0:
                goku_black_rect.left = goku_black_random
            zamasu_rect.left -= 11
            if zamasu_rect.right <= 0:
                zamasu_rect.left = zamasu_random

        match hearts:
            case 3:
                screen.blit(heart_3, heart_3_rect)
                screen.blit(heart_2, heart_2_rect)
                screen.blit(heart_1, heart_1_rect)
            case 2:
                screen.blit(heart_2, heart_2_rect)
                screen.blit(heart_1, heart_1_rect)
            case 1:
                screen.blit(heart_1, heart_1_rect)
            case 0:
                game_active = False

    display_score()
    gravity += 1
    goku_rect.y += gravity
    if goku_rect.bottom >= 432:
        goku_rect.bottom = 430

    print(f"{check_button}     {button_pressed}")

    pygame.display.update()
    clock.tick(30)
