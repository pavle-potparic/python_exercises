pin = input()
lista = list(str(pin))

resenje = int(pin) + (int(lista[3] + lista[1] + lista[2] + lista[0])) + (int(lista[0] + lista[2] + lista[1] + lista[3]))

kraj = list(str(resenje))

if pin != '0000':
    print(*kraj[len(kraj)-4: len(kraj)], sep='')

else:
    print('0000')