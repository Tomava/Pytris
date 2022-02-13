from Piece import Piece
import SubPiece
from Textures import *
import Coordinates
from Config import WIN_HEIGHT, WIN_WIDTH


class SquarePiece(Piece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates):
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates)
        self.texture = YELLOW_IMAGE
        # Topleft
        coords_0 = Coordinates.Coordinates(int(WIN_WIDTH / 2) - piece_width, 0)
        self.list_of_subpieces.append(
            SubPiece.SubPiece(piece_width, piece_height, coords_0, self.texture, vertical_rate,
                              horizontal_rate, ground_coordinates))
        coords_1 = Coordinates.Coordinates(int(WIN_WIDTH / 2), 0)
        self.list_of_subpieces.append(
            SubPiece.SubPiece(piece_width, piece_height, coords_1, self.texture, vertical_rate,
                              horizontal_rate, ground_coordinates))
        coords_2 = Coordinates.Coordinates(int(WIN_WIDTH / 2) - piece_width, piece_height)
        self.list_of_subpieces.append(
            SubPiece.SubPiece(piece_width, piece_height, coords_2, self.texture, vertical_rate,
                              horizontal_rate, ground_coordinates))
        coords_3 = Coordinates.Coordinates(int(WIN_WIDTH / 2), piece_height)
        self.list_of_subpieces.append(
            SubPiece.SubPiece(piece_width, piece_height, coords_3, self.texture, vertical_rate,
                              horizontal_rate, ground_coordinates))
