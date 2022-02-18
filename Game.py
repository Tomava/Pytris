import random

from GameAssets.GroundedPiece import GroundedPiece
from GameAssets.JPiece import JPiece
from GameAssets.LPiece import LPiece
from GameAssets.SquarePiece import SquarePiece
from GameAssets.SPiece import SPiece
from GameAssets.ZPiece import ZPiece
from GameAssets.TPiece import TPiece
from GameAssets.IPiece import IPiece
from GameAssets.Coordinates import Coordinates
from Config import *
from Textures import *


class Game:
    def __init__(self):
        self.current_piece = None
        self.next_piece = None
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Hello")
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font("Arial", 32)
        self.pieces = set(x for x in range(0, 7))
        self.next_indexes = []
        self.next_pieces = []
        self.get_next_indexes()
        self.running = True
        self.playing = False
        self.has_rotated = False
        self.has_dropped = False
        self.ground_piece = GroundedPiece(PIECE_WIDTH, PIECE_HEIGHT, 10)
        self.handle_piece_creation()
        self.score = 0
        self.score_text = SCORE_FONT.render(str(self.score), True, (255, 255, 255))
        self.got_tetris = 0
        self.cleared_lines = 0

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

    def get_next_indexes(self):
        while len(self.next_indexes) < NEXT_PIECES:
            if len(self.pieces) < 1:
                self.pieces = set(x for x in range(0, 7))
            next_index = random.choice(tuple(self.pieces))
            self.next_indexes.append(next_index)
            self.pieces.remove(next_index)

    def create_piece(self, index, coordinates):
        match index:
            case 0:
                current_piece = JPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100, coordinates,
                                       self.ground_piece.get_occupied_coordinates())
            case 1:
                current_piece = SquarePiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100, coordinates,
                                            self.ground_piece.get_occupied_coordinates())
            case 2:
                current_piece = LPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100, coordinates,
                                       self.ground_piece.get_occupied_coordinates())
            case 3:
                current_piece = SPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100, coordinates,
                                       self.ground_piece.get_occupied_coordinates())
            case 4:
                current_piece = ZPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100, coordinates,
                                       self.ground_piece.get_occupied_coordinates())
            case 5:
                current_piece = TPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100, coordinates,
                                       self.ground_piece.get_occupied_coordinates())
            case 6:
                current_piece = IPiece(PIECE_WIDTH, PIECE_HEIGHT, 400, 100, coordinates,
                                       self.ground_piece.get_occupied_coordinates())
        return current_piece

    def handle_scoring(self, removed_lines):
        if removed_lines == 0:
            return
        score = SCORING.get(removed_lines)
        if removed_lines == 4:
            score += self.got_tetris * SCORING.get(4)
            self.got_tetris = 0.5
        else:
            self.got_tetris = 0
        self.score += score
        self.score_text = SCORE_FONT.render(str(self.score), True, (255, 255, 255))
        self.cleared_lines += removed_lines

    def handle_piece_creation(self):
        self.current_piece = self.create_piece(self.next_indexes[0], Coordinates(int(GAME_WIDTH / 2) - 2 * PIECE_WIDTH, 0))
        self.next_indexes.pop(0)
        self.get_next_indexes()
        offset_y = 0
        self.next_pieces.clear()
        for index in self.next_indexes:
            self.next_pieces.append(self.create_piece(index, Coordinates(GAME_WIDTH + WIN_OFFSET_X / 6, offset_y)))
            offset_y += 4 * 32

    def update(self):
        self.current_piece.move_down()
        if self.current_piece.get_ground_time() != -1:
            removed_lines = self.ground_piece.add_pieces(self.current_piece.get_subpieces())
            self.handle_scoring(removed_lines)
            self.handle_piece_creation()

    def draw(self):
        self.screen.fill((55, 0, 155))
        self.screen.blit(pygame.transform.scale(BACKGROUND, (GAME_WIDTH, GAME_HEIGHT)), (GAME_OFFSET_X, GAME_OFFSET_Y))
        for piece_object in self.current_piece.get_ghost().get_subpieces():
            self.screen.blit(piece_object.get_object(), piece_object.get_coordinates().get_tuple())
        for piece_object in self.current_piece.get_subpieces():
            self.screen.blit(piece_object.get_object(), piece_object.get_coordinates().get_tuple())
        for piece_object in self.ground_piece.get_subpieces():
            self.screen.blit(piece_object.get_object(), piece_object.get_coordinates().get_tuple())
        for next_piece in self.next_pieces:
            for piece_object in next_piece.get_subpieces():
                self.screen.blit(piece_object.get_object(), piece_object.get_coordinates().get_tuple())
        self.screen.blit(self.score_text, (14, 14))
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
