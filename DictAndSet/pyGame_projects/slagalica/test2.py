import pygame
import sys
pygame.init()
fps=30
fpsclock=pygame.time.Clock()
sur_obj=pygame.display.set_mode((400,300))
pygame.display.set_caption("Keyboard_Input")
White=(255,255,255)
p1=10
p2=10
step=5
while True:
    sur_obj.fill(White)
    pygame.draw.rect(sur_obj, (255,0,0), (p1, p2, 55, 45))
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        p1 -= step
    if key_input[pygame.K_UP]:
        p2 -= step
    if key_input[pygame.K_RIGHT]:
        p1 += step
    if key_input[pygame.K_DOWN]:
        p2 += step
    pygame.display.update()
    fpsclock.tick(fps)