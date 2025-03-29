import pygame
import random
from pygame import mixer

pygame.init()
pygame.font.init()
mixer.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodge the falling bricks!")

colors = {
    "white": (255, 255, 255),
    "blue": (0, 0, 255),
    "red": (255, 0, 0)
}

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (50, 50))
brick = pygame.image.load("bricks"
".png")
brick = pygame.transform.scale(brick, (50, 50))



# Song: Tobu & Diviners - Geometry
# Music provided by NoCopyrightSounds
# Free Download/Stream: http://ncs.io/Geometry
# Watch: http://ncs.lnk.to/GeometryAT/youtube
mixer.music.load("ost.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 5

obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Game Over!", True, pygame.Color("black"), None)
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

score = 0


running = True
clock = pygame.time.Clock()
while running:
    screen.fill(colors["white"])
    screen.blit(bg, (0, 0))

    scoreText = font.render("Score: "+ str(score), True, pygame.Color("black"), None)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed

    obstacle_y += obstacle_speed
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
        score += 1

    if (
        player_x < obstacle_x + obstacle_width and
        player_x + player_size > obstacle_x and
        player_y < obstacle_y + obstacle_height and
        player_y + player_size > obstacle_y
    ):
        screen.blit(text, textRect)
        running = False


    screen.blit(player, (player_x, player_y))
    screen.blit(brick, (obstacle_x, obstacle_y))

    screen.blit(scoreText, (0,0))
    pygame.display.update()
    clock.tick(30)