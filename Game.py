import pygame
import sys
import Coordinates
import SubPiece
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
        self.current_piece = SubPiece.SubPiece(WIN_WIDHT, WIN_HEIGHT, PIECE_WIDTH, PIECE_HEIGHT, Coordinates.Coordinates(100, 100), RED_IMAGE, 400, 100)
        self.pieces.append(self.current_piece)

    def start(self):
        self.playing = True
        while self.running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.handle_movement(pygame.key.get_pressed())
            self.update()
            self.draw()
        pygame.quit()

    def update(self):
        self.current_piece.move_down()

    def draw(self):
        self.screen.fill((255, 255, 255))
        for piece in self.pieces:
            self.screen.blit(piece.get_object(), piece.get_coordinates())
        pygame.display.update()

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_a]:
            self.current_piece.move_left()
        if keys_pressed[pygame.K_d]:
            self.current_piece.move_right()


if __name__ == "__main__":
    game = Game()
    game.start()
