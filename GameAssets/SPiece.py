from GameAssets import Coordinates
from GameAssets.SubPiece import SubPiece
from Config import GAME_WIDTH
from GameAssets.Piece import Piece
from Textures import *
from copy import copy


class SPiece(Piece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates, ghost=False):
        self.texture = GREEN_IMAGE
        if ghost:
            self.texture = GREEN_GHOST_IMAGE
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates)
        if not ghost:
            self.ghost = SPieceGhost(piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates)
        self.update_ghost()

    def create_piece(self):
        coords_0 = copy(self.top_left_coordinates)
        coords_0.add_x_and_y(0, self.piece_height)
        self.list_of_subpieces.append(SubPiece(self.piece_width, self.piece_height, coords_0,
                                               self.texture, self.vertical_rate, self.horizontal_rate,
                                               self.ground_coordinates))
        coords_1 = copy(self.top_left_coordinates)
        coords_1.add_x_and_y(self.piece_width, self.piece_height)
        self.list_of_subpieces.append(SubPiece(self.piece_width, self.piece_height, coords_1,
                                               self.texture, self.vertical_rate, self.horizontal_rate,
                                               self.ground_coordinates))
        coords_2 = copy(self.top_left_coordinates)
        coords_2.add_x_and_y(self.piece_width, 0)
        self.list_of_subpieces.append(SubPiece(self.piece_width, self.piece_height, coords_2,
                                               self.texture, self.vertical_rate, self.horizontal_rate,
                                               self.ground_coordinates))
        coords_3 = copy(self.top_left_coordinates)
        coords_3.add_x_and_y(2 * self.piece_width, 0)
        self.list_of_subpieces.append(SubPiece(self.piece_width, self.piece_height, coords_3,
                                               self.texture, self.vertical_rate, self.horizontal_rate,
                                               self.ground_coordinates))

    def rotate(self):
        movements = []
        if self.rotation == 0:
            movements.extend([(self.piece_width, -self.piece_height), (0, 0), (self.piece_width, self.piece_height),
                              (0, 2 * self.piece_height)])
        elif self.rotation == 1:
            movements.extend([(self.piece_width, self.piece_height), (0, 0),
                              (-self.piece_width, self.piece_height), (-2 * self.piece_width, 0)])
        elif self.rotation == 2:
            movements.extend([(-self.piece_width, self.piece_height), (0, 0),
                              (-self.piece_width, -self.piece_height), (0, -2 * self.piece_height)])
        elif self.rotation == 3:
            movements.extend([(-self.piece_width, -self.piece_height), (0, 0),
                              (self.piece_width, -self.piece_height), (2 * self.piece_width, 0)])
        if self.rotate_subpieces(movements):
            self.rotation += 1
            if self.rotation > 3:
                self.rotation = 0


class SPieceGhost(SPiece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates):
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates, True)