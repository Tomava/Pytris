import pygame
import SubPiece


class Piece:
    def __init__(self, WIN_WIDHT, WIN_HEIGHT, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates):
        self.list_of_subpieces[SubPiece.SubPiece] = []
        # Set of coordinates that the ground occupies
        self.ground_coordinates[Coordinates.Coordinates] = ground_coordinates
        self.rotation = 0
        self.piece_width = piece_width
        self.piece_height = piece_height

    def can_rotate(self):
        return True

    def rotate(self):
        pass

    def move_down(self):
        can_move = True
        for sub_piece in self.list_of_subpieces:
            if not sub_piece.can_move_down():
                can_move = False
                break
        if can_move:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_down()

    def move_left(self):
        can_move = True
        for sub_piece in self.list_of_subpieces:
            if not sub_piece.can_move_left():
                can_move = False
                break
        if can_move:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_left()

    def move_right(self):
        can_move = True
        for sub_piece in self.list_of_subpieces:
            if not sub_piece.can_move_right():
                can_move = False
                break
        if can_move:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_right()

    def get_subpieces(self):
        return self.list_of_subpieces
