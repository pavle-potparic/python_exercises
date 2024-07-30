import pygame
import sys
import sqlite3

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Countries')

BACKGROUND_COLOR = (220, 220, 255)
BUTTON_COLOR = (50, 50, 150)
BUTTON_HOVER_COLOR = (70, 70, 200)
TEXT_COLOR = (255, 255, 255)
TITLE_COLOR = (0, 0, 0)

font = pygame.font.SysFont('Helvetica', 30)
font_bold = pygame.font.SysFont('Helvetica', 30, bold=True)
title_font = pygame.font.SysFont('Helvetica', 40, bold=True)
team_font = pygame.font.SysFont('Helvetica', 20)
team_font_bold = pygame.font.SysFont('Helvetica', 20, bold=True)

countries = ['Spain', 'England', 'France', 'Germany', 'Italy']

conn = sqlite3.connect('football_leagues.db')
cursor = conn.cursor()


def get_teams(country_name):
    cursor.execute('''
    SELECT teams.name FROM teams
    JOIN countries ON teams.country_id = countries.id
    WHERE countries.name = ?
    ''', (country_name,))
    teams = cursor.fetchall()
    return [team[0] for team in teams]


selected_country = None


def draw_buttons(buttons, title, is_team_buttons=False):
    screen.fill(BACKGROUND_COLOR)

    title_surface = title_font.render(title, True, TITLE_COLOR)
    title_rect = title_surface.get_rect(center=(width // 2, 240))
    screen.blit(title_surface, title_rect)

    if is_team_buttons:
        button_width, button_height = 250, 30
        gap = 0
        font_used = team_font
        font_bold_used = team_font_bold
    else:
        button_width, button_height = 300, 60
        gap = 20
        font_used = font
        font_bold_used = font_bold

    total_height = len(buttons) * button_height + (len(buttons) - 1) * gap
    start_y = (height - total_height) // 2

    button_rects = []

    for i, button_text in enumerate(buttons):
        y = start_y + i * (button_height + gap)
        button_rect = pygame.Rect((width // 2 - button_width // 2, y, button_width, button_height))

        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect)
            text_surface = font_bold_used.render(button_text, True, TEXT_COLOR)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
            text_surface = font_used.render(button_text, True, TEXT_COLOR)

        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

        button_rects.append((button_rect, button_text))

    return button_rects


running = True
while running:
    if selected_country:
        buttons = get_teams(selected_country)
        title = f""
        button_rects = draw_buttons(buttons, title, is_team_buttons=True)
    else:
        buttons = countries
        title = "Select League"
        button_rects = draw_buttons(buttons, title)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button_rect, button_text in button_rects:
                if button_rect.collidepoint(event.pos):
                    if not selected_country:
                        selected_country = button_text
                    else:
                        print(f"Selected team: {button_text}")
                    break

    pygame.display.flip()

pygame.quit()
sys.exit()
