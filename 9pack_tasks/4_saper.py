import random

import numpy
import pygame


class Place:
    def __init__(self, x, y):
        self.area = numpy.zeros([x, y])
        self.b_area = numpy.zeros([x + 2, y + 2])
        self.shape = self.area.shape

    def fill_bombs(self, n):
        for i in range(n):
            x = random.randint(0, self.shape[0] - 1)
            y = random.randint(0, self.shape[1] - 1)
            self.area[x][y] = -1
        self.MaxPooling()
        self.fill_values()
        self.FlatPooling()

        # print(self.area)
        return self.area

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

    def MaxPooling(self):
        self.b_area[1:self.shape[0] + 1, 1:self.shape[1] + 1] = self.area

    def FlatPooling(self):
        self.area = self.b_area[1:self.shape[0] + 1, 1:self.shape[1] + 1]


class Board:
    def __init__(self, width, height, field):
        self.width = width
        self.height = height
        self.cell_size = width // field.shape[0]
        self.field = field

    def render(self, screen):
        for i in range(self.field.shape[0]):
            for k in range(self.field.shape[1]):
                pygame.draw.rect(screen, pygame.color.Color('red' if self.field[i][k] == -1 else 'black'),
                                 (self.cell_size * k, self.cell_size * i, self.cell_size * (k + 1),
                                  self.cell_size * (i + 1)))
                pygame.draw.rect(screen, pygame.color.Color('white'), (self.cell_size * k, self.cell_size * i,
                                                                       self.cell_size * (k + 1),
                                                                       self.cell_size * (i + 1)), 1)

    def onClick(self, screen, pos):
        k = int(pos[0] / self.cell_size)
        i = int(pos[1] / self.cell_size)
        f = pygame.font.Font(None, 25)
        digit = f.render(str(int(self.field[i][k])), 255, (0, 0, 0))
        pygame.draw.rect(screen, pygame.color.Color('pink'),
                         (self.cell_size * k, self.cell_size * i, self.cell_size, self.cell_size))
        screen.blit(digit, (k * self.cell_size, i * self.cell_size))


pl = Place(10, 10)
area = pl.fill_bombs(20)

pygame.init()
size = weight, height = 500, 500
screen = pygame.display.set_mode(size)
board = Board(weight, height, area)
board.render(screen)
pygame.display.flip()
quitFlag = False
while not quitFlag:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.onClick(screen, pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            quitFlag = True
        pygame.display.flip()
pygame.quit()
