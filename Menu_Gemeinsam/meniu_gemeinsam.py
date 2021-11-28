from Entities.guest import Guest
from Entities.reservierung import Reservierung
from fct_input import *

def meniu_gemeinsam(hotel):
    while True:                                                                       # meniu activ mereu -> arata optiunile
        print('------------------------------------------------------------------')
        print('1. Mach eine Reservierung:')
        print('2. Anzeige die Liste von Gästen,die aktuelle Reservierungen haben')
        print('3. Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien')
        print('4. Anzeige alle Zimmer, die heute frei sind')
        print('5. Go back')
        print('------------------------------------------------------------------')
        rez = int(input('Wählen Sie eine Nummer: '))

        if rez == 1:
            opt_mach_reservierung(hotel)
        elif rez == 2:
            now = input_now()
            opt_anzeige_guest_aktiv(hotel, now)
        elif rez == 3:
            criteriu = input_criteriu()
            opt_anzeige_zimmer_gefiltert(hotel, criteriu)
        elif rez == 4:
            now = input_now()
            opt_anzeige_zimmer_frei(hotel, now)
        elif rez == 5:
            print("Going back...")
            break


def opt_anzeige_zimmer_frei(hotel, now):              #afiseaza camerele libere dintr-o anumita data
    now_converted = convert_data_nr(now)              #se foloseste data ca nr int
    liste_zimmern = hotel.zimmern

    for zimmer in liste_zimmern:
        if zimmer.status[now_converted] == 0:
            print(zimmer)


def opt_anzeige_guest_aktiv(hotel, now):               #afiseaza lista de persoane care au rezervare intr-o anumita data + ce rezervare are
    now_converted = convert_data_nr(now)               #se foloseste data ca nr int
    lista_reservierungen = hotel.reservierungen
    lista_guests_activi = []

    for reservierung in lista_reservierungen:
        if now_converted >= reservierung.start_date and now_converted <= reservierung.end_date:
            lista_guests_activi.append(reservierung.guest)
            print(lista_guests_activi)


def opt_mach_reservierung(hotel):                                                              #faceti o rezervare
    vorname = input('Fügen Sie Euren Vorname ein: ')
    nachname = input('Fügen Sie Euren Name ein: ')
    serie_nr_buletin = input('Fügen Sie die Daten Eures Personalausweises ein: ')
    anzahl_gueste = int(input('Für wie viele Personen wollen Sie die Reservierung machen? '))
    mehrblick = input('Wollen Sie Mehrblick? JA/NEIN: ')
    start_date = input('Die erste Tag der Reservierung: ')
    end_date = input('Die letzte Tag der Reservierung: ')

    start_date_convertit = convert_data_nr(start_date)                                         # convertim stringul in nr
    end_date_convertit = convert_data_nr(end_date)

    liste_guests = hotel.guests[:]
    liste_zimmer = hotel.zimmern[:]
    guest = Guest(vorname, nachname, serie_nr_buletin)
    reservierung = Reservierung(guest, start_date_convertit, end_date_convertit)
    gute_zimmer = []

    for z in range(0, len(liste_zimmer)):
        zimmer = liste_zimmer[z]
        if anzahl_gueste <= liste_zimmer[z].anzahl_g and mehrblick == liste_zimmer[z].mehrblick and verificare_status(liste_zimmer[z], start_date_convertit, end_date_convertit) == 0:
            gute_zimmer.append(liste_zimmer[z])                                               #camerele vor fi afisate de la 1 la n
            print(zimmer)

    if len(gute_zimmer) == 0:
        print("Keine freie Zimmer für die ausgewählten Kriterien")
        meniu_gemeinsam(hotel)

    pers_gasita = 0
    for g in range(0, len(liste_guests)):
        if liste_guests[g] == guest:
            pers_gasita = 1
            alege_si_adauga_rezervare(liste_zimmer, hotel, guest, reservierung)

    if pers_gasita == 0:                                                                      #persoana se adauga la lista oaspetilor
        liste_guests.append(guest)
        alege_si_adauga_rezervare(liste_zimmer, hotel, guest, reservierung)


def alege_si_adauga_rezervare(liste_zimmer, hotel, guest, reservierung):                     #alege o camera pt rezervare
    zimmerSelectat = input('Wählen Sie eine Zimmer: ')                                       #se alege nr camerei, afisat pe ecran

    for z in range(0, len(liste_zimmer)):
        if liste_zimmer[z].nr_zimmer == zimmerSelectat:
            reservierung.zimmer = liste_zimmer[z]
            hotel.zimmern[z].set_status(reservierung.start_date, reservierung.end_date)      #modificam statusul camerei in lista cu toate camerele de la hotel
            print("*")  # MERGE!!!
            hotel.add_reservierungen(reservierung)
            guest.add_reservierung(reservierung)


def convert_data_nr(data):                                        #convertim data din str in int
    an= 0
    ziua = 0
    luna = 0
    sum = 0
    # data: "20/12/2021"

    for i in range(0, len(data)):                                 #obtinem ziua, luna, anul
        if i == 0:
            ziua = int(data[i]) * 10 + int(data[i + 1])
        elif i == 3:
            luna = int(data[i]) * 10 + int(data[i + 1])
        elif i == 6:
            an = int(data[i]) * 1000 + int(data[i + 1]) * 100 + int(data[i + 2]) * 10 + int(data[i + 3])

    if an % 4 == 1:                                               #verificam dupa an
        sum = ziua                                               #sum = numarul zilei cautate in vectorul de zile ale anului
        lista_zile_an = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for l in range(0, luna-1):
            sum = sum + lista_zile_an[l]
    elif an % 4 == 2:
        sum = 365 + ziua
        lista_zile_an = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for l in range(0, luna-1):
            sum = sum + lista_zile_an[l]
    elif an % 4 == 3:
        sum = 730 + ziua
        lista_zile_an = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for l in range(0, luna-1):
            sum = sum + lista_zile_an[l]
    elif an % 4 == 0:
        sum = 1095 + ziua
        lista_zile_an = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for l in range(0, luna-1):
            sum = sum + lista_zile_an[l]
    return sum


def verificare_status(zimmer, start_date, end_date):                      #verificare daca intreaga perioada dorita e libera
    libera = 0
    lista_status = zimmer.status

    for s in range(start_date, end_date):
        if lista_status[s] == 1:
            libera = 1
            break
    if libera == 0:
        return 0
    else:
        return 1


def opt_anzeige_zimmer_gefiltert(hotel, criteriu):                                                   #optiuni de filtrare dupa pret si vedere la mare
    liste_zimmer = hotel.zimmern[:]                                   #verificare optiuni dorite

    crt = input_filter_zimmer(criteriu)
    for z in range(0, len(liste_zimmer)):
        zimmer = liste_zimmer[z]
        if criteriu == 1:
            if less_than_price(zimmer.preis,crt[0]) == 1:
                print(zimmer)
        elif criteriu == 2:
            if more_than_price(zimmer.preis, crt[0]) == 1:
                print(zimmer)
        elif criteriu == 3:
            if intre_preturi(zimmer.preis, crt[0], crt[1]) == 1:  #poz 0 -> pret_maxim, poz 1 --> pret_minim (fct_input)
                print(zimmer)
        elif criteriu == 4:
            if mehrblick(zimmer.mehrblick, crt[0]) == 1:
                print(zimmer)
        elif criteriu == 5:
            if less_than_price(zimmer.preis,crt[0]) == 1 and mehrblick(zimmer.mehrblick, crt[1]) == 1: #poz 0 -> pret_maxim, poz 1 --> preferinta (fct_input)
                print(zimmer)
        elif criteriu == 6:
            if more_than_price(zimmer.preis,crt[0]) == 1 and mehrblick(zimmer.mehrblick, crt[1]) == 1: #poz 0 -> pret_minim, poz 1 --> preferinta (fct_input)
                print(zimmer)
        elif criteriu == 7:
            if intre_preturi(zimmer.preis,crt[0], crt[1]) == 1 and mehrblick(zimmer.mehrblick, crt[2]) ==1: #poz 0 -> pret_maxim, poz 1 -> pret_minim, poz 2 --> preferinta (fct_input)
                print(zimmer)


def less_than_price(x,pret_maxim):                                          #functii de ajutor pentru comparare preturi + vedere mare
    return x <= pret_maxim


def more_than_price(x, pret_minim):
    return x >= pret_minim


def intre_preturi(x, pret_maxim, pret_minim):
    return less_than_price(x,pret_maxim) and more_than_price(x, pret_minim)


def mehrblick(x, preferinta):
    return x == preferinta