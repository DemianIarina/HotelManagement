from Entities.zimmer import Zimmer
from fct_input import *

def meniu_zimmer(lista_zimmer):
    while True:                                                 #meniu activ mereu
        print('-------------------------------------------')
        print('1. Füge ein Zimmer hin')
        print('2. Aktualisierung des Preises eines Zimmers')
        print('3. Löschung eines Zimmers')
        print('4. Anzeige die Liste von Zimmern')
        print('5. Go back')
        print('-------------------------------------------')
        rez = int(input('Wählen Sie eine Nummer: '))
        print('-------------------------------------------')

        if rez == 1:
            neu_zimmer = input_opt_add_z()
            opt_add(lista_zimmer, neu_zimmer)
        elif rez == 2:
            nr_zimmer = input_nr_camera()
            preis = input_opt_akt_preis()
            opt_aktualisierung(lista_zimmer, nr_zimmer, preis)
        elif rez == 3:
            nr_zimmer = input_nr_camera()
            opt_delete(lista_zimmer, nr_zimmer)
        elif rez == 4:
            opt_anzeige(lista_zimmer)
        elif rez == 5:
            print("Going back...")
            break


def opt_add(lista_zimmer, neu_zimmer):                                      #adauga o camera
    lista_zimmer.append(neu_zimmer)
    return lista_zimmer


def opt_aktualisierung(lista_zimmer, nr_zimmer_cautat, neues_preis):                                       #actualizeaza o camera
    gasit = 0

    for i in range(0, len(lista_zimmer)):                                   #cauta camera dorita
        if lista_zimmer[i].nr_zimmer == nr_zimmer_cautat:
            gasit = 1
            lista_zimmer[i].preis = neues_preis

    if gasit == 0:                                                          #verificare daca exista camera dorita
        print("Keine Zimmer mit diesem Nummer!")
        meniu_zimmer(lista_zimmer)
    else:
        return lista_zimmer


def opt_delete(lista_zimmer, nr_zimmer_cautat):                                               #sterge o anumita camera
    gasit = 0
    lungime = len(lista_zimmer)
    i = 0

    while i < lungime:                                                       #cauta camera dori
        if lista_zimmer[i].nr_zimmer == nr_zimmer_cautat:
            gasit = 1
            del lista_zimmer[i]
            lungime -= 1
        i += 1

    if gasit == 0:                                                          #verificare daca exista camera dorita
        print("Die gesuchte Zimmer wurde nicht gefunden!")
        meniu_zimmer(lista_zimmer)


def opt_anzeige(lista_zimmer):                                              #actualizare camera
    for zimmer in lista_zimmer:
        print(zimmer)
