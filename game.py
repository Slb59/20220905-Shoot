import pygame
from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent

class Game():
    def __init__(self):
        # definir si le jeu à commencer
        self.is_playing = False
        # generation du joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # creation du groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        # ensemble des touches utilisees
        self.pressed = {}
        # generer le manager de comete
        self.comet_event = CometFallEvent(self)
        # chargement de la police
        self.font = pygame.font.Font("assets/my_custom_font.ttf", 25)
        # mettre le score a 0
        self.score = 0


    def start(self):
        self.is_playing = True
        # spawn un premier monstre
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        # remettre le jeu a neuf
        # retirer les monstres
        self.all_monsters = pygame.sprite.Group()

        # remettre les vies au joueur
        self.player.health = self.player.max_health

        # remettre le jeu en attente
        self.is_playing = False

        # retirer les cometes
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()

        self.score = 0

    def add_score(self, points=10):
        self.score += points



    def update(self, screen):

        # afficher le score

        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'evenement
        self.comet_event.update_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recupere les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuperer les comets du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer les images du groupe d ecomets
        self.comet_event.all_comets.draw(screen)

        # appliquer les images du groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer les images du groupe de monstre
        self.all_monsters.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
         self.all_monsters.add(monster_class_name.__call__(self))