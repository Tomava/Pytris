import pygame
import SubPiece
from Config import GAME_HEIGHT, GAME_WIDTH
import Coordinates
from copy import copy


class Piece:
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates):
        self.list_of_subpieces = []
        # Set of coordinates that the ground occupies
        self.ground_coordinates = ground_coordinates
        self.rotation = 0
        self.piece_width = piece_width
        self.piece_height = piece_height
        self.ground_time = -1
        self.sped_up = False

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
            # Try to move pieces left and see if they still collide
            self.move_left()
            if self.rotate_subpieces(movements, True):
                return True
            # Try to move right and rotate
            self.move_right()
            if self.rotate_subpieces(movements, True):
                return True
        return False

    def can_rotate(self):
        return True

    def rotate(self):
        pass

    def drop_down(self):
        while self.ground_time == -1:
            self.move_down(True)

    def speed_up(self):
        self.sped_up = True
        for sub_piece in self.list_of_subpieces:
            sub_piece.speed_up()

    def speed_down(self):
        if self.sped_up:
            self.sped_up = False
            for sub_piece in self.list_of_subpieces:
                sub_piece.speed_down()

    def move_down(self, ignore_time=False):
        can_move = True
        for sub_piece in self.list_of_subpieces:
            if not sub_piece.can_move_down(ignore_time):
                can_move = False
            if sub_piece.get_ground_time() != -1:
                self.ground_time = sub_piece.get_ground_time()
        if can_move:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_down()

    def move_left(self, ignore_time=False):
        can_move = True
        for sub_piece in self.list_of_subpieces:
            if not sub_piece.can_move_left(ignore_time):
                can_move = False
                break
        if can_move:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_left()

    def move_right(self, ignore_time=False):
        can_move = True
        for sub_piece in self.list_of_subpieces:
            if not sub_piece.can_move_right(ignore_time):
                can_move = False
                break
        if can_move:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_right()

    def get_subpieces(self):
        return self.list_of_subpieces

    def get_ground_time(self):
        return self.ground_time
