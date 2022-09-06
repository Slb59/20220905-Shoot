import pygame
from player import Player
from monster import Monster

class Game():
    def __init__(self):
        # generation du joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # creation du groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        # ensemble des touches utilisees
        self.pressed = {}
        # spawn un premier monstre
        self.spawn_monster()
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)