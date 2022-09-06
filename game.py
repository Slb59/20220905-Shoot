import pygame
from player import Player

class Game():
    def __init__(self):
        # generation du joueur
        self.player = Player()
        self.pressed = {}