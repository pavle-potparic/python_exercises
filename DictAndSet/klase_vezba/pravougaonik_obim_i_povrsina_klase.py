class Pravougaonik(object):

    ime = "pravougaonik"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def povrsina(self):
        return self.a * self.b

    def obim(self):
        return 2 * (self.a + self.b)


prvi_pravougaonik = Pravougaonik(4, 2)
drugi_pravougaonik = Pravougaonik(10, 5)
# print(prvi_pravougaonik.povrsina(), prvi_pravougaonik.obim())
# print(drugi_pravougaonik.povrsina(), drugi_pravougaonik.obim())

Pravougaonik.ime = "kvadrat"

print(Pravougaonik.ime)
print(prvi_pravougaonik.ime)

