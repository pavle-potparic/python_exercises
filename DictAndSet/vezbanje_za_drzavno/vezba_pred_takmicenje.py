niz = [1, 1, 5, 4, 7]
# resenje = [i for i, z in enumerate(niz) if z > 1]
#
# niz.sort(key=lambda k: (k[0], k[1], k))

resenje = [i for i, z in enumerate(niz) if z > 1]
niz.sort(key=lambda k: (k[1], k))