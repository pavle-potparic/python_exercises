import tkinter
import time
from tkinter import messagebox

sirina_terena = 750
visina_terena = 500
prozor = tkinter.Tk()
teren = tkinter.Canvas(prozor, width=sirina_terena, height=visina_terena, bg='dodgerblue4')
teren.pack()

palica = teren.create_rectangle(0, 0, 40, 10, fill='dark turquoise')
lopta = teren.create_oval(0, 0, 10, 10, fill='deep pink')
x_osa_od_kocke = 150
y_osa_od_kocke = 100
pocetna_x_pozicija = 0
pocetna_y_pozicija = 0
kocka_za_dodatne_poene = teren.create_rectangle(x_osa_od_kocke, y_osa_od_kocke, pocetna_x_pozicija, pocetna_y_pozicija,
                                                fill='green')

rezultat = 0
broj_udaraca = 0

prozor_otvoren = True
x_osa_gore_desno = -115
y_osa_gore_desno = 174
y_osa_dole_desno = 94
x_osa_dole_levo = -235

# TODO napravi x-115 y 174, y 94 x-235


def glavna_petlja():
    global rezultat
    while prozor_otvoren:
        pomeri_palicu()
        pomeri_loptu()
        prozor.update()
        time.sleep(0.02)
        if prozor_otvoren:
            kraj_igre()


leva_pritisnuta = 0
desna_pritisnuta = 0


def taster_pritisnut(event):
    global leva_pritisnuta, desna_pritisnuta
    if event.keysym == 'Left':
        leva_pritisnuta = 1
    elif event.keysym == 'Right':
        desna_pritisnuta = 1


def taster_oslobodjen(event):
    global leva_pritisnuta, desna_pritisnuta
    if event.keysym == 'Left':
        leva_pritisnuta = 0
    elif event.keysym == 'Right':
        desna_pritisnuta = 0


brzina_palice = 6


def pomeri_palicu():
    palica_pomeraj = brzina_palice * desna_pritisnuta - brzina_palice * leva_pritisnuta
    (palica_levo, palica_gore, palica_desno, palica_dole) = teren.coords(palica)
    if palica_levo > 0 or palica_pomeraj > 0 and palica_desno < sirina_terena or palica_pomeraj < 0:
        teren.move(palica, palica_pomeraj, 0)


lopta_pomeraj_x = 4
lopta_pomeraj_y = -4
postavi_palica_gore = visina_terena - 40
postavi_palica_dole = visina_terena - 30
da_li_dodiruje_kocku = 0


def pomeri_loptu():
    global x_osa_gore_desno, y_osa_gore_desno, y_osa_dole_desno, x_osa_dole_levo
    global lopta_pomeraj_x, lopta_pomeraj_y, rezultat, broj_udaraca, brzina_palice
    lopta_levo, lopta_gore, lopta_desno, lopta_dole = teren.coords(lopta)
    if x_osa_gore_desno > lopta_pomeraj_x and y_osa_gore_desno > lopta_pomeraj_y and x_osa_dole_levo < lopta_pomeraj_x and lopta_pomeraj_y > y_osa_dole_desno:
        rezultat = rezultat + 1
        lopta_pomeraj_y += 1
    if lopta_pomeraj_x > 0 and lopta_desno > sirina_terena:
        lopta_pomeraj_x = -lopta_pomeraj_x
    if lopta_pomeraj_x < 0 and lopta_levo < 0:
        lopta_pomeraj_x = -lopta_pomeraj_x
    if lopta_pomeraj_y < 0 and lopta_gore < 0:
        lopta_pomeraj_y = -lopta_pomeraj_y
    if lopta_pomeraj_y > 0 and lopta_dole > postavi_palica_gore and lopta_dole < postavi_palica_dole:
        palica_levo, palica_gore, palica_desno, palica_dole = teren.coords(palica)
        if lopta_pomeraj_x > 0 and lopta_desno + lopta_pomeraj_x > palica_levo and lopta_levo < palica_desno or lopta_pomeraj_x < 0 and lopta_desno > palica_levo and lopta_levo + lopta_pomeraj_x < palica_desno:
            lopta_pomeraj_y = -lopta_pomeraj_y
            rezultat = rezultat + 1
            broj_udaraca = broj_udaraca + 1
            if broj_udaraca == 4:
                broj_udaraca = 0
                brzina_palice = brzina_palice + 1
                if lopta_pomeraj_x > 0:
                    lopta_pomeraj_x = lopta_pomeraj_x + 1
                else:
                    lopta_pomeraj_x = lopta_pomeraj_x - 1
                lopta_pomeraj_y = lopta_pomeraj_y - 1
    teren.move(lopta, lopta_pomeraj_x, lopta_pomeraj_y)
    return lopta_dole


def kraj_igre():
    lopta_levo, lopta_gore, lopta_desno, lopta_dole = teren.coords(lopta)
    if lopta_gore > visina_terena:
        print('Vas rezultat je', rezultat)
        igraj_ponovo = tkinter.messagebox.askyesno(message='Da li zelite da igrate ponovo? ')
        if igraj_ponovo:
            nova_igra()
        else:
            zatvori()


def zatvori():
    global prozor_otvoren
    prozor_otvoren = False
    prozor.destroy()


def nova_igra():
    global rezultat, broj_udaraca, brzina_palice
    global leva_pritisnuta, desna_pritisnuta
    global lopta_pomeraj_x, lopta_pomeraj_y
    leva_pritisnuta = 0
    desna_pritisnuta = 0
    lopta_pomeraj_x = 4
    lopta_pomeraj_y = -4
    teren.coords(palica, 10, postavi_palica_gore, 50, postavi_palica_dole)
    teren.coords(lopta, 20, postavi_palica_gore - 10, 30, postavi_palica_gore)
    rezultat = 0
    broj_udaraca = 0
    brzina_palice = 6


prozor.protocol('WM_DELETE_WINDOW', zatvori)
prozor.bind('<KeyPress>', taster_pritisnut)
prozor.bind('<KeyRelease>', taster_oslobodjen)

nova_igra()
glavna_petlja()
