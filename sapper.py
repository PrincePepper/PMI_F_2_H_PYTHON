import random
from datetime import datetime

import numpy as np


def time_check(func):
    def wrapper(self):
        start = datetime.now()
        func(self)
        print(datetime.now() - start)

    return wrapper


class Place:
    def __init__(self, shapes):
        self.area = np.zeros(shapes)
        self.b_area = np.zeros([shapes[0] + 2, shapes[1] + 2])
        self.shape = self.area.shape

    def fill_bombs(self, n):
        for i in range(n):
            x = random.randint(0, self.shape[0] - 1)
            y = random.randint(0, self.shape[1] - 1)
            self.area[x][y] = -1
        self.MaxPooling()
        self.fill_values()
        self.FlatPooling()

        print(self.area)
        print(self.get_environment([0, 0], [3, 3]))

    @time_check
    def fill_values(self):
        for i, row in enumerate(self.b_area):
            for j, value in enumerate(row):
                if value == -1:
                    self.b_area[i - 1][j - 1] += 1 if not self.b_area[i - 1][j - 1] == -1 else 0
                    self.b_area[i - 1][j] += 1 if not self.b_area[i - 1][j] == -1 else 0
                    self.b_area[i - 1][j + 1] += 1 if not self.b_area[i - 1][j + 1] == -1 else 0
                    self.b_area[i][j - 1] += 1 if not self.b_area[i][j - 1] == -1 else 0
                    self.b_area[i][j + 1] += 1 if not self.b_area[i][j + 1] == -1 else 0
                    self.b_area[i + 1][j - 1] += 1 if not self.b_area[i + 1][j - 1] == -1 else 0
                    self.b_area[i + 1][j] += 1 if not self.b_area[i + 1][j] == -1 else 0
                    self.b_area[i + 1][j + 1] += 1 if not self.b_area[i + 1][j + 1] == -1 else 0

    def get_environment(self, xy, shape=None):
        x, y = xy
        if shape is None:
            shape = [3, 3]

        shape[0] = (shape[0] - 1) // 2
        shape[1] = (shape[1] - 1) // 2
        return self.b_area[x - shape[0] + 1:x + shape[0] + 2, y - shape[1] + 1:y + shape[1] + 2]

    @time_check
    def MaxPooling(self):
        self.b_area[1:self.shape[0] + 1, 1:self.shape[1] + 1] = self.area

    @time_check
    def FlatPooling(self):
        self.area = self.b_area[1:self.shape[0] + 1, 1:self.shape[1] + 1]


pl = Place([1000, 1000])
pl.fill_bombs(1000000)
