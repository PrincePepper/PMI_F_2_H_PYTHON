import math


class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return MyVector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return MyVector(self.x * other, self.y * other)

    def __imul__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __rmul__(self, other):
        return MyVector(self.x * other, self.y * other)

    def __eq__(self, other):
        if self.x == other.x1 and self.y == other.x2:
            return True
        return False

    def __ne__(self, other):
        if self.x != other.x1 and self.y != other.x2:
            return True
        return False

    def __len__(self):
        return math.floor(math.sqrt(self.x ** 2 + self.y ** 2))

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


v1 = MyVector(-2, 5)
v2 = MyVector(3, -4)

v_sum = v1 - v2
print(v_sum)
