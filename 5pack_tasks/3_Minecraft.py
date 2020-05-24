from coordinates import Coordinate


class BaseObject:
    def __init__(self, x, y, z):
        self.coord_3d = Coordinate(x=x, y=y, z=z)

    def get_coordinates(self):
        return self.coord_3d


class Block(BaseObject):
    def shatter(self):
        self.coord_3d = None


class Entity(BaseObject):
    def move(self, x, y, z):
        self.coord_3d = Coordinate(x=x, y=y, z=z)


class Thing(BaseObject):
    pass


minecraft = BaseObject(4, 5, 0)
