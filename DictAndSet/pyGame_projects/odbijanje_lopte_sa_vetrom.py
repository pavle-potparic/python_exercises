import pygame

pygame.init()

speed = 1

clock = pygame.time.Clock()

height = 550
width = 1000

Vy = -5
a = 0.1


red = (255, 0, 0)
black = (0, 0, 0)

screen_res = (width, height)

pygame.display.set_caption("GFG Bouncing game")
screen = pygame.display.set_mode(screen_res)

ball = pygame.draw.circle(
    surface=screen, color=red, center=[500, 325], radius=15)

centar_x = 500
centar_y = 325
r = 15

Vx = 5

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

    screen.fill(black)

    pygame.draw.circle(
        surface=screen, color=red, center=[centar_x, centar_y], radius=r)

    Vy += a
    centar_y += Vy

    Vx += a
    centar_x += Vx

    if centar_x > width - r:
        Vx *= -0.97

    if centar_y > height - r:
        Vy *= -0.97

    clock.tick(60)
    pygame.display.update()
