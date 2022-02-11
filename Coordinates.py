class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def __eq__(self, other) -> bool:
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()
