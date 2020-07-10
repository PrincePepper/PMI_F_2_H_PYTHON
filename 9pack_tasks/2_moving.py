import random

import pygame

scale_screen, position_react = (500, 500), [0, 0, 125, 125]
color_screen = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color_react = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
pygame.init()
screen = pygame.display.set_mode(scale_screen, pygame.RESIZABLE)
screen.fill(color_screen)
pygame.draw.rect(screen, color_react, position_react)
pygame.display.flip()

last_pos = [0, 0]
running = True
check = False
while running:
    for event in pygame.event.get():
        scale_react = pygame.display.get_surface().get_size()
        scale_react = [i / 4 for i in scale_react]
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            check = position_react[0] <= x <= position_react[0] + scale_react[0] and position_react[1] <= y <= \
                    position_react[1] + scale_react[1]
            last_pos = [x, y]

        if check and event.type == pygame.MOUSEMOTION and event.buttons == (1, 0, 0):
            x, y = pygame.mouse.get_pos()

            position_react[0] = position_react[0] + (x - last_pos[0])

            position_react[1] = position_react[1] + (y - last_pos[1])

            screen.fill(color_screen)
            print(check, position_react, pygame.mouse.get_pos(), scale_react)
            pygame.draw.rect(screen, color_react, position_react)
            last_pos = [x, y]
    pygame.display.flip()

pygame.quit()
