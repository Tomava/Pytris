import Coordinates
import SubPiece
from Config import GAME_WIDTH
from Piece import Piece
from Textures import *


class TPiece(Piece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates, ghost=False):
        self.texture = PURPLE_IMAGE
        if ghost:
            self.texture = PURPLE_GHOST_IMAGE
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates)
        if not ghost:
            self.ghost = TPieceGhost(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates)
        self.update_ghost()

    def create_piece(self):
        coords_0 = Coordinates.Coordinates(int(GAME_WIDTH / 2) - self.piece_width, 0)
        self.list_of_subpieces.append(SubPiece.SubPiece(self.piece_width, self.piece_height, coords_0,
                                                        self.texture, self.vertical_rate, self.horizontal_rate,
                                                        self.ground_coordinates))
        coords_1 = Coordinates.Coordinates(int(GAME_WIDTH / 2) - 2 * self.piece_width, self.piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(self.piece_width, self.piece_height, coords_1,
                                                        self.texture, self.vertical_rate, self.horizontal_rate,
                                                        self.ground_coordinates))
        coords_2 = Coordinates.Coordinates(int(GAME_WIDTH / 2) - self.piece_width, self.piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(self.piece_width, self.piece_height, coords_2,
                                                        self.texture, self.vertical_rate, self.horizontal_rate,
                                                        self.ground_coordinates))
        coords_3 = Coordinates.Coordinates(int(GAME_WIDTH / 2), self.piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(self.piece_width, self.piece_height, coords_3,
                                                        self.texture, self.vertical_rate, self.horizontal_rate,
                                                        self.ground_coordinates))

    def rotate(self):
        movements = []
        if self.rotation == 0:
            movements.extend([(self.piece_width, self.piece_height), (self.piece_width, -self.piece_height), (0, 0),
                              (-self.piece_width, self.piece_height)])
        elif self.rotation == 1:
            movements.extend([(-self.piece_width, self.piece_height), (self.piece_width, self.piece_height),
                              (0, 0), (-self.piece_width, -self.piece_height)])
        elif self.rotation == 2:
            movements.extend([(-self.piece_width, -self.piece_height), (-self.piece_width, self.piece_height),
                              (0, 0), (self.piece_width, -self.piece_height)])
        elif self.rotation == 3:
            movements.extend([(self.piece_width, -self.piece_height), (-self.piece_width, -self.piece_height),
                              (0, 0), (self.piece_width, self.piece_height)])
        if self.rotate_subpieces(movements):
            self.rotation += 1
            if self.rotation > 3:
                self.rotation = 0

class TPieceGhost(TPiece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates):
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates, True)
