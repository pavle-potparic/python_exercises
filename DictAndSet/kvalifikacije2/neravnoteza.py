dete1 = int(input())
dete2 = int(input())
dete3 = int(input())
dete4 = int(input())

lista = [dete1, dete2, dete3, dete4]

lista.sort()

resenje = abs((lista[0] + lista[3]) - (lista[1] + lista[2]))

if resenje == 0:
    print("da")
    print(0)

elif resenje % 2 == 0:
    if resenje / 2 < 5:
        print("da")
        print(resenje // 2)
    else:
        print("ne")

else:
    print("ne")