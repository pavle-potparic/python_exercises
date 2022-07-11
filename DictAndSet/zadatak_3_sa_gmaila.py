# promena brzine = ubrzanje * vremenski interval
# v = promena brzine * vremenski interval
metri_po_sekundi = int(input("Unesi metre po sekundi. "))
vremenski_interval = int(input("Unesi vreme u sekundama. "))


def ubrzanje(metri_u_sekundi, vreme):
    brzina = metri_u_sekundi * vreme
    predjeni_put = brzina * vreme
    return str(brzina) + "m/s", str(predjeni_put) + "m"


stampanje = ubrzanje(metri_po_sekundi, vremenski_interval)
print(stampanje)
