class Piece:
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates, ghost=False):
        self.list_of_subpieces = []
        # Set of coordinates that the ground occupies
        self.ground_coordinates = ground_coordinates
        self.rotation = 0
        self.piece_width = piece_width
        self.piece_height = piece_height
        self.vertical_rate = vertical_rate
        self.horizontal_rate = horizontal_rate
        self.ground_time = -1
        self.sped_up = False
        self.create_piece()
        self.ghost = None

    def create_piece(self):
        pass

    def update_ghost(self):
        if self.ghost is not None:
            self.ghost.teleport(self)
            self.ghost.set_ground_time(-1)
            for subpiece in self.ghost.get_subpieces():
                subpiece.reset_ground_time()
            self.ghost.drop_down()

    def get_ghost(self):
        if self.ghost is not None:
            return self.ghost

    def teleport(self, other):
        for subpiece, other_subpiece in zip(self.list_of_subpieces, other.get_subpieces()):
            subpiece.set_coordinates(other_subpiece.get_coordinates())

    def rotate_subpieces(self, movements, moved=False):
        """
        Tries to rotate subpieces
        :param movements: list, Contains tuples for relative_x and relative_y for each index of pieces
        :param moved: bool, If False will try to move the piece and then rotate
        :return: nothing
        """""
        can_rotate = True
        for sub_piece, (relative_x, relative_y) in zip(self.list_of_subpieces, movements):
            if not sub_piece.can_move_relative(relative_x, relative_y):
                can_rotate = False
        if can_rotate:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_relative()
            self.update_ghost()
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
            self.update_ghost()

    def move_left(self, ignore_time=False):
        can_move = True
        for sub_piece in self.list_of_subpieces:
            if not sub_piece.can_move_left(ignore_time):
                can_move = False
                break
        if can_move:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_left()
            self.update_ghost()

    def move_right(self, ignore_time=False):
        can_move = True
        for sub_piece in self.list_of_subpieces:
            if not sub_piece.can_move_right(ignore_time):
                can_move = False
                break
        if can_move:
            for sub_piece in self.list_of_subpieces:
                sub_piece.move_right()
            self.update_ghost()

    def get_subpieces(self):
        return self.list_of_subpieces

    def get_ground_time(self):
        return self.ground_time

    def set_ground_time(self, time):
        self.ground_time = time


class PieceGhost(Piece):
    def __init__(self, piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates):
        super().__init__(piece_width, piece_height, vertical_rate, horizontal_rate, ground_coordinates, True)
