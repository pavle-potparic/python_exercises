import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
DARK_RED = (139, 0, 0)
DARK_GREEN = (34, 139, 34)
LIGHT_BROWN = (210, 180, 140)
WINDOW_BLUE = (173, 216, 230)

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Animirana Kuća u Pygame-u")

house_x = 50
house_y = 300
house_speed_x = 3
house_speed_y = 2
def draw_house(x, y):

    pygame.draw.rect(screen, LIGHT_BROWN, (x, y, 200, 150))

    pygame.draw.polygon(screen, DARK_RED, [(x, y), (x + 100, y - 100), (x + 200, y)])

    pygame.draw.rect(screen, DARK_GREEN, (x + 75, y + 70, 50, 80))

    pygame.draw.rect(screen, WINDOW_BLUE, (x + 20, y + 30, 50, 50))

    pygame.draw.rect(screen, WINDOW_BLUE, (x + 130, y + 30, 50, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    house_x += house_speed_x
    house_y += house_speed_y

    if house_x <= 0 or house_x + 200 >= window_size[0]:
        house_speed_x = -house_speed_x
    if house_y <= 0 or house_y + 150 >= window_size[1]:
        house_speed_y = -house_speed_y

    screen.fill(SKY_BLUE)

    draw_house(house_x, house_y)

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
