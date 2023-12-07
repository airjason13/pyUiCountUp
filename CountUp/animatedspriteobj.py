import pygame


class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (x, bottom))
        self.image_index = 0

    def update(self):
        self.image_index += 1
        if self.image_index >= len(self.images):
            self.image_index = 0
        self.image = self.images[self.image_index]