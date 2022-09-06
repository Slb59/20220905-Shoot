import pygame

pygame.init()

# generer la fenetre du jeu


pygame.display.set_caption("Jeu de shooter")
# TODO : Changer le titre du jeu et ajouter une icone de jeu

pygame.display.set_mode((1080, 720))

running = True

# boucle de jeu

while running:

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():

        # evenement fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")


