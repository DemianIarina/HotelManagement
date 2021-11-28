from Entities.guest import Guest
from Entities.zimmer import Zimmer

#meniu guests
def input_opt_add_g():                                                            #adauga persoana
    vorname = input('Fügen Sie Euren Name ein: ')                                     #nu apelam functia direct cu parametrii de guest, pt a putea fi console anvendung
    nachname = input('Fügen Sie Euren Vorname ein: ')
    serie_nr_buletin = input('Fügen Sie die Daten Eures Personalausweises ein: ')
    neu_guest = Guest(vorname, nachname, serie_nr_buletin)
    return neu_guest

def input_serie_nr_buletin():                                                 #cautare dupa seria si nr din buletin -> actualizare nume de familie
    serie_nr_buletin_cautat = input('Fügen Sie die Daten Eures Personalausweises ein: ')
    return serie_nr_buletin_cautat

def input_opt_akt_nachname():
    new_nachname = input ('Neuer Nachame: ')
    return new_nachname



#meniu zimmer
def input_opt_add_z():
    nr_zimmer = input('Fügen Sie die Kameranummer ein: ')
    anzahl_guests = input('Fügen Sie die Kapazität der Kamera ein: ')
    preis = input('Fügen Sie den Preis der Kamera ein: ')
    farbe = input('Fügen Sie die Farbe der Kamera ein: ')
    mehrblick = input('Mehrblick: ')
    neu_zimmer = Zimmer(nr_zimmer, anzahl_guests, preis, farbe, mehrblick)
    return neu_zimmer

def input_nr_camera():
    nr_zimmer_cautat = input('Fügen Sie die Nummer des Zimmers ein: ')
    return nr_zimmer_cautat

def input_opt_akt_preis():
    neues_preis = input('Der neue Preis für dieses Zimmer ist: ')
    return neues_preis


#meniu gemeinsam


def input_now():
    now = input('Heutige Datum: ')

def input_criteriu():
    print('----------------------------------------------------------------------------')
    print('1. Filter Zimmer nach maximales Preis: ')
    print('2. Filter Zimmer nach minimales Preis: ')
    print('3. Filter Zimmer nach maximales und minimales Preis: ')
    print('4. Filter Zimmer nach Mehrblick Kriterium: ')
    print('5. Filter Zimmer nach maximales Preis und Mehrblick Kriterium:')
    print('6. Filter Zimmer nach minimale Preis und Mehrblick Kriterium:')
    print('7. Filter Zimmer nach maximales und minimales Preis und Mehrblick Kriterium:')
    print('----------------------------------------------------------------------------')

    rez = int(input('Wählen Sie eine Nummer: '))
    return rez

def input_filter_zimmer(criteriu):
    crt = []

    if criteriu == 1:
        pret_maxim = int(input('Gewollte maximale Preis: '))
        print('-------------------------------------')
        crt.append(pret_maxim)
        return crt
    elif criteriu == 2:
        pret_minim = int(input('Gewollte minimale Preis: '))
        print('-------------------------------------')
        crt.append(pret_minim)
        return crt
    elif criteriu == 3:
        pret_maxim = int(input('Gewollte maximale Preis: '))
        crt.append(pret_maxim)
        pret_minim = int(input('Gewollte minimale Preis: '))
        crt.append(pret_minim)
        print('-------------------------------------')
        return crt
    elif criteriu == 4:
        preferinta = input('Wollen Sie Mehrblick haben? JA/NEIN: ')
        print('---------------------------------------------')
        crt.append(preferinta)
        return crt
    elif criteriu == 5:
        crt = []
        pret_maxim = int(input('Gewollte maximale Preis: '))
        crt.append(pret_maxim)
        preferinta = input('Wollen Sie Mehrblick haben? JA/NEIN: ')
        crt.append(preferinta)
        print('---------------------------------------------')
        return crt
    elif criteriu == 6:
        crt = []
        pret_minim = int(input('Gewollte minimale Preis: '))
        crt.append(pret_minim)
        preferinta = input('Wollen Sie Mehrblick haben? JA/NEIN: ')
        crt.append(preferinta)
        print('---------------------------------------------')
        return crt
    elif criteriu == 7:
        crt = []
        pret_maxim = int(input('Gewollte maximale Preis: '))
        crt.append(pret_maxim)
        pret_minim = int(input('Gewollte minimale Preis: '))
        crt.append(pret_minim)
        preferinta = input('Wollen Sie Mehrblick haben? JA/NEIN: ')
        crt.append(preferinta)
        print('---------------------------------------------')
        return crt