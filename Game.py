import random

from GameAssets.GroundedPiece import GroundedPiece
from GameAssets.JPiece import JPiece
from GameAssets.LPiece import LPiece
from GameAssets.SquarePiece import SquarePiece
from GameAssets.SPiece import SPiece
from GameAssets.ZPiece import ZPiece
from GameAssets.TPiece import TPiece
from GameAssets.IPiece import IPiece
from Config import *
from Textures import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Hello")
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font("Arial", 32)
        self.pieces = set(x for x in range(0, 7))
        self.current_piece = None
        self.running = True
        self.playing = False
        self.has_rotated = False
        self.has_dropped = False
        self.ground_piece = GroundedPiece(PIECE_WIDTH, PIECE_HEIGHT, 10)
        self.create_piece()

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

    def create_piece(self):
        if len(self.pieces) < 1:
            self.pieces = set(x for x in range(0, 7))
        i = random.choice(tuple(self.pieces))
        match i:
            case 0:
                self.current_piece = JPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100,
                                            self.ground_piece.get_occupied_coordinates())
            case 1:
                self.current_piece = SquarePiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100,
                                                 self.ground_piece.get_occupied_coordinates())
            case 2:
                self.current_piece = LPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100,
                                            self.ground_piece.get_occupied_coordinates())
            case 3:
                self.current_piece = SPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100,
                                            self.ground_piece.get_occupied_coordinates())
            case 4:
                self.current_piece = ZPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100,
                                            self.ground_piece.get_occupied_coordinates())
            case 5:
                self.current_piece = TPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100,
                                            self.ground_piece.get_occupied_coordinates())
            case 6:
                self.current_piece = IPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100,
                                            self.ground_piece.get_occupied_coordinates())
        self.pieces.remove(i)

    def update(self):
        self.current_piece.move_down()
        if self.current_piece.get_ground_time() != -1:
            self.ground_piece.add_pieces(self.current_piece.get_subpieces())
            self.create_piece()

    def draw(self):
        self.screen.blit(pygame.transform.scale(BACKGROUND, (WIN_WIDTH, WIN_HEIGHT)), (0, 0))
        for piece_object in self.current_piece.get_ghost().get_subpieces():
            self.screen.blit(piece_object.get_object(), piece_object.get_coordinates().get_tuple())
        for piece_object in self.current_piece.get_subpieces():
            self.screen.blit(piece_object.get_object(), piece_object.get_coordinates().get_tuple())
        for piece_object in self.ground_piece.get_subpieces():
            self.screen.blit(piece_object.get_object(), piece_object.get_coordinates().get_tuple())
        pygame.display.update()

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.current_piece.move_left()
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.current_piece.move_right()
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.current_piece.speed_up()
        else:
            self.current_piece.speed_down()
        if keys_pressed[pygame.K_SPACE]:
            if not self.has_dropped:
                self.has_dropped = True
                self.current_piece.drop_down()
        else:
            self.has_dropped = False
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            if not self.has_rotated:
                self.has_rotated = True
                self.current_piece.rotate()
        else:
            self.has_rotated = False


if __name__ == "__main__":
    game = Game()
    game.start()
