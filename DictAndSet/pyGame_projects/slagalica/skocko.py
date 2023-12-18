import pygame

pygame.init()
width = 800
height = 650

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Slike i Oblici')

babolat = pygame.image.load("teniser2.png").convert()
babolat = pygame.transform.scale(babolat, (80, 60))

federer = pygame.image.load("teniser1.png").convert()
federer = pygame.transform.scale(federer, (80, 60))

nadal = pygame.image.load("teniser6.png").convert()
nadal = pygame.transform.scale(nadal, (80, 60))

novak = pygame.image.load("teniser4.png").convert()
novak = pygame.transform.scale(novak, (80, 60))

zverev = pygame.image.load("teniser3.png").convert()
zverev = pygame.transform.scale(zverev, (80, 60))

skocko = pygame.image.load("teniser5.png").convert()
skocko = pygame.transform.scale(skocko, (80, 60))

babolat_rect = babolat.get_rect(bottomright=(width - 10, height - 20))
federer_rect = federer.get_rect(bottomright=(width - 110, height - 20))
nadal_rect = nadal.get_rect(bottomright=(width - 210, height - 20))
novak_rect = novak.get_rect(bottomright=(width - 310, height - 20))
zverev_rect = zverev.get_rect(bottomright=(width - 410, height - 20))
skocko_rect = skocko.get_rect(bottomright=(width - 510, height - 20))

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

counter = pygame.Vector2()

selected_image = None

lista = []

while slike:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(slike):

                if rect[1].collidepoint(event.pos) and not occupied_cells[i // NUM_SHAPES_PER_ROW][
                    i % NUM_SHAPES_PER_ROW]:
                    occupied_cells[i // NUM_SHAPES_PER_ROW][i % NUM_SHAPES_PER_ROW] = True
                    selected_image, _ = slike[i]
                    counter.x += 1
                    if counter.x >= 4:
                        counter.y += 1
                        counter.x = 0

                    (mosuse_x, mouse_y) = pygame.mouse.get_pos()
                    if mosuse_x <= width - 110 and mosuse_x >= width - 10 and mouse_y <= height - 80 and mouse_y >= height-20:
                        selected_image = skocko

                    break

    screen.fill((55, 95, 145))

    for kvadrat in kvadrati:
        pygame.draw.rect(screen, (255, 255, 255), kvadrat, 2)

    for krug in krugovi:
        pygame.draw.circle(screen, (255, 255, 255), krug.center, SHAPE_SIZE // 2, 2)

    for slika, rect in slike:
        screen.blit(slika, rect)

    image_counter = 0

    if selected_image is not None:
        kvadrat_x, kvadrat_y = kvadrati[image_counter][0], kvadrati[image_counter][1]
        screen.blit(selected_image, (kvadrat_x, kvadrat_y))
        image_counter += 1

    pygame.display.update()


