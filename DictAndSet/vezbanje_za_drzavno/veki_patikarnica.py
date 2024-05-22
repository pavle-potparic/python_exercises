class Patika:
    def __init__(self, ime, vrednost):
        self.ime = ime
        self.vrednost = vrednost

def main():
    n = int(input())
    patike = []
    for _ in range(n):
        ime, vrednost = input().split()
        vrednost = int(vrednost)
        patike.append(Patika(ime, vrednost))

    patike.sort(key=lambda x: (-x.vrednost, x.ime))

    k = int(input())
    for _ in range(k):
        budget = int(input())
        najskuplje = -1
        if budget < patike[-1].vrednost:
            print("nema")
        else:
            for p in patike:
                if p.vrednost <= budget and najskuplje == p.vrednost:
                    print(f"{p.ime} {p.vrednost}")
                elif najskuplje == -1 and p.vrednost <= budget:
                    najskuplje = p.vrednost
                    print(f"{p.ime} {p.vrednost}")
                elif najskuplje > p.vrednost:
                    break

if __name__ == "__main__":
    main()
