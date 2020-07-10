import pygame

size = weight, height = 500, 500
screens = []
running = False
check = False
flag = 0
pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
screen2 = pygame.Surface(screen.get_size())
screens.append(screen.copy())

startX, startY = 0, 0
sideX, sideY = 0, 0

keys = []

while not running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            check = True
            startX, startY = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            screen2.blit(screen, (0, 0))
            check = False
            sideX, sideY = 0, 0
            screens.append(screen.copy())
            flag = 1
        if event.type == pygame.MOUSEMOTION and check:
            sideX, sideY = event.pos[0] - startX, event.pos[1] - startY
            screen.fill(pygame.Color('black'))
        if keys[pygame.K_LCTRL] and keys[pygame.K_z] and flag:
            if len(screens) > 0:
                screen2 = screens[len(screens) - 1]
                del screens[-1]
            else:
                screen.fill((0, 0, 0))
                screen2 = pygame.Surface(screen.get_size())
            print(flag)
    screen.blit(screen2, (0, 0))
    if check:
        pygame.draw.rect(screen, (255, 255, 255), ((startX, startY), (sideX, sideY)), 5)
    pygame.display.flip()
