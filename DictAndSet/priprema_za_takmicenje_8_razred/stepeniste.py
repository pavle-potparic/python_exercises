metri = int(input())
centimetri = int(input())

metri *= 100

ukupno = metri + centimetri

stepenice = ukupno // 16 * 30 + 30

resenje = list(str(stepenice / 100).split('.'))

resenje[1] += '0'

print(*resenje, sep=' ')