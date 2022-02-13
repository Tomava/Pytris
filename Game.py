import pygame
import sys
import Coordinates
import GroundedPiece
import JPiece
import SubPiece
import SquarePiece
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
        self.has_rotated = False
        self.pieces = []
        self.current_piece = JPiece.JPiece(WIN_WIDHT, WIN_HEIGHT, PIECE_WIDTH, PIECE_HEIGHT, 400, 100, set())
        ground_piece = GroundedPiece.GroundedPiece(WIN_WIDHT, WIN_HEIGHT, PIECE_WIDTH, PIECE_HEIGHT)
        ground_piece.add_pieces(self.current_piece.get_subpieces())
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
            for piece_object in piece.get_subpieces():
                self.screen.blit(piece_object.get_object(), piece_object.get_coordinates().get_tuple())
        pygame.display.update()

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_a]:
            self.current_piece.move_left()
        if keys_pressed[pygame.K_d]:
            self.current_piece.move_right()
        if keys_pressed[pygame.K_w]:
            if not self.has_rotated:
                self.has_rotated = True
                self.current_piece.rotate()
        else:
            self.has_rotated = False


if __name__ == "__main__":
    game = Game()
    game.start()
