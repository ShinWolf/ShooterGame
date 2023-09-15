import pygame

from game import Game

pygame.init()

# Generer la fenetre
pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

game = Game()

running = True

# Main loop
while running:
    # On met notre bg sur le jeu et on met à jour l ecran
    screen.blit(background, (0, -200))
    screen.blit(game.player.image, game.player.rect)

    for p in game.player.all_projectiles:
        p.move()

    game.player.all_projectiles.draw(screen)

    for m in game.all_monsters:
        m.forward()
        m.update_health_bar(screen)

    game.all_monsters.draw(screen)

    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()

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
