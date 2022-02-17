from Piece import Piece
import SubPiece
import Coordinates
import SubPiece
from Config import GAME_WIDTH
from Piece import Piece
from Textures import *


class IPiece(Piece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates, ghost=False):
        self.texture = LIGHTBLUE_IMAGE
        if ghost:
            self.texture = LIGHTBLUE_GHOST_IMAGE
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates)
        if not ghost:
            self.ghost = IPieceGhost(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates)
        self.update_ghost()

    def create_piece(self):
        coords_0 = Coordinates.Coordinates(int(GAME_WIDTH / 2) - 2 * self.piece_width, self.piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(self.piece_width, self.piece_height, coords_0,
                                                        self.texture, self.vertical_rate, self.horizontal_rate,
                                                        self.ground_coordinates))
        coords_1 = Coordinates.Coordinates(int(GAME_WIDTH / 2) - self.piece_width, self.piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(self.piece_width, self.piece_height, coords_1,
                                                        self.texture, self.vertical_rate, self.horizontal_rate,
                                                        self.ground_coordinates))
        coords_2 = Coordinates.Coordinates(int(GAME_WIDTH / 2) , self.piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(self.piece_width, self.piece_height, coords_2,
                                                        self.texture, self.vertical_rate, self.horizontal_rate,
                                                        self.ground_coordinates))
        coords_3 = Coordinates.Coordinates(int(GAME_WIDTH / 2) + self.piece_width, self.piece_height)
        self.list_of_subpieces.append(SubPiece.SubPiece(self.piece_width, self.piece_height, coords_3,
                                                        self.texture, self.vertical_rate, self.horizontal_rate,
                                                        self.ground_coordinates))

    def rotate_subpieces(self, movements, moved=False):
        """
        Tries to rotate subpieces
        :param moved: bool, If True will try to move the piece and then rotate
        :param movements: list, Contains tuples for relative_x and relative_y for each index of pieces
        :return: nothing
        """""
        can_rotate = True
        for sub_piece, (relative_x, relative_y) in zip(self.list_of_subpieces, movements):
            if not sub_piece.can_move_relative(relative_x, relative_y):
                can_rotate = False
        if can_rotate:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_relative()
            return True
        elif not moved:
            # Try to move pieces left  twice and see if they still collide
            self.move_left(True)
            if self.rotate_subpieces(movements, True):
                return True
            self.move_left(True)
            if self.rotate_subpieces(movements, True):
                return True
            # Try to move right twice and rotate
            self.move_right(True)
            if self.rotate_subpieces(movements, True):
                return True
            self.move_right(True)
            if self.rotate_subpieces(movements, True):
                return True
        return False

    def rotate(self):
        movements = []
        if self.rotation == 0:
            movements.extend([(2 * self.piece_width, -self.piece_height), (self.piece_width, 0), (0, self.piece_height),
                             (-self.piece_width, 2 * self.piece_height)])
        elif self.rotation == 1:
            movements.extend([(self.piece_width, 2 * self.piece_height), (0, self.piece_height),
                             (-self.piece_width, 0), (-2 * self.piece_width, -self.piece_height)])
        elif self.rotation == 2:
            movements.extend([(-2 * self.piece_width, self.piece_height), (-self.piece_width, 0),
                             (0, -self.piece_height), (self.piece_width, -2 * self.piece_height)])
        elif self.rotation == 3:
            movements.extend([(-self.piece_width, -2 * self.piece_height), (0, -self.piece_height),
                             (self.piece_width, 0), (2 * self.piece_width, self.piece_height)])
        if self.rotate_subpieces(movements):
            self.rotation += 1
            if self.rotation > 3:
                self.rotation = 0

class IPieceGhost(IPiece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates):
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates, True)