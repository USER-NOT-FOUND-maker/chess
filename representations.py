from classes import *
import pygame
from pygame import image

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("chess")

Tfont = pygame.font.Font(None, 54)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("0x000000")

    for i in range(8):
        draw_text(str(i + 1), Tfont, (255, 255, 255), 15, 80 + (i * 80))

    for i in range(8):
        draw_text(files[i], Tfont, (255,255,255), 90 + (i*80), 15)

    for i in board:
        rect = pygame.Rect((ord(i.file)-ord("A"))*80 + 60, 620-((i.rank-1)*80), 80, 80)

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

