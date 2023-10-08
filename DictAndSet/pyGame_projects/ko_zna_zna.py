import pygame
import random


lista_pitanja = [
    "Ko je bio glavni autor Američke Deklaracije nezavisnosti?",
    "Kada je Američka Deklaracija nezavisnosti usvojena?",
    "Koja je osnovna poruka Američke Deklaracije nezavisnosti?",
    "Ko je potpisao Američku Deklaraciju nezavisnosti?",
    "Koji je poznat izraz iz Američke Deklaracije nezavisnosti kojim se ističe pravo na 'život, slobodu i potragu za srećom'?",
    "Kako su se potpisnici Američke Deklaracije nezavisnosti izlagali riziku?",
    "Koji datum se obeležava kao Dan nezavisnosti u Sjedinjenim Američkim Državama?",
    "Kako je Deklaracija nezavisnosti uticala na odnos između SAD-a i Velike Britanije?",
    "Ko je potpisao Deklaraciju nezavisnosti kao prvi?",
    "Šta je bila osnovna svrha Deklaracije nezavisnosti?",
    "Koji sektor ekonomije je bio najviše pogođen Prvom industrijskom revolucijom?",
    "Koji je izum bio ključan za razvoj fabričke proizvodnje tokom Prve industrijske revolucije?",
    "Gde je Prva industrijska revolucija prvo započela?",
    "Koji sektor je pretrpeo najveće promene u produktivnosti tokom Prve industrijske revolucije?",
    "Koja nova izvor energije je zamenila ljudsku i životinjsku snagu tokom Prve industrijske revolucije?",
    "Kako je Prva industrijska revolucija uticala na urbanizaciju?",
    "Koja je promena u proizvodnji najviše doprinela rastućem broju fabrika tokom Prve industrijske revolucije?",
    "Koja vrsta transporta je postala efikasnija tokom Prve industrijske revolucije zahvaljujući parnim mašinama?",
    "Koja industrija je bila prva koja je primenila fabričku proizvodnju tokom Prve industrijske revolucije?",
    "Kako se zvala prva fabrika koja je primenila fabričku proizvodnju tokom Prve industrijske revolucije?"
]

lista_ponudjenih_odgovora = [
    ["George Washington", "John Adams", "Benjamin Franklin", "Thomas Jefferson"],
    ["2. jul 1776.", "4. jul 1776.", "15. jun 1776.", "19. apr 1776."],
    ["Zahtev za nezavisnost od Velike Britanije", "Zahtev za obnovu monarhije", "Kritika kolonijalnog sistema", "Zahtev za povećanje poreza"],
    ["Samo osnivači Sjedinjenih Američkih Država", "Samo članovi Kontinentalnog kongresa", "Samo britanski političari", "Predstavnici trinaest američkih kolonija"],
    ["Pravo na oružje", "Pravo na slobodu govora", "Pravo na život, slobodu i potragu za srećom", "Pravo na brzu sudsku proceduru"],
    ["Gubili su imetak", "Bili su izloženi hapšenju i smrtnoj kazni", "Gubili su građanske slobode", "Gubili su pravo glasa"],
    ["4. jul", "15. jun", "2. jul", "19. apr"],
    ["Dovela je do pomirenja i savezništva", "Dovela je do rata za nezavisnost", "Dovela je do trenutnog povlačenja britanskih trupa", "Nije imala uticaja na odnos"],
    ["John Adams", "George Washington", "Thomas Jefferson", "Benjamin Franklin"],
    ["Usmeravanje trgovinskih sporazuma", "Očuvanje britanske kolonijalne politike", "Služila je kao manifest protiv britanske kolonijalne politike", "Stvaranje unije među kolonijama"],
    ["Poljoprivreda", "Trgovina", "Proizvodnja", "Građevinarstvo"],
    ["Parna lokomotiva", "Parobrod", "Parna mašina", "Električna struja"],
    ["Sjedinjene Američke Države", "Francuska", "Velika Britanija", "Nemačka"],
    ["Poljoprivreda", "Rudarstvo", "Tekstilna industrija", "Građevinarstvo"],
    ["Vodena energija", "Vetar", "Električna energija", "Parna energija"],
    ["Smanjila je broj gradova", "Povećala je broj ruralnih naselja", "Povećala je broj gradova i urbanizaciju", "Nije imala uticaja na urbanizaciju"],
    ["Ručna proizvodnja", "Metoda rašivanja", "Fabrička proizvodnja", "Zanatska proizvodnja"],
    ["Konjske kočije", "Vodeni transport (brodovi)", "Putnički vozovi", "Avioni"],
    ["Tekstilna industrija", "Prehrambena industrija", "Rudarstvo", "Metalurgija"],
    ["Cottonopolis", "Manchester", "Birmingham", "Textilia"]
]


lista_odgovora = [3, 1, 2, 3, 2, 1, 1, 2, 0, 2, 2, 2, 2, 2, 3, 2, 2, 1, 0, 1]

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((55, 95, 145))
pygame.display.set_caption("Ko zna njemu dva")
font = pygame.font.Font(None, 24)
big_font = pygame.font.Font(None, 48)

running = True

square_size = 630
x = 180
y = 100

poeni = 0

lista_indexa = []
lista10 = []

for x1 in range(0, 10):
    broj = random.randint(0, len(lista_pitanja) - 1)
    lista_indexa.append(broj)
    lista10.append(lista_pitanja[broj])

print(len(lista_odgovora))
print(len(lista_pitanja))
print(len(lista_ponudjenih_odgovora))
z = 0
while running:

    if z > 9:
        break

    screen.fill((55, 95, 145))
    text = font.render(lista10[z], True, "black")
    text_rect = text.get_rect(center=(screen.get_width() / 2, y))
    screen.blit(text, text_rect)

    ponuda1 = font.render(lista_ponudjenih_odgovora[lista_indexa[z]][0], True, "black")
    ponuda1_rect = ponuda1.get_rect(center=(150, 200))
    ponuda1_border = ponuda1.get_rect(center=(150, 200))
    ponuda1_border.width += 50
    ponuda1_border.height += 50
    ponuda1_border.top -= 25
    ponuda1_border.left -= 25
    screen.blit(ponuda1, ponuda1_rect)
    pygame.draw.rect(screen, (255, 255, 255), ponuda1_border, 4)

    if z > 9:
        pygame.quit()
        running = False
        break

    ponuda2 = font.render(lista_ponudjenih_odgovora[lista_indexa[z]][1], True, "black")
    ponuda2_rect = ponuda2.get_rect(center=(600, 200))
    ponuda2_border = ponuda2.get_rect(center=(600, 200))
    ponuda2_border.width += 50
    ponuda2_border.height += 50
    ponuda2_border.top -= 25
    ponuda2_border.left -= 25
    screen.blit(ponuda2, ponuda2_rect)
    pygame.draw.rect(screen, (255, 255, 255), ponuda2_border, 4)

    ponuda3 = font.render(lista_ponudjenih_odgovora[lista_indexa[z]][2], True, "black")
    ponuda3_rect = ponuda3.get_rect(center=(150, 400))
    ponuda3_border = ponuda3.get_rect(center=(150, 400))
    ponuda3_border.width += 50
    ponuda3_border.height += 50
    ponuda3_border.top -= 25
    ponuda3_border.left -= 25
    screen.blit(ponuda3, ponuda3_rect)
    pygame.draw.rect(screen, (255, 255, 255), ponuda3_border, 4)

    ponuda4 = font.render(lista_ponudjenih_odgovora[lista_indexa[z]][3], True, "black")
    ponuda4_rect = ponuda4.get_rect(center=(600, 400))
    ponuda4_border = ponuda4.get_rect(center=(600, 400))
    ponuda4_border.width += 50
    ponuda4_border.height += 50
    ponuda4_border.top -= 25
    ponuda4_border.left -= 25
    screen.blit(ponuda4, ponuda4_rect)
    pygame.draw.rect(screen, (255, 255, 255), ponuda4_border, 4)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            if ponuda1_rect.collidepoint(x1, y1):
                z += 1
                if z > 9:
                    pygame.quit()
                    running = False
                    break

                if lista_odgovora[lista_indexa[z - 1]] == 0:
                    pygame.draw.rect(screen, "green", ponuda1_border, 4)
                    print("tacno")
                    poeni += 1

                else:
                    pygame.draw.rect(screen, "red", ponuda1_border, 4)

            elif ponuda2_rect.collidepoint(x1, y1):
                z += 1
                if z > 9:
                    pygame.quit()
                    running = False
                    break

                if lista_odgovora[lista_indexa[z - 1]] == 1:
                    pygame.draw.rect(screen, "green", ponuda2_border, 4)
                    print("tacno")
                    poeni += 1

                else:
                    pygame.draw.rect(screen, "red", ponuda2_border, 4)

            elif ponuda3_rect.collidepoint(x1, y1):
                z += 1
                if z > 9:
                    pygame.quit()
                    running = False
                    break

                if lista_odgovora[lista_indexa[z - 1]] == 2:
                    pygame.draw.rect(screen, "green", ponuda3_border, 4)
                    print("tacno")
                    poeni += 1

                else:
                    pygame.draw.rect(screen, "red", ponuda3_border, 4)

            elif ponuda4_rect.collidepoint(x1, y1):
                z += 1
                if z > 9:
                    pygame.quit()
                    running = False
                    break

                if lista_odgovora[lista_indexa[z - 1]] == 3:
                    pygame.draw.rect(screen, "green", ponuda4_border, 4)
                    print("tacno")
                    poeni += 1

                else:
                    pygame.draw.rect(screen, "red", ponuda4_border, 4)

        tekst_poena = font.render(f"Poeni: {poeni}", True, "black")

        pygame.display.update()

print(poeni)
pygame.quit()



"""
Benjamin Franklin bio je jedan od najvažnijih američkih osnivača, polimat, pisac, izumitelj i diplomata. Rođen je 17. januara 1706. godine u Bostonu, Massachusetts, i preminuo 17. aprila 1790. godine u Filadelfiji, Pennsylvania. Franklin je ostavio dubok trag u mnogim područjima, pa evo nekoliko ključnih informacija o njemu:

Izumitelj: Franklin je poznat po mnogim izumima. Njegovi najpoznatiji izumi su gromobran (poznat i kao Franklinov gromobran) i bifokalne naočare. Takođe je doprineo razvoju različitih tehničkih uređaja i poboljšao efikasnost mnogih svakodnevnih predmeta.

Polimat: Franklin je bio izuzetno obrazovan i interesovao se za različite discipline. Bio je naučnik, pisac, filozof, muzičar i mnogo toga. Njegova radoznalost i rad u mnogim oblastima doprineli su njegovoj reputaciji polimata.

Pisac: Franklin je poznat po svojim spisima i esejima. Njegovo najpoznatije delo je "Autobiografija", u kojoj opisuje svoj život i postignuća. Takođe je bio novinar i vlasnik tiskare i osnovao je časopis "Poor Richard's Almanac", u kojem je objavljivao aforizme i praktične savete.

Diplomata: Franklin je služio kao američki diplomat tokom Američke revolucije. Bio je ključna figura u pregovorima s Francuskom i pomogao je obezbediti francusku podršku američkoj borbi za nezavisnost.

Potpisnik Deklaracije nezavisnosti: Franklin je bio jedan od potpisnika Američke Deklaracije nezavisnosti 1776. godine. Takođe je učestvovao u pisanju Ustava Sjedinjenih Američkih Država.

Filozofija i politika: Franklin je bio poznat po svojim filozofskim i političkim stavovima. Bio je zagovornik vrednosti kao što su sloboda, nezavisnost i građanska prava.

Benjamin Franklin ostaje važna figura u američkoj istoriji i kulturi i smatra se jednim od osnivača nacije. Njegova dela i doprinosi ostavili su dubok i trajan uticaj na mnoga područja života u Sjedinjenim Američkim Državama i širom sveta.
"""

"""
Izraz "polimat" ili "polimatika" označava osobu koja je izuzetno obrazovana ili talentovana u više različitih područja. Polimat je osoba koja ima širok opseg znanja i interesovanja, te često istražuje i stiče duboko razumevanje različitih disciplina, umesto da se specijalizuje u samo jednom polju. Ovaj izraz se često koristi da se opišu ljudi koji su veoma radoznali i strastveni prema učenju i istraživanju, bez obzira na to da li se radi o naučnicima, umetnicima, piscima ili drugim oblastima.

Polimat nije ograničen na samo jedno područje i često može primenjivati znanje i veštine iz jednog polja na drugo, što može dovesti do inovacija i kreativnih rešenja. Polimatika se ceni zbog sposobnosti povezivanja različitih disciplina i donošenja novih perspektiva i ideja u različita područja.

Primeri istorijskih polimata uključuju ljude kao što su Leonardo da Vinci, Benjamin Franklin i Gottfried Wilhelm Leibniz, koji su bili poznati po svojim širokim intelektualnim interesovanjima i doprinosima u različitim oblastima.
"""

"""
Benjamin Franklin nije otkrio elektricitet, ali je napravio značajne doprinose razumevanju i proučavanju elektriciteta. Njegovi eksperimenti s elektricitetom bili su ključni za razvoj ranog razumevanja ovog fenomena. Evo nekoliko važnih aspekata njegovih doprinosa elektricitetu:

Pojam pozitivnog i negativnog naboja: Franklin je uveo koncepte pozitivnog i negativnog naboja kako bi opisao kako elektricitet funkcioniše. On je pretpostavio da elektricitet dolazi u dvije suprotno nabijene vrste, i to je kasnije postalo osnova za razumevanje električnih polja.

Eksperiment s zmijom elektriciteta: Najpoznatiji eksperiment koji je Franklin izveo bio je eksperiment s zmijom elektriciteta. Koristio je zmijoliku staklenu cijev (tzv. Leydenova boca) kako bi sakupljao električni naboja. Ovaj eksperiment pomogao je u shvatanju kako se električni naboj može skladištiti i oslobađati.

Gromobran: Franklin je također poznat po izumu gromobrana, koji je temeljen na njegovom razumevanju elektriciteta. Gromobran je dizajniran da štiti zgrade od udara groma, usmjeravajući električnu energiju sigurno prema zemlji.

Teorija elektriciteta: Franklin je razvio teoriju o elektricitetu koja je u to vrijeme bila revolucionarna. Iako su njegovi koncepti pozitivnog i negativnog naboja kasnije revidirani, njegovi radovi bili su ključni za razvoj moderne teorije elektriciteta.

Iako nije otkrio elektricitet kao takav, Benjamin Franklin je svojim eksperimentima i konceptima značajno doprinio razumevanju ovog prirodnog fenomena. Njegovi radovi bili su preteča razvoja moderne elektrofizike i elektrotehnike.
"""
