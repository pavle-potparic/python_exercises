import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Srećan rođendan!")


font = pygame.font.Font(None, 36)
text = ""
current_letter = 0
message = "Debeli Zole Debeli Zole Debeli Zole Debeli Zole Debeli Zole Debeli Zole Debeli Zole Debeli Zole "


delay = 0.5
start_time = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.time()

    if current_time - start_time > delay and current_letter < len(message):
        text += message[current_letter]
        current_letter += 1
        start_time = current_time

    screen.fill((171, 245, 12))

    text_surface = font.render(text, True, (2, 126, 189))
    text_rect = text_surface.get_rect(center=(400, 300))
    screen.blit(text_surface, text_rect)

    pygame.display.update()

pygame.quit()
