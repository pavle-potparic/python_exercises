import pygame
import sys
import sqlite3
import random
import time

pygame.init()

width, height = 1200, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Countries')

BACKGROUND_COLOR = (220, 220, 255)
BUTTON_COLOR = (50, 50, 150)
BUTTON_HOVER_COLOR = (70, 70, 200)
TEXT_COLOR = (255, 255, 255)
TITLE_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

font = pygame.font.SysFont('Helvetica', 30)
font_bold = pygame.font.SysFont('Helvetica', 30, bold=True)
title_font = pygame.font.SysFont('Helvetica', 40, bold=True)
team_font = pygame.font.SysFont('Helvetica', 20)
team_font_bold = pygame.font.SysFont('Helvetica', 20, bold=True)

countries = ['Spain', 'England', 'France', 'Germany', 'Italy']

conn = sqlite3.connect('football_leagues.db')
cursor = conn.cursor()

buy = False
klupa = False
is_transfer_listed = False
budget = 90


def get_players(starting_with):
    cursor.execute("SELECT name FROM players WHERE name LIKE ? LIMIT 8", ('%' + starting_with + '%',))
    return [row[0] for row in cursor.fetchall()]


def draw_text_box(text):
    pygame.draw.rect(screen, WHITE, (450, 200, 500, 40))
    txt_surface = font.render(text, True, BLACK)
    screen.blit(txt_surface, (455, 205))


def draw_drop_down(players):
    y = 300
    for player in players:
        for row in cursor.execute('SELECT value FROM players WHERE name = "{}"'.format(player)):
            value = str(row[0])
        pygame.draw.rect(screen, GRAY, (450, y, 500, 40))
        pygame.draw.rect(screen, BLACK, (900, y, 85, 40))
        txt_surface = font.render(player, True, BLACK)
        screen.blit(txt_surface, (455, y + 5))
        text_value = font.render(str(value) + 'M$', True, WHITE)
        screen.blit(text_value, (900, y))
        y += 50


def create_dict():
    teams_and_players1 = {}

    for col in cursor.execute('SELECT countries.name, countries.id FROM countries'):
        country_name = col[0]
        country_id = col[1]

        if country_name not in teams_and_players1:
            teams_and_players1[country_name] = {}

        for row in cursor.execute(
                'SELECT teams.name, players.name, players.rating, players.picture, players.position, players.value, players.is_starting FROM players JOIN teams ON players.team_id = teams.id JOIN countries ON teams.country_id = countries.id WHERE countries.id = {}'.format(
                    country_id)):
            team_name = row[0]
            player_name = row[1]
            player_rating = row[2]
            player_picture = row[3]
            player_position = row[4]
            player_value = row[5]
            if row[6] == '1':
                player_is_starting = True

            elif row[6] == '0':
                player_is_starting = False

            else:
                player_is_starting = None

            if team_name not in teams_and_players1[country_name]:
                teams_and_players1[country_name][team_name] = {}

            teams_and_players1[country_name][team_name][player_name] = [
                player_rating,
                player_picture,
                player_position,
                player_value,
                player_is_starting
            ]

    return teams_and_players1


teams_and_players1 = create_dict()


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


start_rating = 0
start = False

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
                        team_rating = 0
                        screen.fill(BACKGROUND_COLOR)
                        running = True

                        while running:
                            button_rect = pygame.Rect((150, 700, 75, 75))
                            if button_rect.collidepoint(pygame.mouse.get_pos()):
                                pygame.draw.rect(screen, (240, 119, 43), button_rect)
                                text_surface = team_font_bold.render('Bench', True, TEXT_COLOR)
                                text_rect = text_surface.get_rect(center=button_rect.center)
                                screen.blit(text_surface, text_rect)
                            else:
                                pygame.draw.rect(screen, (196, 89, 22), button_rect)
                                text_surface = font.render('Bench', True, TEXT_COLOR)
                                text_rect = text_surface.get_rect(center=button_rect.center)
                                screen.blit(text_surface, text_rect)

                            buy_rect = pygame.Rect((1100, 700, 75, 75))
                            if buy_rect.collidepoint(pygame.mouse.get_pos()):
                                pygame.draw.rect(screen, (92, 237, 170), buy_rect)
                                text_surface = team_font_bold.render('BUY', True, TEXT_COLOR)
                                text_rect = text_surface.get_rect(center=buy_rect.center)
                                screen.blit(text_surface, text_rect)

                            else:
                                pygame.draw.rect(screen, (28, 214, 109), buy_rect)
                                text_surface = font.render('BUY', True, TEXT_COLOR)
                                text_rect = text_surface.get_rect(center=buy_rect.center)
                                screen.blit(text_surface, text_rect)

                            start_rect = pygame.Rect((1000, 250, 150, 75))
                            if start_rect.collidepoint(pygame.mouse.get_pos()):
                                pygame.draw.rect(screen, (92, 237, 170), start_rect)
                                text_surface = team_font_bold.render('Start season', True, TEXT_COLOR)
                                text_rect = text_surface.get_rect(center=start_rect.center)
                                screen.blit(text_surface, text_rect)

                            else:
                                pygame.draw.rect(screen, (28, 214, 109), start_rect)
                                text_surface = font.render('Start season', True, TEXT_COLOR)
                                text_rect = text_surface.get_rect(center=start_rect.center)
                                screen.blit(text_surface, text_rect)

                            sell_rect = pygame.Rect((1000, 700, 75, 75))
                            if sell_rect.collidepoint(pygame.mouse.get_pos()):
                                pygame.draw.rect(screen, (250, 90, 90), sell_rect)
                                text_surface = team_font_bold.render('SELL', True, TEXT_COLOR)
                                text_rect = text_surface.get_rect(center=sell_rect.center)
                                screen.blit(text_surface, text_rect)

                            else:
                                pygame.draw.rect(screen, (189, 13, 13), sell_rect)
                                text_surface = font.render('SELL', True, TEXT_COLOR)
                                text_rect = text_surface.get_rect(center=sell_rect.center)
                                screen.blit(text_surface, text_rect)

                            budget_rect = pygame.Rect((1050, 150, 100, 75))
                            pygame.draw.rect(screen, (76, 235, 68), budget_rect)
                            text_surface = font.render(str(budget) + 'M$', True, TEXT_COLOR)
                            text_rect = text_surface.get_rect(center=budget_rect.center)
                            screen.blit(text_surface, text_rect)

                            if start_rating == 1:
                                rating_rect = pygame.Rect((100, 150, 100, 75))
                                pygame.draw.rect(screen, (72, 200, 217), rating_rect)
                                text_surface = font.render(str(team_rating) + ' OVR', True, TEXT_COLOR)
                                text_rect = text_surface.get_rect(center=rating_rect.center)
                                screen.blit(text_surface, text_rect)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    if button_rect.collidepoint(event.pos):
                                        klupa = True
                                        screen.fill(BACKGROUND_COLOR)
                                        pygame.display.update()

                                    elif sell_rect.collidepoint(event.pos):
                                        x = 170
                                        y = 200
                                        lista = []
                                        counter = 0
                                        is_transfer_listed = True
                                        for key, val in teams_and_players1[selected_country][button_text].items():
                                            if not val[-1]:
                                                screen.fill(BACKGROUND_COLOR)
                                                pict = pygame.image.load(val[1])
                                                scaled_image = pygame.transform.scale(pict, (150, 150))
                                                screen.blit(scaled_image, (x, y))
                                                lista.append((scaled_image, (x, y, 150, 150), key))
                                                x += 200
                                                counter += 1
                                                if counter == 5:
                                                    y += 200
                                                    x = 170
                                            pygame.display.update()

                                    elif buy_rect.collidepoint(event.pos):
                                        buy = True

                                    elif start_rect.collidepoint(event.pos):
                                        start = True

                                    while klupa:
                                        x = 170
                                        y = 200
                                        lista = []
                                        counter = 0

                                        for key, val in teams_and_players1[selected_country][button_text].items():
                                            if not val[-1]:
                                                pict = pygame.image.load(val[1])
                                                scaled_image = pygame.transform.scale(pict, (150, 150))
                                                screen.blit(scaled_image, (x, y))
                                                lista.append((scaled_image, (x, y, 150, 150), key))
                                                x += 200
                                                counter += 1
                                                if counter == 5:
                                                    y += 200
                                                    x = 170
                                        pygame.display.update()

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                screen.fill(BACKGROUND_COLOR)
                                                klupa = False

                                            elif event.type == pygame.MOUSEBUTTONDOWN:

                                                mouse_x, mouse_y = event.pos

                                                for _, (img_x, img_y, img_w, img_h), key in lista:
                                                    if img_x <= mouse_x <= img_x + img_w and img_y <= mouse_y <= img_y + img_h:
                                                        change_player = str(key)
                                                        change = False
                                                        lista1 = []
                                                        screen.fill(BACKGROUND_COLOR)
                                                        while not change:
                                                            y = 640
                                                            x = 100
                                                            counter = 0

                                                            for player, image in \
                                                                    teams_and_players1[selected_country][
                                                                        button_text].items():
                                                                if counter == 0:
                                                                    x = 300

                                                                if counter == 5 or counter == 8:
                                                                    x = 300
                                                                else:
                                                                    if counter == 1:
                                                                        x = 220
                                                                        y -= 160

                                                                    else:
                                                                        x += 200

                                                                if counter == 5 or counter == 8:
                                                                    y -= 160

                                                                if image[-1]:
                                                                    pict = pygame.image.load(image[1])
                                                                    scaled_image = pygame.transform.scale(pict, (
                                                                        150, 150))
                                                                    screen.blit(scaled_image, (x, y))
                                                                    lista1.append(
                                                                        (scaled_image, (x, y, 150, 150), player))
                                                                    counter += 1

                                                                for event in pygame.event.get():
                                                                    if event.type == pygame.QUIT:
                                                                        klupa = False

                                                                    elif event.type == pygame.MOUSEBUTTONDOWN:

                                                                        mouse_x1, mouse_y1 = event.pos

                                                                        for _, (img_x1, img_y1, img_w1,
                                                                                img_h1), key1 in lista1:
                                                                            if img_x1 <= mouse_x1 <= img_x1 + img_w1 and img_y1 <= mouse_y1 <= img_y1 + img_h1:
                                                                                change_player2 = str(key1)
                                                                                for z in cursor.execute(
                                                                                        "SELECT * FROM players WHERE name = '{}'".format(
                                                                                            key1)):
                                                                                    player_id = z[0]
                                                                                    player_name = z[1]
                                                                                    player_rating = z[2]
                                                                                    player_picture = z[3]
                                                                                    player_position = z[4]
                                                                                    player_value = z[5]
                                                                                    player_is_starting = z[6]
                                                                                    break

                                                                                for q in cursor.execute(
                                                                                        "SELECT * FROM players WHERE name = '{}'".format(
                                                                                            change_player)):
                                                                                    player2_id = q[0]
                                                                                    cursor.execute(
                                                                                        'UPDATE players SET name = "{}", rating = {}, picture = "{}", position = "{}", value = {}, is_starting = {} WHERE id = {}'.format(
                                                                                            q[1], q[2], q[3], q[4],
                                                                                            q[5], 1, player_id))

                                                                                cursor.execute(
                                                                                    'UPDATE players SET name = "{}", rating = {}, picture = "{}", position = "{}", value = {}, is_starting = {} WHERE id = {}'.format(
                                                                                        player_name, player_rating,
                                                                                        player_picture, player_position,
                                                                                        player_value, 0, player2_id))

                                                                                teams_and_players1 = create_dict()

                                                                                klupa = False
                                                                                change = True
                                                                                break

                                                            pygame.display.update()

                                    while is_transfer_listed:
                                        x = 170
                                        y = 200
                                        lista = []
                                        counter = 0

                                        for key, val in teams_and_players1[selected_country][button_text].items():
                                            if not val[-1]:
                                                pict = pygame.image.load(val[1])
                                                scaled_image = pygame.transform.scale(pict, (150, 150))
                                                screen.blit(scaled_image, (x, y))
                                                budget_rect = pygame.Rect((x, y + 150, 100, 75))
                                                pygame.draw.rect(screen, (0, 0, 0), budget_rect)
                                                text_surface = font.render(str(val[3]) + 'M$', True, TEXT_COLOR)
                                                text_rect = text_surface.get_rect(center=budget_rect.center)
                                                screen.blit(text_surface, text_rect)
                                                lista.append((scaled_image, (x, y, 150, 150), key))
                                                x += 200
                                                counter += 1
                                                if counter == 5:
                                                    y += 200
                                                    x = 170
                                        pygame.display.update()

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                screen.fill(BACKGROUND_COLOR)
                                                is_transfer_listed = False

                                            elif event.type == pygame.MOUSEBUTTONDOWN:

                                                mouse_x, mouse_y = event.pos

                                                for _, (img_x, img_y, img_w, img_h), key in lista:
                                                    if img_x <= mouse_x <= img_x + img_w and img_y <= mouse_y <= img_y + img_h:
                                                        new_counter = 0
                                                        for n in cursor.execute(
                                                                'SELECT teams.id FROM teams JOIN countries ON teams.country_id = countries.id WHERE countries.name = "{}"'.format(
                                                                    selected_country)):
                                                            if new_counter == 0:
                                                                first = int(n[0])
                                                            new_counter += 1
                                                            last = int(n[0])

                                                        for i in cursor.execute(
                                                                'SELECT value, team_id FROM players WHERE name = "{}"'.format(
                                                                    key)):
                                                            budget += i[0]
                                                            new_id = random.randint(first, last)

                                                            cursor.execute(
                                                                "UPDATE players SET team_id = {} WHERE name = '{}'".format(
                                                                    new_id, key))

                                                        teams_and_players1 = create_dict()

                                                        is_transfer_listed = False
                                                        screen.fill(BACKGROUND_COLOR)
                                    input_text = ''
                                    filtered_players = get_players('')
                                    while buy:
                                        screen.fill(BACKGROUND_COLOR)
                                        draw_text_box(input_text)
                                        draw_drop_down(filtered_players)

                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                screen.fill(BACKGROUND_COLOR)
                                                buy = False
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_BACKSPACE:
                                                    input_text = input_text[:-1]
                                                else:
                                                    input_text += event.unicode
                                                filtered_players = get_players(input_text)
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                                if 300 <= mouse_x <= 900:
                                                    index = (mouse_y - 300) // 50
                                                    if 0 <= index < len(filtered_players):
                                                        for z in cursor.execute(
                                                                'SELECT players.value, teams.name, teams.id FROM players JOIN teams ON players.team_id = teams.id WHERE players.name = "{}"'.format(
                                                                    filtered_players[index])):
                                                            pass
                                                        number_of_players = 0

                                                        for w in cursor.execute(
                                                                'SELECT * FROM players WHERE players.team_id = {}'.format(
                                                                    z[2])):
                                                            number_of_players += 1

                                                        if z[1] == button_text:
                                                            print('Imas tog igraca')

                                                        elif z[0] > budget:
                                                            print('Nemas dovoljno para')

                                                        elif number_of_players < 12:
                                                            print(
                                                                'Tim iz kog je igrac koga zelite da kupite nema dovoljno igraca')

                                                        else:
                                                            for p in cursor.execute(
                                                                    'SELECT id FROM teams WHERE name = "{}"'.format(
                                                                        button_text)):
                                                                p = int(p[0])
                                                            cursor.execute(
                                                                'UPDATE players SET team_id = {}, is_starting = 0 WHERE name = "{}"'.format(
                                                                    p, filtered_players[index]))
                                                            teams_and_players1 = create_dict()
                                                            budget -= z[0]
                                                            print(teams_and_players1)

                                                        screen.fill(BACKGROUND_COLOR)
                                                        buy = False

                                        pygame.display.update()

                                    while start:

                                        screen.fill(BACKGROUND_COLOR)
                                        rating_list = []
                                        team_names_list = []
                                        teams_and_players1 = create_dict()

                                        for team_name, values in teams_and_players1[selected_country].items():
                                            if team_name != button_text:
                                                team_names_list.append(team_name)
                                                j = 0
                                                counter1 = 0
                                                for z, q in values.items():
                                                    j += q[0]
                                                    counter1 += 1

                                                rating_list.append(j // counter1)

                                            else:
                                                team_names_list.append(button_text)
                                                rating_list.append(team_rating)

                                        dictionary = dict(zip(team_names_list, rating_list))

                                        final_list = []
                                        counter2 = 1
                                        for x in range(0, len(team_names_list)):
                                            if counter2 == 1:
                                                final_list.append([int(0), 'picture/united_crest.jpg', 0, 0])

                                            if counter2 == 2:
                                                final_list.append([int(0), 'picture/liverpool_crest.jpg', 0, 0])

                                            if counter2 == 3:
                                                final_list.append([int(0), 'picture/city_crest.jpg', 0, 0])

                                            if counter2 == 4:
                                                final_list.append([int(0), 'picture/chelsea_crest.jpg', 0, 0])

                                            if counter2 == 5:
                                                final_list.append([int(0), 'picture/arsenal_crest.jpg', 0, 0])

                                            counter2 += 1

                                        final_dict = dict(zip(team_names_list, final_list))
                                        print(final_dict)

                                        for real_key, real_value in dictionary.items():
                                            for fake_key, fake_value in dictionary.items():

                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        conn.close()
                                                        pygame.quit()
                                                        sys.exit()

                                                if real_key == fake_key:
                                                    pass

                                                else:
                                                    print(final_dict)
                                                    difference = abs(real_value - fake_value)
                                                    if real_value > fake_value:

                                                        win = 33 + (difference * 3)
                                                        draw = win + 33
                                                        lose = draw + win

                                                    elif fake_value > real_value:

                                                        win = 33 - (difference * 3)
                                                        draw = win + 33
                                                        if win < 0:
                                                            win = 0

                                                        lose = win + draw

                                                    else:
                                                        win = 33
                                                        draw = 66
                                                        lose = 99

                                                    chance = random.randint(0, 99)

                                                    if chance <= win:
                                                        final_dict[real_key][0] += 3
                                                        home = random.randint(1, 5)
                                                        away = random.randint(0, 4)
                                                        if away > home:
                                                            temp = int(home)
                                                            home = int(away)
                                                            away = int(temp)
                                                        if away == home:
                                                            home += 1
                                                        text = 'HOME WIN'
                                                        final_dict[real_key][3] += home
                                                        final_dict[real_key][2] += home - away

                                                        final_dict[fake_key][3] += away
                                                        final_dict[fake_key][2] += away - home

                                                    elif chance <= draw:
                                                        final_dict[real_key][0] += 1
                                                        final_dict[fake_key][0] += 1
                                                        home = random.randint(0, 4)
                                                        away = int(home)
                                                        final_dict[real_key][3] += int(home)
                                                        final_dict[fake_key][3] += int(home)

                                                        text = 'DRAW'

                                                    else:
                                                        final_dict[fake_key][0] += 3
                                                        home = random.randint(0, 4)
                                                        away = random.randint(1, 5)
                                                        if away < home:
                                                            temp = int(away)
                                                            away = int(home)
                                                            home = int(temp)
                                                        if away == home:
                                                            away += 1

                                                        final_dict[real_key][3] += home
                                                        final_dict[real_key][2] += home - away
                                                        final_dict[fake_key][3] += away
                                                        final_dict[fake_key][2] += away - home
                                                        text = 'AWAY WIN'

                                                    pict = pygame.image.load(final_dict[real_key][1])
                                                    scaled_image = pygame.transform.scale(pict, (300, 300))
                                                    screen.blit(scaled_image, (100, 130))

                                                    pict2 = pygame.image.load(final_dict[fake_key][1])
                                                    scaled_image2 = pygame.transform.scale(pict2, (300, 300))
                                                    screen.blit(scaled_image2, (700, 130))

                                                    result_font = pygame.font.SysFont('Helvetica', 40)
                                                    score_rect = pygame.Rect((450, 520, 200, 60))
                                                    result = pygame.Rect((450, 400, 200, 200))
                                                    pygame.draw.rect(screen, 'blue', score_rect)
                                                    pygame.draw.rect(screen, 'blue', result)
                                                    text_surface = team_font_bold.render(text, True, TEXT_COLOR)
                                                    result_surface = result_font.render(str(home) + ' : ' + str(away),
                                                                                        True, TEXT_COLOR)
                                                    text_rect2 = result_surface.get_rect(center=score_rect.center)
                                                    text_rect = text_surface.get_rect(center=result.center)
                                                    screen.blit(result_surface, text_rect2)
                                                    screen.blit(text_surface, text_rect)

                                                    pygame.display.update()
                                                    time.sleep(2)

                                        screen.fill(BACKGROUND_COLOR)
                                        x = 550
                                        y = 130
                                        final_dict = dict(sorted(final_dict.items(), key=lambda item: (item[1][2], item[1][3]), reverse=True))
                                        for o, e in final_dict.items():
                                            result = pygame.Rect((x, y, 200, 100))
                                            pygame.draw.rect(screen, 'blue', result)
                                            text_surface = team_font_bold.render(str(o) + ' ' + str(e[0]) + ' ' + str(e[2]) + ' ' + str(e[3]), True,
                                                                                 TEXT_COLOR)
                                            text_rect = text_surface.get_rect(center=result.center)
                                            screen.blit(text_surface, text_rect)
                                            y += 120

                                        pygame.display.update()
                                        time.sleep(15)
                                        screen.fill(BACKGROUND_COLOR)
                                        pygame.display.update()
                                        start = False

                            temp = 0
                            for team, players in teams_and_players1[selected_country].items():
                                team_id = cursor.lastrowid

                                if team == button_text:
                                    selected_team = str(button_text)
                                    y = 640
                                    x = 100
                                    counter = 0
                                    for player, image in players.items():

                                        if 0 < counter < 5 and image[-1]:
                                            for p in cursor.execute(
                                                    "SELECT position FROM players WHERE name = '{}'".format(player)):
                                                if str(p[0]) == 'GK':
                                                    if image[-1]:
                                                        temp -= 50
                                                        print(player)

                                                elif str(p[0]) == 'MID':
                                                    if image[-1]:
                                                        temp -= 30
                                                        print(player)
                                                elif str(p[0]) == 'ATK':
                                                    if image[-1]:
                                                        temp -= 40
                                                        print(player)

                                        elif 5 <= counter < 8 and image[-1]:
                                            for p in cursor.execute(
                                                    "SELECT position FROM players WHERE name = '{}'".format(player)):
                                                if str(p[0]) == 'DEF':
                                                    if image[-1]:
                                                        temp -= 15
                                                        print(player)

                                                elif str(p[0]) == 'GK':
                                                    if image[-1]:
                                                        temp -= 60
                                                        print(player)
                                                elif str(p[0]) == 'ATK':
                                                    if image[-1]:
                                                        temp -= 30
                                                        print(player)

                                        elif counter > 8 and image[-1]:
                                            for p in cursor.execute(
                                                    "SELECT position FROM players WHERE name = '{}'".format(player)):
                                                if str(p[0]) == 'DEF':
                                                    if image[-1]:
                                                        temp -= 40
                                                        print(player)

                                                elif str(p[0]) == 'MID':
                                                    if image[-1]:
                                                        temp -= 20
                                                        print(player)
                                                elif str(p[0]) == 'GK':
                                                    if image[-1]:
                                                        temp -= 70
                                                        print(player)

                                        if counter == 0:
                                            x = 300
                                            for p in cursor.execute(
                                                    "SELECT position FROM players WHERE name = '{}'".format(player)):
                                                if str(p[0]) == 'DEF':
                                                    if image[-1]:
                                                        temp -= 25


                                                elif str(p[0]) == 'MID':
                                                    if image[-1]:
                                                        temp -= 30

                                                elif str(p[0]) == 'ATK':
                                                    if image[-1]:
                                                        temp -= 40

                                        if counter == 5 or counter == 8:
                                            x = 300
                                            y -= 160

                                        else:
                                            if counter == 1:
                                                x = 220
                                                y -= 160
                                            else:
                                                x += 200

                                        if image[-1]:
                                            temp += image[0]
                                            pict = pygame.image.load(image[1])
                                            scaled_image = pygame.transform.scale(pict, (150, 150))
                                            screen.blit(scaled_image, (x, y))
                                            counter += 1

                            temp = temp // 11
                            team_rating = int(temp)

                            start_rating = 1
                            pygame.display.update()
                        break

    pygame.display.flip()

print(budget)
pygame.quit()
sys.exit()
