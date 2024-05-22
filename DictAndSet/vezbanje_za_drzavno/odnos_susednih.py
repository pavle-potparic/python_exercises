lista = list(input().split(' '))

najveci = []
najmanji = []

if lista[0] == '>':
    najveci.append('a')

else:
    najmanji.append('a')

if lista[0] == '>' and lista[1] == '<':
    najmanji.append('b')

elif lista[0] == '<' and lista[1] == '>':
    najveci.append('b')

if lista[1] == '<' and lista[2] == '>':
    najveci.append('c')

elif lista[1] == '>' and lista[2] == '<':
    najmanji.append('c')

if lista[2] == '<' and lista[3] == '>':
    najveci.append('d')

elif lista[2] == '>' and lista[3] == '<':
    najmanji.append('d')

if lista[3] == '<':
    najveci.append('e')

else:
    najmanji.append('e')

print(*najmanji, sep='')
print(*najveci, sep='')