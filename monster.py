import pygame
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.health = 100
        self.max_health = 100
        self.attack = 0.3

        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        # TODO : recuperer la taille de l'écran
        self.rect.y = 540 - offset


        # TODO : mettre une vitesse aleatoire

        self.game = game

        self.start_animation()

        self.loot_amount = 0



    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, self.default_speed)

    def damage(self, amount):
        # infliger les degats
        self.health -= amount
        # verifie si le nb de points de vie >0
        if self.health <= 0:
            # respawn un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health

            # si la barre d'evenement chargee à son maxi
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                # essayer de declencher la pluie de cometes
                self.game.comet_event.attempt_fall()

            # ajouter le nb de points au score
            self.game.add_score(self.loot_amount)

    def set_loot_amount(self, amount):
        self.loot_amount += amount

    def update_animation(self):
        self.animate(True)
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

# definir une classe pour gerer la momie

class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

# definir une classe pour gerer un alien

class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.set_speed(1)
        self.attack = 0.8
        self.set_loot_amount(80)