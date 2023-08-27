import pygame

pygame.init()
width = 800
hight = 600

screen = pygame.display.set_mode((width, hight))

screen.fill((55, 95, 145))

pygame.display.set_caption('skocko')

babolat = pygame.image.load("C:\\python_exercises\\DictAndSet\\pyGame_projects\\babolat_logo_slagalica.jpg").convert()

babolat = pygame.transform.scale(babolat, (80, 60))

screen.blit(babolat, (700, 535))

federer = pygame.image.load("C:\\python_exercises\\DictAndSet\\pyGame_projects\\federer_logo_slagalica.jpg").convert()

federer = pygame.transform.scale(federer, (80, 60))

screen.blit(federer, (610, 535))

nadal = pygame.image.load("C:\\python_exercises\\DictAndSet\\pyGame_projects\\nadal_logo_slagalica.png").convert()

nadal = pygame.transform.scale(nadal, (80, 60))

screen.blit(nadal, (520, 535))

novak = pygame.image.load("C:\\python_exercises\\DictAndSet\\pyGame_projects\\novak_logo_slagalica.png").convert()

novak = pygame.transform.scale(novak, (80, 60))

screen.blit(novak, (430, 535))


zverev = pygame.image.load("C:\\python_exercises\\DictAndSet\\pyGame_projects\\zverev_logo_slagalica.png").convert()

zverev = pygame.transform.scale(zverev, (80, 60))

screen.blit(zverev, (340, 535))

skocko = pygame.image.load("C:\\python_exercises\\DictAndSet\\pyGame_projects\\skocko.jpg").convert()

skocko = pygame.transform.scale(skocko, (80, 60))

screen.blit(skocko, (250, 535))

pygame.display.update()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

pygame.quit()
