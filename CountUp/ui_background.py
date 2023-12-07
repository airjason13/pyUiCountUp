import pygame
from .util_gif import *
from .animatedspriteobj import *
import threading
from .icon_cord_def import *


'''Mario Fist Test'''
MarioFist = '/mario_fist.gif'


class UiAnimatedBackground:
    def __init__(self, window, pygame : pygame, material_file_uri, width=0, height=0, **kwargs):
        self.window = window
        self.pygame = pygame
        self.material_file_uri = material_file_uri
        self.frames = load_gif(material_file_uri)
        self.bg_animated_sprite = AnimatedSpriteObject(self.window.get_width() / 2, self.window.get_height(), self.frames)
        self.bg_sprites = pygame.sprite.Group(self.bg_animated_sprite)
        self.is_start_drawing = False

        self.mario_frames = load_gif('Image/mario_fist.gif')
        self.mario_sprite = AnimatedSpriteObject(870, 560, self.mario_frames)
        self.mario_sprites = pygame.sprite.Group(self.mario_sprite)
        self.is_start_drawing = False

    def start_drawing(self):
        self.is_start_drawing = True

    def stop_drawing(self):
        self.is_start_drawing = False

    def update_bg(self):
        while True:
            if self.start_drawing is False:
                return

            #print("draw bg")
            self.bg_sprites.update()
            # self.bg_sprites.draw(self.window)
            # self.pygame.display.flip()
            #print("draw bg ok")

    def draw(self):
        self.bg_sprites.update()
        self.mario_sprites.update()
        self.bg_sprites.draw(self.window)
        self.mario_sprites.draw(self.window)



