from math import cos, radians, sin

import pygame

size = weight, height = 1000, 1000

screen = pygame.display.set_mode(size)

quitFlag = False
pause = False

color = pygame.color.Color(255, 0, 0)
hsv = color.hsva

x1 = int(cos(radians(0)) * 350) + 500
y1 = int(sin(radians(0)) * 350) + 500
x2 = int(cos(radians(0)) * 350) + 500
y2 = int(sin(radians(0)) * 350) + 500

firstNumber = 2
secondNumber = 0
a = 1

screens = [None for i in range(360)]

while not quitFlag:
    if not pause:
        secondNumber += 1
        if secondNumber >= 360:
            firstNumber += 1
            secondNumber = 0
        a += 0.1
        color.hsva = (a % 360, hsv[1], hsv[2], hsv[3])
        x1 = int(cos(radians(secondNumber)) * 350) + 500
        y1 = int(sin(radians(secondNumber)) * 350) + 500
        x2 = int(cos(radians(secondNumber * firstNumber)) * 350) + 500
        y2 = int(sin(radians(secondNumber * firstNumber)) * 350) + 500
        screens[secondNumber] = [[x1, y1], [x2, y2]]
        screen.fill((0, 0, 0))
        for i in range(len(screens)):
            if screens[i] != None:
                pygame.draw.line(screen, color, screens[i][0], screens[i][1], 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitFlag = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pause = not pause
    pygame.display.flip()

pygame.quit()
