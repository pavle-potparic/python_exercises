a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c < a and b < d:
    print(0)

else:
    jedan = c - a
    dva = b - d

    if jedan > dva:
        print(jedan)

    else:
        print(dva)