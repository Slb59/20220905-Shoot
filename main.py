import pygame

pygame.init()

# generer la fenetre du jeu


pygame.display.set_caption("Jeu de shooter")
# TODO : Changer le titre du jeu et ajouter une icone de jeu

screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')
running = True

# boucle de jeu

while running:

    # appliquer l'arriere plan
    screen.blit(background,(0,-200))

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():

        # evenement fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")


