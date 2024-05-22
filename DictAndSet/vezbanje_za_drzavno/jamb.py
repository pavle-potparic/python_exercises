bacanje = list(map(int, input().split(" ")))
temp_bacanje = set(bacanje)
temp_temp_bacanje = list(temp_bacanje)

if len(temp_bacanje) == 1:
    print(5)

elif len(temp_bacanje) == 2:
    if bacanje.count(bacanje[0]) == 1 or bacanje.count(bacanje[0]) == 4:
        print(4)

    else:
        print('3+2')

elif len(temp_bacanje) == 3:
    if bacanje.count(temp_temp_bacanje[0]) == 3 or bacanje.count(temp_temp_bacanje[1]) == 3 or bacanje.count(temp_temp_bacanje[2]) == 3:
        print(3)

    else:
        print('2+2')

elif len(temp_bacanje) == 4:
    print(2)

else:
    print('-')