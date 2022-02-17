from GameAssets import Coordinates
from GameAssets.SubPiece import SubPiece
from Config import GAME_WIDTH
from GameAssets.Piece import Piece
from Textures import *


class SquarePiece(Piece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates, ghost=False):
        self.texture = YELLOW_IMAGE
        if ghost:
            self.texture = YELLOW_GHOST_IMAGE
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates)
        if not ghost:
            self.ghost = SquarePieceGhost(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates)
        self.update_ghost()

    def create_piece(self):
        # Topleft
        coords_0 = Coordinates.Coordinates(int(GAME_WIDTH / 2) - self.piece_width, 0)
        self.list_of_subpieces.append(
            SubPiece(self.piece_width, self.piece_height, coords_0, self.texture, self.vertical_rate,
                     self.horizontal_rate, self.ground_coordinates))
        coords_1 = Coordinates.Coordinates(int(GAME_WIDTH / 2), 0)
        self.list_of_subpieces.append(
            SubPiece(self.piece_width, self.piece_height, coords_1, self.texture, self.vertical_rate,
                     self.horizontal_rate, self.ground_coordinates))
        coords_2 = Coordinates.Coordinates(int(GAME_WIDTH / 2) - self.piece_width, self.piece_height)
        self.list_of_subpieces.append(
            SubPiece(self.piece_width, self.piece_height, coords_2, self.texture, self.vertical_rate,
                     self.horizontal_rate, self.ground_coordinates))
        coords_3 = Coordinates.Coordinates(int(GAME_WIDTH / 2), self.piece_height)
        self.list_of_subpieces.append(
            SubPiece(self.piece_width, self.piece_height, coords_3, self.texture, self.vertical_rate,
                     self.horizontal_rate, self.ground_coordinates))


class SquarePieceGhost(SquarePiece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates):
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates, True)
