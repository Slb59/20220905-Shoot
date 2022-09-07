import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 0.3

        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        # TODO : recuperer la taille de l'écran
        self.rect.y = 540

        self.velocity = random.randint(1, 3)
        # TODO : mettre une vitesse aleatoire

        self.game = game

    def damage(self, amount):
        # infliger les degats
        self.health -= amount
        # verifie si le nb de points de vie >0
        if self.health <= 0:
            # respawn un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

            # si la barre d'evenement chargee à son maxi
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                # essayer de declencher la pluie de cometes
                self.game.comet_event.attempt_fall()


    def update_health_bar(self, surface):

        # dessin de la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        # verifie pas de collision avec un joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

        # si le monstre est en collision avec le joueur
        else:
            #infliger des degats au joueur
            self.game.player.damage(self.attack)

