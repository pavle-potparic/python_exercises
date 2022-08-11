f0 = 0
f1 = 1
while f0 + f1 < 10000:
    x = f1
    f1 = f0 + f1
    f0 = x
    print(f1)
