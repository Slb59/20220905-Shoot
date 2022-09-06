import pygame
from game import Game

pygame.init()

# generer la fenetre du jeu


pygame.display.set_caption("Jeu de shooter")
# TODO : Changer le titre du jeu et ajouter une icone de jeu

screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

# charger le jouer
game = Game()

running = True

# boucle de jeu

while running:

    # appliquer l'arriere plan
    screen.blit(background, (0, -200))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recupere les monstres du jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # appliquer les images du groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # appliquer les images du groupe de monstre
    game.all_monsters.draw(screen)

    # verifier si le joueur souhaite aller à gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():

        # evenement fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                print('envoi un projectile')
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False







