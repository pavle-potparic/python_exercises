import pygame
import random

lista_pitanja = ["Koji je najveći kontinent na svetu po površini?",
                 "Koji je najveći satelit Saturna?", "Koja je najveća ptica na svetu i ne leti?",
                 "Koji vitamini se često nazivaju sunčevi vitamini jer se proizvode u koži kada je izložena sunčevoj svetlosti?"
                 "Koji grad je poznat kao Grad stotinu tornjeva i smešten je u Italiji?",
                 "Koja je najveća žlezda u ljudskom telu i igra ključnu ulogu u regulisanju šećera u krvi?",
                 "Koji praznik se često obeležava bojenjem jaja i organizovanjem potrage za skrivenim slatkišima?",
                 "Koji element se koristi za označavanje hemoglobina u ljudskoj krvi?",
                 "Koja ptica je simbol Amerike i poznata po svom oštroumnom vidu?",
                 "Koja naučna oblast proučava poreklo, evoluciju i budućnost svemira?"
                 ]

lista_ponudjenih_odgovora = [["Evropa", "Severna Amerika", "Azija", "Afrika"],
                             ["Titan", "Phobos", "Ganymede", "Enceladus"],
                             ["Labud", "Emu", "Pingvin", "Orao"],
                             ["Vitamin A i C", "Vitamin B i D", "Vitamin E i K", "Vitamin F i G"],
                             ["Venecija", "Rim", "Piza", "Firenca"],
                             ["Jetra", "Pankreas", "Bubrezi", "Želudac"],
                             ["Božić", "Uskrs", "Noć veštica (Halloween)", "Dan zahvalnosti"],
                             ["Kiseonik", "Gvožđe", "Bakar", "Ugljenik"],
                             ["Jastreb", "Sova", "Orao", "Pelikan"],
                             ["Astronomija", "Biologija", "Geografija", "Psihologija"]]

lista_odgovora = [2, 0, 1, 1, 2, 1, 1, 1, 2,0]

lista_pitanja += [
    "Koji element je poznat kao 'Kraljica metala' i koristi se u izradi nakita?",
    "Koje godine je počeo Prvi svetski rat?",
    "Koje godine je osnovana Ujedinjene nacije (UN)?",
    "Koji element se nalazi u većini minerala i čini osnovni sastojak stena?",
    "Koji kontinent se često naziva 'Kontinentom budućnosti' zbog svoje velike geološke aktivnosti?",
    "Koja biljka je poznata po svojim listovima u obliku srca i često se vezuje za Dan zaljubljenih?",
    "Koji je najveći organ u ljudskom telu?",
    "Koja planeta je poznata kao 'Crvena planeta' zbog svoje crvenkaste površine?",
    "Koja ptica je poznata po svojim dugim nogama i vratu, te karakterističnom 'trubičastom' zvuku?",
    "Koji hemijski element ima simbol 'C' i čini osnovni sastojak organskih jedinjenja?"
]

lista_ponudjenih_odgovora += [
    ["Srebro", "Zlato", "Platina", "Bakar"],
    ["1905", "1914", "1919", "1939"],
    ["1945", "1950", "1960", "1975"],
    ["Gvožđe", "Bakar", "Srebro", "Zlato"],
    ["Australija", "Evropa", "Azija", "Antarktik"],
    ["Ruža", "Ljiljan", "Kaktus", "Kopriva"],
    ["Srce", "Jetra", "Pluća", "Mozak"],
    ["Mars"],
    ["Flamingo"],
    ["Ugljenik"]
]

lista_odgovora += [
    1, 1, 0, 0, 0, 0, 1, 2, 1, 1
]

lista_pitanja += [
    "Koji je najveći svetski okean?",
    "Koji gas je najzastupljeniji u vazduhu?",
    "Koja životinja je poznata po svojim karakterističnim crnim i belim prugama i dolazi iz Afrike?",
    "Koja reka je poznata kao 'Plavi Nil' i ima ključnu ulogu u vodosnabdevanju Egipta?",
    "Koje godine je čovek prvi put hodao na Mesecu?",
    "Koji je najmanji okean na svetu?",
    "Koji grad je poznat kao 'Grad brda' i ima znamenit toranj zvan 'Toranj tvrđave'?",
    "Koji je najveći mesec Plutona?",
    "Koji element je često korišćen u fluorescentnim sijalicama i ima simbol 'Pb'?",
    "Koja ptica je poznata po svojoj sposobnosti da leti unazad?"
]

lista_ponudjenih_odgovora += [
    ["Tihi okean", "Atlantski okean", "Indijski okean", "Severni ledoviti okean"],
    ["Kiseonik", "Azot", "Vodonik", "Helijum"],
    ["Zebra", "Tigrova", "Lav", "Slon"],
    ["Nil", "Jordan", "Misisipi", "Jangce"],
    ["1969", "1975", "1981", "1992"],
    ["Južni okean", "Atlantski okean", "Indijski okean", "Severni ledoviti okean"],
    ["Firenca", "San Francisko", "Pariz", "Njujork"],
    ["Charon", "Enceladus", "Titan", "Ganymede"],
    ["Olovo", "Bakar", "Srebro", "Zlato"],
    ["Kolibri", "Orao", "Golub", "Jastreb"]
]

lista_odgovora += [
    0, 1, 0, 0, 0, 3, 2, 2, 2, 0
]

lista_pitanja += [
    "Koji kontinent se često naziva 'Kontinentom leda' zbog svoje velike površine prekrivene ledom?",
    "Koja planetarna pojava uzrokuje tamne oblike na površini Sunca kada se jedan astronomski objekat preklapa drugim?",
    "Koji ocean se nalazi između Evrope i Severne Amerike?",
    "Koja je najveća žlezda u ljudskom telu i igra ključnu ulogu u metabolizmu?",
    "Koji praznik se obeležava 31. oktobra i često uključuje oblačenje u kostime i traženje slatkiša?",
    "Koje godine je pao Berlinski zid?",
    "Koja reka teče kroz Kairo i ima veliki istorijski značaj za Egipat?",
    "Koje godine je potpisana Američka deklaracija nezavisnosti?",
    "Koji je najmanji planet Sunčevog sistema?",
    "Koja ptica je poznata po svom karakterističnom 'kukuriku' zvuku ujutro?"
]

lista_ponudjenih_odgovora += [
    ["Severna Amerika", "Evropa", "Australija", "Antarktik"],
    ["Solarni vetar", "Solarni maksimum", "Solarni minimum", "Solarni mrak (eclipse)"],
    ["Tihi okean", "Indijski okean", "Atlantski okean", "Severni ledoviti okean"],
    ["Jetra", "Pankreas", "Štitna žlezda", "Pluća"],
    ["Uskrs", "Božić", "Noć veštica (Halloween)", "Dan zahvalnosti"],
    ["1989", "1991", "1993", "1985"],
    ["Nil", "Jordan", "Tigra", "Eufrat"],
    ["1776", "1789", "1812", "1865"],
    ["Merkur", "Venera", "Mars", "Neptun"],
    ["Kokoska", "Galeb", "Noj", "Petao"]
]

lista_odgovora += [
    3, 3, 2, 0, 2, 0, 0, 0, 0, 3
]

lista_pitanja += [
    "Koji element se često naziva 'Krvavo crveni metal' i koristi se za proizvodnju bakarnih legura?",
    "Koja boja se dobija mešanjem plave i žute boje?",
    "Koji je najveći mesec u Sunčevom sistemu?",
    "Kako se zove proces kada gas prelazi direktno u čvrsto stanje bez prolaska kroz tečno stanje?",
    "Koja naučna oblast se bavi proučavanjem organizama i njihovih okruženja?",
    "Koje godine je doneta Univerzalna deklaracija o ljudskim pravima?",
    "Koji je najveći broj koji se može zapisati koristeći rimsku numeraciju?",
    "Koji planet se ponekad naziva 'Zemljin blizanac' zbog sličnosti u veličini i strukturi?",
    "Koji kontinent se često naziva 'Starim kontinentom' zbog svoje dugotrajne geološke istorije?",
    "Koja biljka je poznata po svojim velikim listovima i karakterističnom obliku pera?"
]

lista_ponudjenih_odgovora += [
    ["Bakar", "Aluminijum", "Željezo", "Titanijum"],
    ["Zelena", "Ljubičasta", "Narandžasta", "Roza"],
    ["Titan", "Mimas", "Ganymede", "Phobos"],
    ["Sublimacija", "Kondenzacija", "Kapanje", "Kristalizacija"],
    ["Astronomija", "Biologija", "Geografija", "Fizika"],
    ["1945", "1948", "1955", "1960"],
    ["M", "C", "D", "L"],
    ["Merkur", "Venera", "Mars", "Jupiter"],
    ["Azija", "Afrika", "Australija", "Južna Amerika"],
    ["Palm", "Kaktus", "Bananin list", "Paprat"]
]

lista_odgovora += [
    0, 0, 2, 0, 1, 1, 0, 1, 1, 3
]

lista_pitanja += [
    "Koji element se naziva 'Hemijski patuljak' jer je najlakši stabilni element?",
    "Koja planeta se često naziva 'Crveni planet' zbog boje njene površine?",
    "Koja supstanca je poznata kao 'Provitamin A' i važna je za očuvanje vida?",
    "Koja životinja je poznata kao 'Pustinjski brod' zbog svoje sposobnosti skladištenja vode?",
    "Koja drevna građevina visoka iza 138 metara se nalazi u Egiptu?",
    "Koji hemijski element je najrasprostranjeniji metal na Zemlji?",
    "Koja ptica je najveća i najteža ptica na svetu?",
    "Koja planetarna pojava nastaje kada Mesec potpuno prekrije Sunce?",
    "Koja planeta je poznata po svojim prstenovima?",
    "Koji gas je odgovoran za zelenkasto plavu boju Zemljine atmosfere?"
]

lista_ponudjenih_odgovora += [
    ["Vodonik", "Helijum", "Litijum", "Kiseonik"],
    ["Mars", "Venera", "Merkur", "Saturn"],
    ["Beta-karoten", "Cink", "Kalcijum", "Vitamin C"],
    ["Kamel", "Kondor", "Guanako", "Dromedar"],
    ["Piramide", "Hramovi", "Sfinga", "Obelisk"],
    ["Gvožđe", "Aluminijum", "Kalijum", "Natrijum"],
    ["Australski noj", "Emu", "Ostrich", "Kasuari"],
    ["Pomračenje Sunca", "Mesečev ciklus", "Solarni vetar", "Komet"],
    ["Mars", "Venera", "Saturn", "Neptun"],
    ["Kiseonik", "Azot", "Helijum", "Ugljen-dioksid"]
]

lista_odgovora += [
    1, 0, 0, 3, 0, 3, 2, 0, 2, 1
]

lista_pitanja += [
    "Koje godine je počeo Drugi svetski rat?",
    "Koji hemijski element ima simbol 'Hg'?",
    "Koji časovnik pokazuje vreme pomoću svetla koje prolazi kroz uske proreze i stvara senku na brojevima?",
    "Koji je najveći organ u ljudskom telu po površini?",
    "Kako se zove proces kada tečnost prelazi u čvrsto stanje pri nižoj temperaturi od tačke zamrzavanja?",
    "Koja ptica je simbol mudrosti u mnogim kulturama?",
    "Koji je najveći kontinent na Zemlji?",
    "Koja je najduža reka u Severnoj Americi?",
    "Koji je najmanji planet Sunčevog sistema?",
    "Koja životinja je poznata po svojoj crno-beloj šari i sposobnosti da se penje po drveću?"
]

lista_ponudjenih_odgovora += [
    ["1914", "1939", "1945", "1950"],
    ["Hidrogen", "Helijum", "Srebro", "Živa"],
    ["Peskovnik", "Digitalni časovnik", "Sunčani časovnik", "Analogni časovnik"],
    ["Jetra", "Koža", "Mozak", "Pluća"],
    ["Isparavanje", "Kondenzacija", "Sublimacija", "Zaleđivanje"],
    ["Sokol", "Sova", "Jastreb", "Pelikan"],
    ["Severna Amerika", "Južna Amerika", "Afrika", "Azija"],
    ["Misisipi", "Sveti Lorenco", "Kolorado", "Jukon"],
    ["Venera", "Merkur", "Mars", "Neptun"],
    ["Medved", "Leopard", "Panda", "Tigrova"]
]

lista_odgovora += [
    1, 3, 2, 1, 3, 1, 3, 0, 1, 2
]

lista_pitanja += [
    "Koji planet se ponekad naziva 'Crvena planeta' zbog svoje očigledne crvene boje?",
    "Koja reka je najduža na svetu?",
    "Kako se zove proces kada tečnost prelazi u gasno stanje pri nižoj temperaturi od tačke ključanja?",
    "Koja planeta se često naziva 'Plavi dragulj' zbog svog plavog izgleda iz svemira?",
    "Ko je autor romana 'Ponos i predrasude'?",
    "Koja planeta je poznata po svojim karakterističnim prugama i velikom tamnom mestu koje se naziva 'Veliki crveni oblak'?",
    "Koji kontinent se ponekad naziva 'Crni kontinent' zbog svoje bogate istorije i resursa?",
    "Koja naučnica je prva dobila Nobelovu nagradu u dve različite naučne oblasti: fizici i hemiji?",
    "Koji grad se često naziva 'Grad svetlosti' i poznat je po Ajfelovom tornju?",
    "Koje godine je prvi čovek hodao na Mesecu?"
]

lista_ponudjenih_odgovora += [
    ["Venera", "Mars", "Jupiter", "Saturn"],
    ["Nil", "Amazonka", "Misisipi", "Jangce"],
    ["Sublimacija", "Kondenzacija", "Isparavanje", "Taljenje"],
    ["Mars", "Zemlja", "Neptun", "Venera"],
    ["Džordž Orvel", "Džejn Ostin", "Čarls Dikens", "Tomas Hardi"],
    ["Saturn", "Uran", "Neptun", "Jupiter"],
    ["Afrika", "Australija", "Azija", "Evropa"],
    ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Irene Joliot-Curie"],
    ["Rim", "Pariz", "London", "Njujork"],
    ["1969", "1975", "1981", "1992"]
]

lista_odgovora += [
    1, 0, 2, 1, 1, 3, 0, 0, 1, 0
]


lista_pitanja += [
    "Koja planeta je poznata kao 'Jutarnja zvezda' i 'Večernja zvezda' zbog svog sjaja u ranim jutarnjim i večernjim satima?",
    "Koji osnovni gas čini najveći deo Zemljine atmosfere?",
    "Kako se zove proces kada biljke koriste sunčevu svetlost da pretvore vodu i ugljen-dioksid u hranljive materije?",
    "Koji je glavni grad Australije?",
    "Koje godine je počeo Prvi svetski rat?",
    "Koja od sledećih knjiga je napisana od strane Vilijama Šekspira?",
    "Koji je najveći sisavac na svetu?",
    "Koji kontinent je domaćin Svetskog prvenstva u fudbalu 2022. godine?",
    "Kako se zove najveća planina u Severnoj Americi?",
    "Koji gas čini oko 78% Zemljine atmosfere?"
]

lista_ponudjenih_odgovora += [
    ["Mars", "Venera", "Merkur", "Neptun"],
    ["Kiseonik", "Azot", "Vodonik", "Helijum"],
    ["Fotosinteza", "Disanje", "Digestija", "Transpiracija"],
    ["Melburn", "Sidnej", "Brisbejn", "Kanbera"],
    ["1905", "1914", "1919", "1939"],
    ["'Romeo i Julija'", "'Veličanstveni Gatsby'", "'Sto godina samoće'", "'Rat i mir'"],
    ["Slon", "Kit", "Nosorog", "Medved"],
    ["Evropa", "Afrika", "Azija", "Severna Amerika"],
    ["Mont Everest", "Kilimandžaro", "Denali (McKinley)", "Mont Blanc"],
    ["Kiseonik", "Azot", "Vodonik", "Helijum"]
]

lista_odgovora.append([1, 1, 0, 3, 1, 0, 1, 2, 2, 1])

lista_pitanja += [
    "Koji je najveći planet Sunčevog sistema?",
    "Koja reka protiče kroz Pariz?",
    "Koja boja se dobija mešanjem plave i crvene boje?",
    "Koji hemijski element ima simbol 'Fe'?",
    "Koja ptica je poznata po svojoj sposobnosti da ponavlja ljudski govor?",
    "Koji kontinent je domaćin Letnjih olimpijskih igara 2020. godine?",
    "Koji planet je poznat po svojim karakterističnim prstenovima?",
    "Koji naučnik je razvio teoriju relativnosti?",
    "Koji je najveći organ u ljudskom telu?",
    "Koji je najviši planinski vrh na svetu?"
]

lista_ponudjenih_odgovora += [
    ["Mars", "Venera", "Jupiter", "Saturn"],
    ["Temza", "Dunav", "Sava", "Sena"],
    ["Zelena", "Žuta", "Narandžasta", "Roza"],
    ["Kiseonik", "Gvožđe", "Aluminijum", "Bakar"],
    ["Sokol", "Vrabac", "Papagaj", "Golub"],
    ["Evropa", "Azija", "Severna Amerika", "Afrika"],
    ["Mars", "Jupiter", "Saturn", "Uran"],
    ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Marie Curie"],
    ["Srce", "Jetra", "Pluća", "Mozak"],
    ["Mont Everest", "Kilimandžaro", "Anapurna", "Andi"]
]

lista_odgovora.append([2, 3, 2, 1, 2, 1, 2, 1, 1, 0])

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((55, 95, 145))
pygame.display.set_caption("Ko zna njemu dva")
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 48)

running = True

square_size = 630
x = 180
y = -250

lista_indexa = []
lista10 = []

for x in range(0, 10):
    broj = random.randint(0, len(lista_pitanja)-1)
    lista_indexa.append(broj)
    lista10.append(lista_pitanja[broj])

pygame.time.set_timer(pygame.USEREVENT + 1, 2000)

z = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.event.get(pygame.USEREVENT + 1):
        z += 1
        print("ok menjam")
        pygame.time.set_timer(pygame.USEREVENT + 1, 2000)

    if z > 9:
        break

    screen.fill((55, 95, 145))
    text = font.render(lista10[z], True, "black")
    text_rect = text.get_rect(center=(x + square_size / 2, y + square_size / 2))
    screen.blit(text, text_rect)

    ponuda1 = font.render(lista_ponudjenih_odgovora[lista_indexa[z]][0], True, "black")
    ponuda1_rect = ponuda1.get_rect(center=(150, 200))
    screen.blit(ponuda1, ponuda1_rect)

    ponuda2 = font.render(lista_ponudjenih_odgovora[lista_indexa[z]][1], True, "black")
    ponuda2_rect = ponuda2.get_rect(center=(600, 200))
    screen.blit(ponuda2, ponuda2_rect)

    ponuda3 = font.render(lista_ponudjenih_odgovora[lista_indexa[z]][2], True, "black")
    ponuda3_rect = ponuda3.get_rect(center=(150, 400))
    screen.blit(ponuda3, ponuda3_rect)

    ponuda4 = font.render(lista_ponudjenih_odgovora[lista_indexa[z]][3], True, "black")
    ponuda4_rect = ponuda4.get_rect(center=(600, 400))
    screen.blit(ponuda4, ponuda4_rect)
        # print(lista10[z])

    pygame.display.update()

pygame.quit()