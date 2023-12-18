import pygame
import random

pygame.init()


BELA = (121, 233, 237)
CRNA = (0, 0, 0)

prozor = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Igra vesalice")

reci = ["tastatura", "monitor", "monitor", "mis", "slusalice", "selotejp", "geografija", "majmun", "slika", 'motokultivator',
        "traktor", "ajkula", "naruto", "limunada", "telefon", "igrica", "pavle", "potparic", "gitara", "solfedjo"]

izabrana_rec = random.choice(reci)

vesalo = 0
broj_pokusaja = 6

pogodjena_slova = []


def crtanje_vesala():
    if vesalo >= 1:
        pygame.draw.circle(prozor, CRNA, (200, 120), 20)

    if vesalo >= 2:
        pygame.draw.line(prozor, CRNA, (200, 140), (200, 200), 5)

    if vesalo >= 3:
        pygame.draw.line(prozor, CRNA, (200, 160), (180, 170), 5)

    if vesalo >= 4:
        pygame.draw.line(prozor, CRNA, (200, 160), (220, 170), 5)

    if vesalo >= 5:
        pygame.draw.line(prozor, CRNA, (200, 200), (180, 220), 5)

    if vesalo >= 6:
        pygame.draw.line(prozor, CRNA, (200, 200), (220, 220), 5)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                slovo = event.unicode.lower()
                if slovo not in pogodjena_slova:
                    pogodjena_slova.append(slovo)
                    if slovo not in izabrana_rec:
                        vesalo += 1

    prozor.fill(BELA)
    crtanje_vesala()

    prikazana_rec = ""
    for slovo in izabrana_rec:
        if slovo in pogodjena_slova:
            prikazana_rec += slovo
        else:
            prikazana_rec += "_ "
    font = pygame.font.Font(None, 36)
    text = font.render(prikazana_rec, True, CRNA)
    text_x = 200 - text.get_width() // 2
    prozor.blit(text, (text_x, 250))

    pygame.display.update()

    if vesalo >= broj_pokusaja:
        font = pygame.font.Font(None, 36)
        kraj_poruka = font.render(izabrana_rec, True, CRNA)
        prozor.blit(kraj_poruka, (50, 300))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    if "_" not in prikazana_rec:
        font = pygame.font.Font(None, 36)
        kraj_poruka = font.render(izabrana_rec, True, CRNA)
        prozor.blit(kraj_poruka, (50, 300))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

pygame.quit()
