from classes import *
import pygame
from pygame import image

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("0xFFFFFF")

    for i in board:
        rect = pygame.Rect((ord(i.file)-ord("A"))*80, (i.rank-1)*80, 80, 80)
        if i.colour:
            pygame.draw.rect(screen, "0xD2B48C", rect)
        else:
            pygame.draw.rect(screen, "0x6F4E37", rect)
        
        if i.piece:
            rep = pygame.image.load(i.piece.rep)
            screen.blit(rep, rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

