import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Park Reči")

white = (255, 255, 255)
blue = (0, 0, 255)

reci = ["Kompjuter", "Drvo", "Sunce", "Oblak", "Reket", "Pas", "Reka", "Planina", "Pismo", "Most"]

font = pygame.font.Font(None, 36)

current_letter = ""
search_bar = ""
search_text = font.render("Reč: ", True, blue)
show_last_line = True

slova = [["K", "O", "J", "M", "P", "E", "U", "U", "X", "R", "A"],
         ["R", "O", "D", "V", "O", "J", "S", "L", "B", "R", "O"], ["E", "S", "T", "S", "U", "N", "L", "C", "A", "Z"],
         ["B", "O", "C", "K", "L", "A", "M", "J", "Q", "B"], ["R", "A", "K", "E", "Y", "N", "A", "M", "T", "U"],
         ["A", "S", "P", "D", "J", "K", "W", "H", "L"],
         ["K", "V", "U", "G", "R", "A", "R", "T", "F", "W"], ["I", "L", "A", "A", "P", "Z", "N", "N", "I", "L"],
         ["A", "S", "S", "I", "M", "P", "N", "M", "K"], ["T", "M", "S", "O", "T", "R", "K", "C", "B"]]


def reset_search_bar():
    global search_bar
    search_bar = ""


def generisi_kvadrate(rec):
    kvadrati = []
    x = 50
    y = 50
    for slovo in rec:
        kvadrat = pygame.draw.rect(screen, blue, (x, y, 60, 60))
        letter = font.render(slovo, True, white)
        letter_rect = letter.get_rect(center=kvadrat.center)
        kvadrati.append((kvadrat, letter, letter_rect))
        x += 70
    return kvadrati


counter = 0
running = True
kvadrati = generisi_kvadrate(slova[counter])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                print("Uneli ste reč:", search_bar)

                if search_bar:
                    if reci[counter].upper() == search_bar:
                        print("Tačno!!!")
                    else:
                        print("Reč koju ste uneli nije tačna. Tačna reč je", reci[counter])

                    counter += 1
                    if counter < len(reci):
                        kvadrati = generisi_kvadrate(slova[counter])
                    else:
                        print("Kraj igre.")
                        running = False

                    reset_search_bar()
                    show_last_line = False
            elif event.key == pygame.K_BACKSPACE:
                search_bar = search_bar[:-1]
            else:
                current_letter += event.unicode.upper()
                search_bar += event.unicode.upper()
                show_last_line = True

    screen.fill((73, 242, 242))

    for kvadrat, letter, letter_rect in kvadrati:
        pygame.draw.rect(screen, blue, kvadrat)
        screen.blit(letter, letter_rect)

    current_text = font.render(current_letter, True, blue)
    screen.blit(current_text, (20, screen_height - 50))

    if show_last_line:
        search_bar_text = font.render(search_bar, True, blue)
        screen.blit(search_text, (20, screen_height - 100))
        screen.blit(search_bar_text, (120, screen_height - 100))

    pygame.display.update()

pygame.quit()
