import pygame

from game import Game
import math

pygame.init()

# Generer la fenetre
pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.75)

game = Game()

running = True

# Main loop
while running:
    # On met notre bg sur le jeu et on met à jour l ecran
    screen.blit(background, (0, -200))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Close game")
        elif e.type == pygame.KEYDOWN:
            game.pressed[e.key] = True

            if e.key == pygame.K_z:
                game.player.launch_projectile()
        elif e.type == pygame.KEYUP:
            game.pressed[e.key] = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(e.pos):
                game.start()
