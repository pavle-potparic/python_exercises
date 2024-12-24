donje_x, donje_y = list(map(int, input().split(' ')))
gornje_x, gornje_y = list(map(int, input().split(' ')))

robot_x, robot_y = list(map(int, input().split(' ')))
punjac_x, punjac_y = list(map(int, input().split(' ')))

razlika_y = robot_y - punjac_y

put_x1 = 0
put_x2 = 0
put_y1 = 0
put_y2 = 0

resenje = 0

if ((robot_y > gornje_y and punjac_y < donje_y) or (robot_y < donje_y and punjac_y > gornje_y) and donje_x < robot_x < gornje_x) or ((robot_y > gornje_y and punjac_y < donje_y) or (robot_y < donje_y and punjac_y > gornje_y) and donje_x < punjac_x < gornje_x):
    put_x1 += gornje_x - robot_x + 1
    put_x2 += robot_x - donje_x + 1

    put_x1 += abs(robot_x + put_x1 - punjac_x)
    put_x2 += abs(robot_x - put_x2 - punjac_x)

    resenje += min(put_x1, put_x2) + abs(robot_y - punjac_y)

elif ((robot_x > gornje_x and punjac_x < donje_x) or (robot_x < donje_x and punjac_x > gornje_x) and donje_y < robot_y < gornje_y) or ((robot_x > gornje_x and punjac_x < donje_x) or (robot_x < donje_x and punjac_x > gornje_x) and donje_y < punjac_y < gornje_y):
    put_y1 += gornje_y - robot_y + 1
    put_y2 += robot_y - donje_y + 1

    put_y1 += abs(robot_y + put_y1 - punjac_y)
    put_y2 += abs(robot_y - put_y2 - punjac_y)

    resenje += min(put_y1, put_y2) + abs(robot_x - punjac_x)

else:
    if (gornje_y > robot_y and gornje_y > punjac_y) or (donje_y < robot_y and donje_y < punjac_y) or (gornje_y < robot_y and gornje_y < punjac_y) or (donje_y > robot_y and donje_y > punjac_y):
        if (gornje_x > robot_x and gornje_x > punjac_x) or (donje_x < robot_x and donje_x < punjac_x) or (gornje_x < robot_x and gornje_x < punjac_x) or (donje_x > robot_x and donje_x > punjac_x):
            resenje += abs(robot_y - punjac_y) + abs(robot_x - punjac_x)

        else:
            resenje += abs(robot_y - punjac_y) + abs(robot_x - punjac_x) + 2

    else:
        resenje += abs(robot_y - punjac_y) + abs(robot_x - punjac_x) + 2

print(resenje)