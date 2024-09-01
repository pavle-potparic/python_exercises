import pygame
import sys
import sqlite3

pygame.init()

WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

font = pygame.font.SysFont(None, 30)

conn = sqlite3.connect('football_leagues.db')
cursor = conn.cursor()


def get_players(starting_with):
    cursor.execute("SELECT name FROM players WHERE name LIKE ? LIMIT 5", (starting_with + '%',))
    return [row[0] for row in cursor.fetchall()]


def draw_text_box(text):
    pygame.draw.rect(win, WHITE, (50, 50, 500, 40))
    txt_surface = font.render(text, True, BLACK)
    win.blit(txt_surface, (55, 55))


def draw_drop_down(players):
    y = 100
    for player in players:
        pygame.draw.rect(win, GRAY, (50, y, 500, 40))
        txt_surface = font.render(player, True, BLACK)
        win.blit(txt_surface, (55, y + 5))
        y += 50


input_text = ''
filtered_players = get_players('')
while True:
    win.fill(BLUE)
    draw_text_box(input_text)
    draw_drop_down(filtered_players)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            conn.close()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
            filtered_players = get_players(input_text)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 50 <= mouse_x <= 550:
                index = (mouse_y - 100) // 50
                if 0 <= index < len(filtered_players):
                    print(filtered_players[index])

    pygame.display.update()
