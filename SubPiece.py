import pygame


class SubPiece:
    def __init__(self, WIN_WIDHT, WIN_HEIGHT, width, height, coordinates, texture, vertical_rate, horizontal_rate):
        self.WIN_WIDTH = WIN_WIDHT
        self.WIN_HEIGHT = WIN_HEIGHT
        self.WIDTH = width
        self.HEIGHT = height
        # Top left corner of the piece
        self.coordinates = coordinates
        self.texture = texture
        self.object = pygame.transform.scale(self.texture, (self.WIDTH, self.HEIGHT))
        self.vertical_rate = vertical_rate
        self.horizontal_rate = horizontal_rate
        self.last_moved_vertical = pygame.time.get_ticks()
        self.last_moved_horizontal = -horizontal_rate

    def check_inside_play_area(self) -> bool:
        if self.coordinates.get_x() + self.WIDTH >= self.WIN_WIDTH:
            return False
        if self.coordinates.get_x() < 0:
            return False
        if self.coordinates.get_y() + self.HEIGHT >= self.WIN_HEIGHT:
            return False
        if self.coordinates.get_y() < 0:
            return False
        return True

    def move_down(self):
        if pygame.time.get_ticks() - self.last_moved_vertical > self.vertical_rate:
            if self.check_inside_play_area():
                self.last_moved_vertical = pygame.time.get_ticks()
                self.coordinates.add_y(self.HEIGHT)

    def move_left(self):
        if pygame.time.get_ticks() - self.last_moved_horizontal > self.horizontal_rate:
            if self.check_inside_play_area():
                self.last_moved_horizontal = pygame.time.get_ticks()
                self.coordinates.add_x(-self.HEIGHT)

    def move_right(self):
        if pygame.time.get_ticks() - self.last_moved_horizontal > self.horizontal_rate:
            if self.check_inside_play_area():
                self.last_moved_horizontal = pygame.time.get_ticks()
                self.coordinates.add_x(self.HEIGHT)

    def get_object(self):
        return self.object

    def get_coordinates(self):
        return self.coordinates.get_tuple()
