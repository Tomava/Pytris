import pygame
from Config import GAME_HEIGHT, GAME_WIDTH, GAME_OFFSET_X, GAME_OFFSET_Y
from copy import copy


class SubPiece:
    def __init__(self, width, height, coordinates, texture, vertical_rate, horizontal_rate, ground_coordinates):
        self.WIDTH = width
        self.HEIGHT = height
        self.ground_coordinates = ground_coordinates
        # Top left corner of the piece
        coordinates.add_x_and_y(GAME_OFFSET_X, GAME_OFFSET_Y)
        self.coordinates = coordinates
        self.new_coordinates = copy(coordinates)
        self.texture = texture
        self.object = pygame.transform.scale(self.texture, (self.WIDTH, self.HEIGHT))
        self.vertical_rate = vertical_rate
        self.horizontal_rate = horizontal_rate
        self.speed = vertical_rate
        self.last_moved_vertical = pygame.time.get_ticks()
        self.last_moved_horizontal = -horizontal_rate
        self.ground_time = -1
        self.is_grounded = False

    def finalize_new_coordinates(self):
        self.coordinates = copy(self.new_coordinates)

    def is_inside_play_area(self) -> bool:
        if self.new_coordinates.get_x() + self.WIDTH > GAME_WIDTH + GAME_OFFSET_X:
            return False
        if self.new_coordinates.get_x() < 0:
            return False
        if self.new_coordinates.get_y() + self.HEIGHT > GAME_HEIGHT + GAME_OFFSET_Y:
            return False
        if self.new_coordinates.get_y() < 0:
            return False
        return True

    def is_colliding(self) -> bool:
        if self.new_coordinates in self.ground_coordinates:
            return True
        return False

    def is_able_to_move(self, relative_x, relative_y) -> bool:
        self.new_coordinates = copy(self.coordinates)
        self.new_coordinates.add_x_and_y(relative_x, relative_y)
        if self.is_inside_play_area() and not self.is_colliding():
            return True
        return False

    def can_move_down(self, ignore_time=False):
        if ignore_time or pygame.time.get_ticks() - self.last_moved_vertical > self.speed:
            if self.is_able_to_move(0, self.HEIGHT):
                return True
            elif not self.is_grounded:
                self.ground_time = pygame.time.get_ticks()
                self.is_grounded = True
        return False

    def move_down(self):
        self.last_moved_vertical = pygame.time.get_ticks()
        self.finalize_new_coordinates()

    def speed_up(self):
        self.speed = self.vertical_rate / 4

    def speed_down(self):
        self.speed = self.vertical_rate

    def can_move_left(self, ignore_time=False):
        if ignore_time or pygame.time.get_ticks() - self.last_moved_horizontal > self.horizontal_rate:
            if self.is_able_to_move(-self.WIDTH, 0):
                return True
        return False

    def move_left(self):
        self.last_moved_horizontal = pygame.time.get_ticks()
        self.finalize_new_coordinates()

    def can_move_right(self, ignore_time=False):
        if ignore_time or pygame.time.get_ticks() - self.last_moved_horizontal > self.horizontal_rate:
            if self.is_able_to_move(self.WIDTH, 0):
                return True
        return False

    def move_right(self):
        self.last_moved_horizontal = pygame.time.get_ticks()
        self.finalize_new_coordinates()

    def can_move_relative(self, relative_x, relative_y):
        if self.is_able_to_move(relative_x, relative_y):
            return True
        return False

    def move_relative(self):
        self.finalize_new_coordinates()

    def get_object(self):
        return self.object

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_ground_time(self):
        return self.ground_time

    def set_ground_time(self):
        self.ground_time = pygame.time.get_ticks()

    def reset_ground_time(self):
        self.ground_time = -1
        self.is_grounded = False
