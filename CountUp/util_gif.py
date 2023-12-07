from PIL import Image, ImageSequence
import pygame


def load_gif(filename):
    pil_image = Image.open(filename)
    frames = []
    pygame_image = None
    for frame in ImageSequence.Iterator(pil_image):
        frame = frame.convert('RGBA')
        pygame_image = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygame_image)
    return frames
