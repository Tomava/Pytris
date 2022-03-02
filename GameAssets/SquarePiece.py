from GameAssets import Coordinates
from GameAssets.SubPiece import SubPiece
from Config import GAME_WIDTH
from GameAssets.Piece import Piece
from Textures import *
from copy import copy


class SquarePiece(Piece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates, index, ghost=False):
        self.texture = YELLOW_IMAGE
        if ghost:
            self.texture = YELLOW_GHOST_IMAGE
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates, index)
        if not ghost:
            self.ghost = SquarePieceGhost(piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates, index)
        self.update_ghost()

    def create_piece(self):
        # Topleft
        coords_0 = copy(self.top_left_coordinates)
        coords_0.add_x_and_y(self.piece_width, 0)
        coords_1 = copy(self.top_left_coordinates)
        coords_1.add_x_and_y(2 * self.piece_width, 0)
        coords_2 = copy(self.top_left_coordinates)
        coords_2.add_x_and_y(self.piece_width, self.piece_height)
        coords_3 = copy(self.top_left_coordinates)
        coords_3.add_x_and_y(2 * self.piece_width, self.piece_height)
        self.list_of_subpieces.append(
            SubPiece(self.piece_width, self.piece_height, coords_0, self.texture, self.vertical_rate,
                     self.horizontal_rate, self.ground_coordinates))
        self.list_of_subpieces.append(
            SubPiece(self.piece_width, self.piece_height, coords_1, self.texture, self.vertical_rate,
                     self.horizontal_rate, self.ground_coordinates))
        self.list_of_subpieces.append(
            SubPiece(self.piece_width, self.piece_height, coords_2, self.texture, self.vertical_rate,
                     self.horizontal_rate, self.ground_coordinates))
        self.list_of_subpieces.append(
            SubPiece(self.piece_width, self.piece_height, coords_3, self.texture, self.vertical_rate,
                     self.horizontal_rate, self.ground_coordinates))


class SquarePieceGhost(SquarePiece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates, index):
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, top_left_coordinates, ground_coordinates, index, True)
