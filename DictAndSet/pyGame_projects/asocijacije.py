import pygame

pygame.init()

width = 650
height = 600

screen = pygame.display.set_mode((width, height))

screen.fill((9, 72, 189))

pygame.display.update()

a1 = pygame.draw.rect(screen, (140, 89, 235), (20, 20, 150, 45))
a2 = pygame.draw.rect(screen, (140, 89, 235), (40, 70, 150, 45))
a3 = pygame.draw.rect(screen, (140, 89, 235), (60, 120, 150, 45))
a4 = pygame.draw.rect(screen, (140, 89, 235), (80, 170, 150, 45))
a = pygame.draw.rect(screen, (89, 220, 235), (100, 220, 150, 45))

b1 = pygame.draw.rect(screen, (140, 89, 235), (485, 20, 150, 45))
b2 = pygame.draw.rect(screen, (140, 89, 235), (465, 70, 150, 45))
b3 = pygame.draw.rect(screen, (140, 89, 235), (445, 120, 150, 45))
b4 = pygame.draw.rect(screen, (140, 89, 235), (425, 170, 150, 45))
b = pygame.draw.rect(screen, (89, 220, 235), (405, 220, 150, 45))

c1 = pygame.draw.rect(screen, (140, 89, 235), (20, 535, 150, 45))
c2 = pygame.draw.rect(screen, (140, 89, 235), (40, 485, 150, 45))
c3 = pygame.draw.rect(screen, (140, 89, 235), (60, 435, 150, 45))
c4 = pygame.draw.rect(screen, (140, 89, 235), (80, 385, 150, 45))
c = pygame.draw.rect(screen, (89, 220, 235), (100, 335, 150, 45))

d1 = pygame.draw.rect(screen, (140, 89, 235), (485, 535, 150, 45))
d2 = pygame.draw.rect(screen, (140, 89, 235), (465, 485, 150, 45))
d3 = pygame.draw.rect(screen, (140, 89, 235), (445, 435, 150, 45))
d4 = pygame.draw.rect(screen, (140, 89, 235), (425, 385, 150, 45))
d = pygame.draw.rect(screen, (89, 220, 235), (405, 335, 150, 45))

end = pygame.draw.rect(screen, (89, 220, 235), (screen.get_width() / 2 - 80, screen.get_height() / 2 - 20, 160, 40))


pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
