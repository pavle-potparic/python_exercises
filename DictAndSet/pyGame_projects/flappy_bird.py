import pygame
import random

pygame.init()

SIRINA, VISINA = 400, 600
ekran = pygame.display.set_mode((SIRINA, VISINA))
pygame.display.set_caption("Flappy Bird")

SVETLO_PLAVA = (173, 216, 230)
ZUTA = (255, 255, 0)
ZELENA = (0, 255, 0)
BELA = (255, 255, 255)

font = pygame.font.Font(None, 36)
poeni = 0

ptica_x = 50
ptica_y = VISINA // 2
brzina_ptice = 0
ubrzanje_ptice = 0.7
skok_ptice = -10
radijus_ptice = 20

sirina_cevi = 70
razmak_cevi = 200
cevi_x = SIRINA
brzina_cevi = 5
cevi = []

radi = True
while radi:
    for dogadjaj in pygame.event.get():
        if dogadjaj.type == pygame.QUIT:
            radi = False
        if dogadjaj.type == pygame.KEYDOWN:
            if dogadjaj.key == pygame.K_SPACE:
                brzina_ptice = skok_ptice

    brzina_ptice += ubrzanje_ptice
    ptica_y += brzina_ptice

    if len(cevi) == 0 or cevi[-1][0] < SIRINA - 200:
        visina_cevi = random.randint(50, VISINA - razmak_cevi - 50)
        cevi.append([SIRINA, visina_cevi, False])

    for idx, cev in enumerate(cevi):
        cevi_x, visina_cevi, osvojen_poen = cev
        cevi_x -= brzina_cevi
        cevi[idx] = [cevi_x, visina_cevi, osvojen_poen]

        if (
                ptica_x + radijus_ptice > cevi_x
                and ptica_x - radijus_ptice < cevi_x + sirina_cevi
                and (ptica_y - radijus_ptice < visina_cevi or ptica_y + radijus_ptice > visina_cevi + razmak_cevi)
        ):
            radi = False

        if cevi_x < -sirina_cevi:
            cevi.pop(idx)

        if cevi_x + sirina_cevi < ptica_x - radijus_ptice and not osvojen_poen:
            cevi[idx][2] = True
            poeni += 1

    ekran.fill(SVETLO_PLAVA)
    pygame.draw.circle(ekran, ZUTA, (ptica_x, int(ptica_y)), radijus_ptice)
    for cev in cevi:
        cevi_x, visina_cevi, _ = cev
        pygame.draw.rect(ekran, ZELENA, (cevi_x, 0, sirina_cevi, visina_cevi))
        pygame.draw.rect(ekran, ZELENA, (cevi_x, visina_cevi + razmak_cevi, sirina_cevi, VISINA - visina_cevi - razmak_cevi))

    tekst_poena = font.render(f"Poeni: {poeni}", True, BELA)
    ekran.blit(tekst_poena, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

print("Tvoj rezultat je bio:", poeni)
pygame.quit()
