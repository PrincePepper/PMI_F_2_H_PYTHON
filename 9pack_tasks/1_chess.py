import pygame


def draw(colors):
    for i in range(count):
        for j in range(count):
            pygame.draw.rect(screen, colors[(i + j) % 2], (cell_size * i, cell_size * j, cell_size, cell_size))


width, count = [int(i) for i in input().split()]
cell_size = width // count
size = (width, width)
color = pygame.color.Color('Black'), pygame.color.Color('White')

screen = pygame.display.set_mode(size)
pygame.init()
draw(color)
pygame.display.flip()

# ожидание закрытия окна
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
