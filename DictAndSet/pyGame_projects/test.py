import pygame
import sys
WEIGHT = 640
HEIGHT = 480

pygame.init()

rect_w = 30
rect_h = 20

screen = pygame.display.set_mode((WEIGHT, HEIGHT))


pygame.draw.rect(screen, 'Red', (WEIGHT/2 - rect_h/2, HEIGHT/2 - rect_h/2, rect_w, rect_h))

pygame.display.update()

# pygame.draw.circle(screen, "Blue", [WEIGHT/2, HEIGHT/2], 170, 3)

pygame.display.update()

running = True

move = 3

def definicja(move, width):
    screen.fill("black")
    width += move
    pygame.draw.rect(screen, 'Red', (WEIGHT/2 - rect_h/2, HEIGHT/2 - rect_h/2 + move, rect_w, rect_h))
    pygame.display.update()




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    definicja(move, rect_w)

