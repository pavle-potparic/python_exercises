po_komadu = int(input())
po_desetci = int(input())
komadi = int(input())

resenje = 0
temp = int(komadi)

if po_komadu * 10 > po_desetci and komadi >= 10:
    resenje += komadi // 10 * po_desetci
    temp -= komadi // 10 * 10
    if temp != 0:
        resenje += temp * po_komadu

else:
    resenje = komadi * po_komadu

print(resenje)