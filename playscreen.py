import pygame
import random

rows = 20
cols = 20
celldim = 20

pygame.init()


boardsize = (rows*celldim, cols*celldim)
win = pygame.display.set_mode(boardsize)
pygame.display.set_caption("MINESWEAPER AI")
win.fill((0,128,128))
pygame.display.update()


run = True
while run:
    event = pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
