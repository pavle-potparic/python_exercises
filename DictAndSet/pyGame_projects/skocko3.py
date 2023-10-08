import copy
import random

import pygame

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
color = "withe"
for x in range(0, 4):
    broj = random.randint(0, 5)
    kombinacija.append(broj)

print(kombinacija)

SHAPE_SIZE = 60
SHAPE_MARGIN = 10
NUM_SHAPES_PER_ROW = 4
NUM_ROWS = 7

kvadrati = []
krugovi = []

for row in range(NUM_ROWS):
    for col in range(NUM_SHAPES_PER_ROW):
        shape_x = col * (SHAPE_SIZE + SHAPE_MARGIN)
        shape_y = row * (SHAPE_SIZE + SHAPE_MARGIN)
        kvadrat = pygame.Rect(shape_x, shape_y, SHAPE_SIZE, SHAPE_SIZE)
        kvadrati.append(kvadrat)

        circle_x = width - (col + 1) * (SHAPE_SIZE + SHAPE_MARGIN)
        circle_y = row * (SHAPE_SIZE + SHAPE_MARGIN)
        krug = pygame.Rect(circle_x - SHAPE_SIZE // 2, circle_y + SHAPE_SIZE // 4, SHAPE_SIZE, SHAPE_SIZE)
        krugovi.append(krug)

slike = [(babolat, babolat_rect), (federer, federer_rect), (nadal, nadal_rect), (novak, novak_rect),
         (zverev, zverev_rect), (skocko, skocko_rect)]
occupied_cells = [[False for _ in range(NUM_SHAPES_PER_ROW)] for _ in range(NUM_ROWS)]

pygame.init()

screen = pygame.display.set_mode((width, height))

game = [[0 for i in range(4)] for a in range(7)]

counter = pygame.Vector2()

selected_image = None
selected_index = None

running = True

slike = slike * 7

lista_index = []

crvena = 0
zuta = 0

nula = 0

end = 0

loop_counter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(slike):
                if rect[1].collidepoint(event.pos) and not occupied_cells[(i // 7) // NUM_SHAPES_PER_ROW][
                    (i // 7) % NUM_SHAPES_PER_ROW]:
                    occupied_cells[i // NUM_SHAPES_PER_ROW][i % NUM_SHAPES_PER_ROW] = True
                    selected_image, _ = slike[i]
                    selected_index = i
                    if selected_index == 0:
                        nula += 1
                    print(i)

                    index = selected_index - (nula * 6)

                    if index == 6:
                        index -= index

                    if index == -6:
                        index = 0

                    lista_index.append(index)

                    game[int(counter.y)][int(counter.x)] = selected_image
                    counter.x += 1
                    if counter.x >= 4:
                        counter.y += 1
                        counter.x = 0
                    break

    screen.fill((55, 95, 145))

    for kvadrat in kvadrati:
        pygame.draw.rect(screen, (255, 255, 255), kvadrat, 2)

    for krug in krugovi:
        pygame.draw.circle(screen, (255, 255, 255), krug.center, SHAPE_SIZE // 2, 2)

    for slika, rect in slike:
        screen.blit(slika, rect)

    if selected_image is not None:
        kvadrat_x, kvadrat_y = kvadrati[0].topleft
        screen.blit(selected_image, (kvadrat_x, kvadrat_y))
        end += 1

    for y, row in enumerate(game):
        for x, tile in enumerate(row):
            if tile != 0:
                shape_x = x * (SHAPE_SIZE + SHAPE_MARGIN)
                shape_y = y * (SHAPE_SIZE + SHAPE_MARGIN)
                kvadrat = pygame.Rect(shape_x, shape_y, SHAPE_SIZE, SHAPE_SIZE)
                screen.blit(tile, kvadrat)

    kombinacija2 = copy.deepcopy(kombinacija)

    if len(lista_index) == 4:
        loop_counter += 1
        for o in range(0, 4):

            if lista_index[0] in kombinacija2:

                if lista_index[0] == kombinacija2[0]:
                    crvena += 1
                    kombinacija2.remove(kombinacija2[0])
                    lista_index.remove(lista_index[0])

                else:
                    zuta += 1

                    kombinacija2.remove(kombinacija2[0])
                    lista_index.remove(lista_index[0])
            else:
                kombinacija2.remove(kombinacija2[0])
                lista_index.remove(lista_index[0])

        lista_index = []

        print(crvena, zuta)

        if crvena == 4:
            running = False

        if loop_counter == 7:
            running = False

        crvena = 0
        zuta = 0

    pygame.display.update()

print(loop_counter)


