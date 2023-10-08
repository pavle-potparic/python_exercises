import pygame
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moj Broj Igra")

bg_color = (55, 95, 145)
number_bg_color = (80, 120, 170)
input_bg_color = (120, 150, 190)
text_color = (255, 255, 255)

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 48)


def generate_numbers():
    return [random.randint(1, 10) for _ in range(4)]


def generate_first_big_num():
    return random.randint(10, 25)


def generate_second_big_num():
    return random.randint(25, 100)


numbers = generate_numbers()
big1 = generate_first_big_num()
numbers.append(big1)
big2 = generate_second_big_num()
numbers.append(big2)

target_number = random.randint(100, 999)

user_answer = ""
input_rect = pygame.Rect(300, 500, 200, 50)
input_color = input_bg_color

attempt_used = False


def find_closest_number(target, number_list):
    closest_number = number_list[0]
    min_difference = abs(target - closest_number)
    for num in number_list:
        diff = abs(target - num)
        if diff < min_difference:
            min_difference = diff
            closest_number = num
    return closest_number


def find_expression(numbers, target):
    if len(numbers) == 1:
        if numbers[0] == target:
            return str(numbers[0])
        else:
            return None

    closest_diff = abs(target - numbers[0])
    closest_expression = ""

    for i in range(len(numbers)):
        new_numbers = numbers[:i] + numbers[i + 1:]

        plus_expr = f"({find_expression(new_numbers, target - numbers[i])}) + ({numbers[i]})"
        minus_expr = f"({find_expression(new_numbers, numbers[i] - target)}) - ({numbers[i]})"
        times_expr = f"({find_expression(new_numbers, target // numbers[i])}) * ({numbers[i]})"
        div_expr = f"({find_expression(new_numbers, target * numbers[i])}) / ({numbers[i]})"

        expressions = [plus_expr, minus_expr, times_expr, div_expr]

        for expr in expressions:
            try:
                eval_result = eval(expr)
                if abs(eval_result - target) < closest_diff:
                    closest_diff = abs(eval_result - target)
                    closest_expression = expr
            except:
                pass

    return closest_expression


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not attempt_used and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            counter = 0
            for x in range(0, len(user_answer)):
                string = ""
                x += counter
                if x >= len(user_answer)-1:
                    break
                if user_answer[x].isdigit():
                    string += str(user_answer[x])
                    for y in range(x + 1, len(user_answer)):
                        if user_answer[y].isdigit():
                            string += str(user_answer[y])
                            counter += 1

                        else:
                            break

                if string.isdigit():
                    if int(string) in numbers:
                        pass

                    else:
                        print("Brojevi koje ste koristili nisu ponudjeni")
                        pygame.quit()
                        sys.exit()

            user_answer = user_answer.strip()
            try:
                user_number = eval(user_answer)
                if user_number == target_number:
                    print("Čestitamo! Tačno rešenje!")
                else:
                    expression = find_expression(numbers, target_number)
                    if expression:
                        print("Najbliži izraz za tačan rezultat:", expression)
                        print("Rezultat:", eval(expression))
                        print("Korisnikov konacan rezultat:", user_number)
                    else:
                        closest_num = find_closest_number(target_number, numbers)
                        print("Nije pronađen tačan izraz ili blizak rezultat.")
                        print("Najbliži mogući broj:", closest_num)
                attempt_used = True
            except:
                print("Pogrešan unos. Pokušajte ponovo.")
            user_answer = ""

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_answer = user_answer[:-1]
            else:
                user_answer += event.unicode

    screen.fill(bg_color)

    target_text = big_font.render(str(target_number), True, text_color)
    target_rect = target_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(target_text, target_rect)

    square_size = 100
    x = 50
    y = 150
    for num in numbers:

        pygame.draw.rect(screen, number_bg_color, (x, y, square_size, square_size))
        text = font.render(str(num), True, text_color)
        text_rect = text.get_rect(center=(x + square_size / 2, y + square_size / 2))
        screen.blit(text, text_rect)
        x += square_size + 20

    pygame.draw.rect(screen, input_color, input_rect, 2)
    input_text = font.render(user_answer, True, text_color)
    input_rect.width = max(200, input_text.get_width() + 10)
    screen.blit(input_text, (input_rect.x + 5, input_rect.y + 5))
    input_rect.y = 500

    pygame.display.flip()


pygame.quit()
sys.exit()