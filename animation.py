import pygame
import random


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animate(self, loop = False):

        #verifie si l'animation est active
        if self.animation:

            # passer a l'image suivante
            self.current_image += random.randint(0, 1)

            # verifie si atteint la fin de l'animation
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False

            # modifier l'image de l'animation courante
            self.image = self.images[self.current_image]


# charger les images d'un sprite
def load_animation_images(sprite_name):
    images = []
    # recuperer le chemin du dossier
    path = f'assets/{sprite_name}/{sprite_name}'
    # boucle sur chaque image du dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images


# dictionnaire des images chargées de chaque sprite
# mummy -> [mummy1.png, ...]
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player')
}
