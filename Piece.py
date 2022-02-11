import pygame


class Piece:
    def __init__(self, width, height, coordinates, texture):
        self.WIDTH = width
        self.HEIGHT = height
        self.coordinates = coordinates
        self.texture = texture
        self.object = pygame.transform.scale(self.texture, (self.WIDTH, self.HEIGHT))

    def get_object(self):
        return self.object
