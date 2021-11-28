from Entities.guest import Guest

from fct_input import *
def meniu_guest(lista_guest):
    while True:                                                #meniu activ mereu
        print('-------------------------------------------')
        print('1. Füge ein neuer Gast hin')
        print('2. Aktualisierung der Nachname eines Gastes')
        print('3. Löschung eines Gastes')
        print('4. Anzeige die Liste von Gästen')
        print('5. Go back')
        print('-------------------------------------------')
        rez = int(input('Wählen Sie eine Nummer: '))
        print('-------------------------------------------')
        if rez == 1:
            neu_guest = input_opt_add_g()
            opt_add(lista_guest, neu_guest)
        elif rez==2:
            serie_guest = input_serie_nr_buletin()
            new_nachname = input_opt_akt_nachname()
            opt_aktualisierung(lista_guest, serie_guest, new_nachname)
        elif rez == 3:
            serie_guest = input_serie_nr_buletin()
            opt_delete(lista_guest, serie_guest)
        elif rez == 4:
            opt_anzeige(lista_guest)
        elif rez == 5:
            print("Going back...")
            break

def opt_add(lista_guests, neu_guest):                                                 #adauga persoana
    lista_guests.append(neu_guest)
    return lista_guests

def opt_aktualisierung(lista_guests, serie_nr_buletin_cautat, new_nachname):                                                 #cautare dupa seria si nr din buletin -> actualizare nume de familie
    gasit = 0
    for i in range(0,len(lista_guests)):
        if lista_guests[i].serie_nr_buletin == serie_nr_buletin_cautat:                #gasim persoana cautata
            gasit = 1
            lista_guests[i].nachname = new_nachname
    if gasit == 0:                                                                     #daca persoana nu exista in lista - mesaj
        print("Kein Guest mit solche Daten des Personalausweises!")
        meniu_guest(lista_guests)
    else:
        return lista_guests

def opt_delete(lista_guests, serie_nr_buletin_cautat):                                 #stergere persoana din lista
    gasit = 0
    lungime = len(lista_guests)
    i = 0
    while i < lungime:
        if lista_guests[i].serie_nr_buletin == serie_nr_buletin_cautat:                #gasim persoana cautata
            gasit = 1
            del lista_guests[i]
            lungime -= 1                                                               #se modifica lungimea listei
        i +=1
    if gasit == 0:                                                                     #daca persoana nu exista in lista - mesaj
        print("Kein Guest mit solche Daten des Personalausweises!")
        meniu_guest(lista_guests)

def opt_anzeige(lista_guests):                                                         #afisare lista de persoane
    for guest in lista_guests:
        print(guest)