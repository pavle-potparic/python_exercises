jarde1, stope1, inci1 = list(map(int, input().rstrip().split(" ")))
jarde2, stope2, inci2 = list(map(int, input().rstrip().split(" ")))
jarde3, stope3, inci3 = list(map(int, input().rstrip().split(" ")))

centimetri1 = inci1 * 2.54 + stope1 * 2.54 * 12 + jarde1 * 2.54 * 12 * 3
centimetri2 = inci2 * 2.54 + stope2 * 2.54 * 12 + jarde2 * 2.54 * 12 * 3
centimetri3 = inci3 * 2.54 + stope3 * 2.54 * 12 + jarde3 * 2.54 * 12 * 3

lista = [centimetri3, centimetri2, centimetri1]

resenje = max(lista)

if resenje != int(resenje):
    if resenje - int(resenje) > 0.5:
        resenje = int(resenje) + 1
    else:
        resenje = int(resenje)

resenje1 = resenje // 100
resenje2 = resenje - (resenje1*100)

print(resenje1, resenje2)

lista.sort(key=lambda k: (k[0], -k[1]), reverse=True)
lista.sort(key=lambda k: (k[0], -k[1]), reverse=True)