from copy import copy
from Piece import Piece
import SubPiece
from Textures import *
import Coordinates


class JPiece(Piece):
    def __init__(self, WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates):
        self.list_of_subpieces = []
        self.rotation = 0
        self.texture = BLUE_IMAGE
        self.piece_width = piece_width
        self.piece_height = piece_height
        self.ground_coordinates = ground_coordinates
        # Topleft
        coords_0 = Coordinates.Coordinates(int(WIN_WIDHT / 2) - 2 * piece_width, 0)
        self.list_of_subpieces.append(SubPiece.SubPiece(WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, coords_0,
                                                        self.texture, vertical_rate, horizontal_rate))
        coords_1 = Coordinates.Coordinates(int(WIN_WIDHT / 2) - 2 * piece_width, piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, coords_1,
                                                        self.texture, vertical_rate, horizontal_rate))
        coords_2 = Coordinates.Coordinates(int(WIN_WIDHT / 2) - piece_width, piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, coords_2,
                                                        self.texture, vertical_rate, horizontal_rate))
        coords_3 = Coordinates.Coordinates(int(WIN_WIDHT / 2), piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, coords_3,
                                                        self.texture, vertical_rate, horizontal_rate))

    def rotate_subpiece(self, piece_index, relative_x, relative_y, only_check: bool):
        if only_check:
            if copy(self.list_of_subpieces[piece_index].get_coordinates()).add_x_and_y(relative_x, relative_y) in self.ground_coordinates:
                return False
        else:
            self.list_of_subpieces[piece_index].get_coordinates().add_x_and_y(relative_x, relative_y)
            return True
        return True

    def can_rotate(self, only_check: bool):
        if self.rotation == 0:
            if not self.rotate_subpiece(0, 2 * self.piece_width, 0, only_check):
                return False
            if not self.rotate_subpiece(1, self.piece_width, -self.piece_height, only_check):
                return False
            if not self.rotate_subpiece(3, -self.piece_width, self.piece_height, only_check):
                return False
        elif self.rotation == 1:
            if not self.rotate_subpiece(0, 0, 2 * self.piece_height, only_check):
                return False
            if not self.rotate_subpiece(1, self.piece_width, self.piece_height, only_check):
                return False
            if not self.rotate_subpiece(3, -self.piece_width, -self.piece_height, only_check):
                return False
        elif self.rotation == 2:
            if not self.rotate_subpiece(0, -2 * self.piece_width, 0, only_check):
                return False
            if not self.rotate_subpiece(1, -self.piece_width, self.piece_height, only_check):
                return False
            if not self.rotate_subpiece(3, self.piece_width, -self.piece_height, only_check):
                return False
        elif self.rotation == 3:
            if not self.rotate_subpiece(0, 0, -2 * self.piece_height, only_check):
                return False
            if not self.rotate_subpiece(1, -self.piece_width, -self.piece_height, only_check):
                return False
            if not self.rotate_subpiece(3, self.piece_width, self.piece_height, only_check):
                return False
        return True

    def rotate(self):
        if self.can_rotate(True):
            self.can_rotate(False)

        self.rotation += 1
        if self.rotation > 3:
            self.rotation = 0
