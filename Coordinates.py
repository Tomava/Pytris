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

    def add_x(self, amount):
        self.set_x(self.get_x() + amount)

    def add_y(self, amount):
        self.set_y(self.get_y() + amount)

    def get_tuple(self):
        return (self.get_x(), self.get_y())

    def __eq__(self, other) -> bool:
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()
