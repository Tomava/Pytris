import pygame
from GameAssets.Piece import Piece
from Config import GAME_HEIGHT, GAME_WIDTH
from GameAssets.SubPiece import SubPiece


class GroundedPiece(Piece):

    def __init__(self, piece_width, piece_height, lines_width):
        self.list_of_subpieces = set()
        # Set of coordinates that the ground occupies
        self.ground_coordinates = set()
        self.piece_width = piece_width
        self.piece_height = piece_height
        self.lines_widht = lines_width

    def remove_full_lines(self, full_lines):
        to_be_removed = []
        for subpiece in self.list_of_subpieces:
            if subpiece.get_coordinates().get_y() in full_lines:
                to_be_removed.append(subpiece)
        if len(full_lines) > 0:
            self.ground_coordinates.clear()
            for subpiece in to_be_removed:
                self.list_of_subpieces.remove(subpiece)
        for subpiece in self.list_of_subpieces:
            if len(full_lines) > 0:
                for lane in full_lines:
                    if subpiece.get_coordinates().get_y() < lane:
                        subpiece.can_move_down(True)
                        subpiece.move_down()
            self.ground_coordinates.add(subpiece.get_coordinates())

    def count_full_lines(self) -> int:
        lines = {}
        for subpiece in self.list_of_subpieces:
            y = subpiece.get_coordinates().get_y()
            if y not in lines:
                lines[y] = 0
            lines[y] += 1
        full_lines = []
        for line, amount in lines.items():
            if amount >= self.lines_widht:
                full_lines.append(line)
        full_lines.sort()
        self.remove_full_lines(full_lines)
        return len(full_lines)

    def add_pieces(self, list_of_pieces) -> int:
        self.list_of_subpieces.update(list_of_pieces)
        for sub_piece in list_of_pieces:
            sub_piece.set_ground_time()
        return self.count_full_lines()

    def get_occupied_coordinates(self) -> set:
        return self.ground_coordinates
