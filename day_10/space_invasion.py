import pygame
import random
import math
from pygame import mixer
import io

"""
SPATIAL INVASION GAME
"""
# initialize pygame
pygame.init()

# Create screen
WIDTH = 1080
HEIGHT = 680
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Title and icon invasion
pygame.display.set_caption("<|>Space Invasion<|>")
icon = pygame.image.load('img/ovni.png')
pygame.display.set_icon(icon)
# random image
background = pygame.image.load(f'img/galaxy_background_pygame/{random.randint(1, 10)}.jpg')

"""
Tips to executable file:
1) We will convert string to Bytes object
2) Use pyinstaller to create executable file
    pyinstaller --clean --onefile --windowed space_invasion.py
"""


# tip 1 - convert string to Bytes object
def font_in_bytes(font_to_convert):
    # open ttf file on binary read mode
    with open(font_to_convert, 'rb') as f:
        # read bytes of the file and save it
        ttf_bytes = f.read()
    # Create a BytesIO object
    return io.BytesIO(ttf_bytes)


# player variables
player_img = pygame.image.load('img/space_ship.png')
player_img_width = player_img.get_width()  # width pixels of player image
player_img_height = player_img.get_height()  # height pixels of player image
playerX = (WIDTH - player_img_width)//2
playerY = HEIGHT - player_img_height*1.5
# player movement
playerX_change = 0

# screen bounds
bound_left = 8
bound_right = WIDTH - player_img_width


# enemy position random
def random_position(idx_enemy):
    return (
        random.randint(0, WIDTH - enemy_img_pxl[idx_enemy]),
        random.randint(enemy_img_pxl[idx_enemy]//2, HEIGHT//4)
    )


"""
New versions will implement enemy class
"""
# enemy variables
enemy_img = []
enemy_img_pxl = []  # width pixels of enemy image
enemyX, enemyY = [], []
# enemy movement
enemyX_change = []
enemyY_change = []
enemy_quantity = 7


def generate_random_acceleration():
    """
    generate a value between 0.7 and 0.9 to be returned
    """
    return random.randint(7, 9)/10


def random_enemy_img():
    return pygame.image.load(f'img/monster{random.randint(1, 3)}.png')


for en in range(enemy_quantity):
    enemy_img.append(random_enemy_img())
    enemy_img_pxl.append(enemy_img[en].get_width())  # width pixels of enemy image
    randX, randY = random_position(en)
    enemyX.append(randX)
    enemyY.append(randY)
    # enemy movement
    enemyX_change.append(generate_random_acceleration())
    enemyY_change.append(enemy_img_pxl[en]//2)

# bullet variables
bullet_img = pygame.image.load('img/bullet.png')
# bullet_img_pxl = bullet_img.get_width()  # width pixels of bullet image
bulletX = 0  # random.randint(0, WIDTH - bullet_img_pxl)  # initial position
bulletY = playerY  # random.randint(bullet_img_pxl//2, HEIGHT//4)
# bullet movement
bulletX_change = 0
bulletY_change = 1.2
bullet_visible = False

# bullet sound
bullet_sound = mixer.Sound('sounds_fx/star-wars-blaster-2(chosic.com).mp3')

bullet_dic = {
    'posX': 0,
    'posY': playerY,
    'X_change': 0,
    'Y_change': 1.2,
    'visible': False,
    'img': pygame.image.load("img/bullet.png"),
    'sound': mixer.Sound('sounds_fx/star-wars-blaster-2(chosic.com).mp3')
}
bullet_img_pxl = bullet_dic['img'].get_width()  # width pixels of bullet image

# hit/collision sound
hit_sound = mixer.Sound('sounds_fx/rock-destroy-6409.mp3')

# score
score = 0
score_font_as_bytes = font_in_bytes('text/Orbitron/Orbitron-VariableFont_wght.ttf')
score_dic = {
    'score': 0,
    'font_score':  pygame.font.Font(score_font_as_bytes, 32),
    'posX': 15,
    'posY': 15
}

# show level
level = 0
level_font_as_bytes = font_in_bytes('text/Orbitron/Orbitron-VariableFont_wght.ttf')
level_dic = {
    'level': 0,
    'font_level':  pygame.font.Font(level_font_as_bytes, 32),
    'posX': 15,
    'posY': 50
}

# add music
mixer.music.load('music/background/productions-racing-sport-gaming-racing(chosic.com).mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# music background
credits_music_text = "Credits music: Racing Sport Gaming | RACING by Alex-Productions | https://onsound.eu/"
credits_music_text_font_bytes = font_in_bytes('text/Teko/Teko-VariableFont_wght.ttf')
credits_music = {
    'font': pygame.font.Font(credits_music_text_font_bytes, 20),
    'posX': WIDTH - (len(credits_music_text)*6 + 10),  # add 10px margin
    'posY': HEIGHT - 26
}


# player function
def player(x, y):
    screen.blit(player_img, (x, y))


# player function
def enemy(x, y, idx_enemy):
    screen.blit(enemy_img[idx_enemy], (x, y))


# shooting function
def shooting(x, y):
    global bullet_visible
    bullet_visible = True
    screen.blit(
        bullet_img,
        (
            x + player_img.get_width()//3,
            y - player_img.get_height()//2
         )
    )


# detect collisions - distance
def detect_collisions(x1, y1, x2, y2, idx_enemy):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if distance < max(
            enemy_img[idx_enemy].get_height(), bullet_img.get_height()
    ) * 3/4:
        return True

    return False


# show score
def show_score(x, y):
    text1 = score_dic['font_score'].render(f'Score:', True, (255, 255, 255))
    text2 = score_dic['font_score'].render(f'{score_dic["score"]}', True, (255, 255, 255))
    screen.blit(text1, (x, y))
    screen.blit(text2, (x + 140, y))


# increase the game level
def level_up(current_score: int, score_check: int) -> int:
    """
    Increase the level game
    :param current_score: score to apply level up
    :param score_check: score limit to do level up
    :return: a new level
    """
    return round(current_score // score_check)


def show_level(x, y):
    text1 = level_dic['font_level'].render(f'Level:', True, (255, 255, 255))
    text2 = level_dic['font_level'].render(f'{level_dic["level"]}', True, (255, 255, 255))
    screen.blit(text1, (x, y))
    screen.blit(text2, (x + 140, y))


# Game over text
game_over_font_as_bytes = font_in_bytes(
    'text/Orbitron/static/Orbitron-ExtraBold.ttf'
)
game_over_text_setting = pygame.font.Font(game_over_font_as_bytes, 60)
game_over_text = f"{'*' * 3} GAME OVER {'*' * 3}"

# game over sound
game_over_sound = mixer.Sound('sounds_fx/evil-demonic-laugh-6925.mp3')
# game_over_sound.play()


def game_over():
    final_text = game_over_text_setting.render(
        game_over_text,
        True,
        (255, 255, 255)
    )
    screen.blit(final_text, (WIDTH//4, HEIGHT//3))
    mixer.music.stop()
    # game_over_sound.play()


# show credits_music
def show_credits_music(x, y):
    text = credits_music['font'].render(
        f"{credits_music_text}",
        True,
        (255, 255, 255)
    )
    screen.blit(text, (x, y))


# Game Loop
execution = True
while execution:

    # background - rgb
    # screen.fill((117, 163, 253))
    # background - img
    screen.blit(background, (0, 0))

    # event iteration
    for event in pygame.event.get():
        # close app
        if event.type == pygame.QUIT:
            execution = False
        # check key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:

                if not bullet_visible:
                    bulletX = playerX
                    bullet_sound.play()
                    shooting(bulletX, bulletY)
        # key fall event
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or
                    event.key == pygame.K_RIGHT):
                playerX_change = 0

    # update player position
    playerX += playerX_change

    # keep on screen and player/enemy movement
    # -----------------------------------------------------
    # keep on screen to player
    if playerX <= bound_left:
        playerX = bound_left
    elif playerX >= bound_right:
        playerX = bound_right

    # update enemy position
    for en in range(enemy_quantity):
        enemyX[en] += enemyX_change[en]

        # keep on screen to enemy
        level_up_to_move_change = level_dic['level'] / 10
        if enemyX[en] <= bound_left:
            enemyX_change[en] = generate_random_acceleration()
            # speed up with level up
            enemyX_change[en] += level_up_to_move_change
            # update acceleration
            enemyY[en] += enemyY_change[en]
        elif enemyX[en] >= bound_right:
            enemyX_change[en] = -generate_random_acceleration()
            # speed up with level up
            enemyX_change[en] -= level_up_to_move_change
            # update acceleration
            enemyY[en] += enemyY_change[en]

        # check collision
        collision = detect_collisions(enemyX[en], enemyY[en], bulletX, bulletY, en)
        if collision:
            hit_sound.play()
            bulletY = playerY
            bullet_visible = False
            score_dic['score'] += 1
            # level change - up level
            level_dic['level'] = level_up(score_dic['score'], 30)

            enemy_img[en] = random_enemy_img()
            enemyX[en], enemyY[en] = random_position(en)

        # end game
        if enemyY[en] >= playerY - 60:
            for k in range(enemy_quantity):
                enemyY[k] = HEIGHT + 100
            game_over()
            break
        enemy(enemyX[en], enemyY[en], en)

    # bullet movement
    if bulletY <= -1 * bullet_img.get_height():
        bulletY = playerY
        bullet_visible = False

    if bullet_visible:
        shooting(bulletX, bulletY)
        bulletY -= bulletY_change

    # movement fns
    player(playerX, playerY)

    # show score
    show_score(score_dic['posX'], score_dic['posY'])
    # show level
    show_level(level_dic['posX'], level_dic['posY'])
    # show credits music
    show_credits_music(credits_music['posX'], credits_music['posY'])

    # update
    pygame.display.update()

"""
Thanks to:
- icons:
    - flaticon.es
    - freepik.es

- background:
    - canva.com

- font:
    - google fonts

- sounds:
    - effect:
        - pixabay.com
    - music:
        - chosic.com

"""