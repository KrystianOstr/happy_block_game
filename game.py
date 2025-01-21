import pygame
import random

pygame.init()

#gamescreen

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Happy Block - Step 1")

clock = pygame.time.Clock()

#colors

background_white = (255,255,255) #background

#player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
player_color = (0,0,255)

#obstacle
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5
obstacle_color = (255,0,0)

#main game loop

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    #keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
        
    obstacle_y += obstacle_speed
    if obstacle_y > screen_height:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, screen_width - obstacle_width)
    print(f"Obstacle position: x={obstacle_x}, y={obstacle_y}")
    #background and player
    screen.fill(background_white)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()









