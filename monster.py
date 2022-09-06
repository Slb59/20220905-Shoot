import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5

        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        # TODO : recuperer la taille de l'écran
        self.rect.y = 540

        self.velocity = 2
        # TODO : mettre une vitesse aleatoire

        self.game = game

    def forward(self):
        # verifie pas de collision avec un joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
