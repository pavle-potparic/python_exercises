broj_sibica = int(input())

sibice = list(map(int, input().split(" ")))

sibice.sort(reverse=True)

suma = sum(sibice)


def izvuci_upotrebljene_sibice(stranica_kvadrata, sibice):
    start = 0
    sum = 0
    for end in range(0, len(sibice)):
        sum += sibice[end]
        while sum > stranica_kvadrata and start <= end:
            sum -= sibice[start]
            start += 1
        if sum == stranica_kvadrata:
            del sibice[start:end+1]
            return True
    return False


if suma % 4 != 0:
    print(0)

elif max(sibice) > suma / 4:
    print(0)

else:
    stranica = suma // 4
    stranica_1 = izvuci_upotrebljene_sibice(stranica, sibice)
    stranica_2, stranica_3, stranica_4 = False, False, False
    if stranica_1:
        stranica_2 = izvuci_upotrebljene_sibice(stranica, sibice)
    if stranica_2:
        stranica_3 = izvuci_upotrebljene_sibice(stranica, sibice)
    if stranica_3:
        stranica_4 = izvuci_upotrebljene_sibice(stranica, sibice)
    if stranica_4:
        print(1)
    else:
        print(0)
