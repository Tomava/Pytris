from Piece import Piece
import SubPiece
from Textures import *
import Coordinates


class SquarePiece(Piece):
    def __init__(self, WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates):
        self.list_of_subpieces = []
        self.texture = YELLOW_IMAGE
        self.ground_coordinates = ground_coordinates
        self.rotation = 0
        self.piece_width = piece_width
        self.piece_height = piece_height
        # Topleft
        coords_0 = Coordinates.Coordinates(int(WIN_WIDHT / 2) - piece_width, 0)
        self.list_of_subpieces.append(
            SubPiece.SubPiece(WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, coords_0, self.texture, vertical_rate,
                              horizontal_rate))
        coords_1 = Coordinates.Coordinates(int(WIN_WIDHT / 2), 0)
        self.list_of_subpieces.append(
            SubPiece.SubPiece(WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, coords_1, self.texture, vertical_rate,
                              horizontal_rate))
        coords_2 = Coordinates.Coordinates(int(WIN_WIDHT / 2) - piece_width, piece_height)
        self.list_of_subpieces.append(
            SubPiece.SubPiece(WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, coords_2, self.texture, vertical_rate,
                              horizontal_rate))
        coords_3 = Coordinates.Coordinates(int(WIN_WIDHT / 2), piece_height)
        self.list_of_subpieces.append(
            SubPiece.SubPiece(WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, coords_3, self.texture, vertical_rate,
                              horizontal_rate))

    def rotate(self):
        pass
