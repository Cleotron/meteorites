import pygame, sys
import random

pygame.init()
pygame.font.init()

def create_meteorite(list):
    x = random.randint(0, 800)
    y = 0
    list.append([x, y])
    return [x, y]

#define colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

#screen
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#player
player_x = 375
player_y = 590
player_speed = 0
player_width = 50
player_height = 10
score = 0
game_over = False

#meteorites
coord_white = []
coord_blue = []
milliseconds_until_event = random.randint(500, 2001)
milliseconds_since_event = 0

while not game_over:
    milliseconds_since_event += clock.tick(150)
    font = pygame.font.Font(None, 36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
        currently_pressed = pygame.key.get_pressed()
        player_speed = currently_pressed[pygame.K_RIGHT] * 4 - currently_pressed[pygame.K_LEFT] * 4

    screen.fill(black)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    player = pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
    
    player_x += player_speed
    if player_x <= 1:
        player_x = 1
    if player_x >= 750:
        player_x = 750

    if milliseconds_since_event > milliseconds_until_event:
        m1 = create_meteorite(coord_white)
        m2 = create_meteorite(coord_blue)
        if m1 == m2:
            coord_white.remove(m1)
        milliseconds_until_event = random.randint(500, 2001)
        milliseconds_since_event = 0

    for j in coord_white:
        meteore_white = pygame.draw.circle(screen, white, j, 3)
        j[1] += 1
        #create_meteorite(coord_white)
        if j[1] >= 600:
            coord_white.remove(j)

        if meteore_white.colliderect(player):
            game_over = True
            game_over_text = font.render(f'GAME OVER', True, (255, 255, 255))
            screen.blit(game_over_text, (320, 300))

    for j in coord_blue:
        meteore_blue = pygame.draw.circle(screen, blue, j, 3)
        j[1] += 1
        if meteore_blue.colliderect(player):
            coord_blue.remove(j)
            score += 1
        if j[1] >= 600:
            coord_blue.remove(j)

    pygame.display.flip()
    clock.tick (100)