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
obstacle_count = 5
obstacles = []

#obstacle init

for _ in range(obstacle_count):
    obstacle_x = random.randint(0, screen_width - obstacle_width)
    obstacle_y = random.randint(-screen_height, 0)
    obstacles.append([obstacle_x, obstacle_y])

def draw_text(surface, text, size, x, y, color = (0,0,0)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    surface.blit(text_surface, text_rect)

#main game loop

running = True
game_over = False

while running:
    if game_over == True:
        screen.fill(background_white)
        draw_text(screen, 'Game Over', 60, screen_width // 2, screen_height // 2 - 30, (255,0,0))
        draw_text(screen, "Press R to restart", 40, screen_width // 2, screen_height // 2 + 30, (0,0,0))
        pygame.display.flip()
        # pygame.time.wait(1000)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # game restart
                    game_over = False
                    player_x = screen_width // 2 - player_width // 2
                    player_y = screen_height - player_height - 10
                    obstacles = [
                        [random.randint(0, screen_width - obstacle_width), random.randint(-screen_height, 0)]
                        for _ in range(obstacle_count)
                    ]
    
    
    
    
    
    
    
    
    
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        
        #keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed
            
            
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if obstacle[1] > screen_height:
                obstacle[1] = -obstacle_height
                obstacle[0] = random.randint(0, screen_width - obstacle_width)

        
        #background, player and obstacles
        screen.fill(background_white)
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
        for obstacle in obstacles:
            pygame.draw.rect(screen, obstacle_color, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))
            
            if ( 
            player_x < obstacle[0] + obstacle_width and
            player_x + player_width > obstacle[0] and
            player_y < obstacle[1] + obstacle_height and
            player_y + player_height > obstacle[1]
            ):
                game_over = True
                break
        
    
        
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()









