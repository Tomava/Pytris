import pygame
import sys
import Coordinates
import Piece
from Config import *
from Textures import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDHT, WIN_HEIGHT))
        pygame.display.set_caption("Hello")
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font("Arial", 32)
        self.running = True
        self.playing = False
        self.pieces = []
        self.pieces.append(Piece.Piece(PIECE_WIDTH, PIECE_HEIGHT, Coordinates.Coordinates(100, 100), RED_IMAGE))

    def start(self):
        self.playing = True
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
            self.draw()
        pygame.quit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.pieces[0].get_object(), (100, 100))
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.start()
