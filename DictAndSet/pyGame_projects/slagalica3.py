import pygame
import random

pygame.init()

width = 800
height = 650

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Skocko')


babolat = pygame.image.load("babolat_logo_slagalica.jpg").convert()
babolat = pygame.transform.scale(babolat, (80, 60))

federer = pygame.image.load("federer_logo_slagalica.jpg").convert()
federer = pygame.transform.scale(federer, (80, 60))

nadal = pygame.image.load("nadal_logo_slagalica.png").convert()
nadal = pygame.transform.scale(nadal, (80, 60))

novak = pygame.image.load("novak_logo_slagalica.png").convert()
novak = pygame.transform.scale(novak, (80, 60))

zverev = pygame.image.load("zverev_logo_slagalica.png").convert()
zverev = pygame.transform.scale(zverev, (80, 60))

skocko = pygame.image.load("skocko.jpg").convert()
skocko = pygame.transform.scale(skocko, (80, 60))

babolat_rect = babolat.get_rect(bottomright=(width - 10, height - 20))
federer_rect = federer.get_rect(bottomright=(width - 110, height - 20))
nadal_rect = nadal.get_rect(bottomright=(width - 210, height - 20))
novak_rect = novak.get_rect(bottomright=(width - 310, height - 20))
zverev_rect = zverev.get_rect(bottomright=(width - 410, height - 20))
skocko_rect = skocko.get_rect(bottomright=(width - 510, height - 20))

kombinacija = []

for x in range(0, 4):
    broj = random.randint(0, 5)
    kombinacija.append(broj)

print(kombinacija)

for row in range(7):
    for col in range(4):
        shape_x = col * (60 + 10)
        shape_y = row * (60 + 10)
        kvadrat = pygame.Rect(shape_x, shape_y, 60, 10)

        circle_x = width - (col + 1) * (60 + 10)
        circle_y = row * (60 + 10)
        krug = pygame.Rect(circle_x - 60 // 2, circle_y + 60 // 4, 60, 60)


while slike:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
