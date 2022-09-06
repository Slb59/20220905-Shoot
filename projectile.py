import pygame

# class qui gère le projectile du joueur
class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.player = player
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x  += self.velocity
        self.rotate()

        # verifie si le projectile entre en collision avec un monstre
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()

        # verifie si le projectile n'est plus present sur l'ecran
        if self.rect.x > 1080:
            # supprimer le projectile
            self.remove()
            print('projectile supprimé')


