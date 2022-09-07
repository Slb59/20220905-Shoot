import pygame
import math
from game import Game

pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60


# generer la fenetre du jeu


pygame.display.set_caption("Jeu de shooter")
# TODO : Changer le titre du jeu et ajouter une icone de jeu

screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')

# importer la banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# charge le bouton play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jouer
game = Game()

running = True

# boucle de jeu

while running:

    # appliquer l'arriere plan
    screen.blit(background, (0, -200))

    # verifie si le jeu a commencé
    if game.is_playing:
        game.update(screen)
    else:
        # le jeu n'a pas commencé
        # ajouter l'écran de bienvenu
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

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
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifie si la souris est en collision avec le bouton play
            if play_button_rect.collidepoint(event.pos):
                # lancement du jeu
                game.start()

    clock.tick(FPS)




