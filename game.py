import pygame
import random
import sys
import os

pygame.init()

# sound module init

pygame.mixer.init()

# gamescreen

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Happy Hedgehog")

clock = pygame.time.Clock()

# for exe file


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# background


def play_background_music(music_path):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)


background_image = pygame.image.load(resource_path("./images/background.png"))
background_image = pygame.transform.scale(
    background_image, (screen_width, screen_height)
)

background_music = resource_path("./sounds/background_music.mp3")
gameover_music = resource_path("./sounds/gameover.mp3")

collision_sound = pygame.mixer.Sound(resource_path("./sounds/collision.mp3"))
collision_sound.set_volume(1.0)

play_background_music(background_music)

# score

score = 0

# high score

high_score = 0

try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0


def check_highscore(score, high_score):
    if score > high_score:
        high_score = score
        with open("highscore.txt", "w") as file:
            file.write(str(high_score))
    return high_score


# level

level = 1


# colors

background_white = (255, 255, 255)  # background

# player
player_image = pygame.image.load(resource_path("./images/hedgehog.png"))
player_image = pygame.transform.scale(player_image, (50, 50))
player_width, player_height = 50, 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# obstacle
obstacle_image = pygame.image.load(resource_path("./images/stone.png"))
obstacle_image = pygame.transform.scale(obstacle_image, (50, 50))
obstacle_width, obstacle_height = 50, 50
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5
obstacle_count = 5
obstacles = []

# obstacle init

for _ in range(obstacle_count):
    obstacle_x = random.randint(0, screen_width - obstacle_width)
    obstacle_y = random.randint(-screen_height, 0)
    obstacles.append([obstacle_x, obstacle_y])


def draw_text(surface, text, size, x, y, color=(0, 0, 0)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)


# main game loop

running = True
game_over = False

while running:
    if game_over == True:
        screen.fill(background_white)

        high_score = check_highscore(score, high_score)

        draw_text(
            screen,
            "Game Over",
            60,
            screen_width // 2,
            screen_height // 2 - 30,
            (255, 0, 0),
        )
        draw_text(
            screen,
            "Press R to restart",
            40,
            screen_width // 2,
            screen_height // 2 + 30,
            (0, 0, 0),
        )
        draw_text(
            screen,
            f"You earned {score} points!",
            30,
            screen_width // 2,
            screen_height // 2 - 100,
            (0, 0, 0),
        )
        draw_text(
            screen,
            f"High score: {high_score}",
            30,
            screen_width // 2,
            screen_height // 2 - 130,
            (0, 0, 0),
        )
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # game restart
                    game_over = False
                    play_background_music(background_music)
                    score = 0
                    obstacle_speed = 5
                    player_speed = 5
                    level = 0
                    player_x = screen_width // 2 - player_width // 2
                    player_y = screen_height - player_height - 10
                    obstacles = [
                        [
                            random.randint(0, screen_width - obstacle_width),
                            random.randint(-screen_height, 0),
                        ]
                        for _ in range(obstacle_count)
                    ]
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_speed = 10
        if keys[pygame.K_DOWN]:
            player_speed = 5

        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if obstacle[1] > screen_height:
                obstacle[1] = -obstacle_height
                obstacle[0] = random.randint(0, screen_width - obstacle_width)

        # background, player and obstacles
        screen.blit(background_image, (0, 0))
        screen.blit(player_image, (player_x, player_y))
        for obstacle in obstacles:
            screen.blit(obstacle_image, (obstacle[0], obstacle[1]))
            if (
                player_x < obstacle[0] + obstacle_width
                and player_x + player_width > obstacle[0]
                and player_y < obstacle[1] + obstacle_height
                and player_y + player_height > obstacle[1]
            ):
                play_background_music(gameover_music)
                collision_sound.play()
                game_over = True

        draw_text(screen, f"Score: {score}", 40, screen_width // 2, 30, (0, 0, 0))
        draw_text(
            screen, f"High score: {high_score}", 35, screen_width - 120, 30, (0, 0, 0)
        )
        draw_text(screen, f"Level: {level}", 35, 120, 30, (0, 0, 0))

    if not game_over:
        score += 1  # score per tick
        if score % 200 == 0:
            obstacle_speed += 0.2
        if score % 400 == 0:
            level += 1

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
