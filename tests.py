from Repository.hotel import Hotel
from Menu_Gemeinsam.meniu_gemeinsam import *
from Entities.zimmer import Zimmer


def test_convert_data_nr():                  #meniu_gemeinsam -> transformarea datei din str in int
    test1 = convert_data_nr("20/02/2021")
    assert test1 == 51
    print('*')


def test_verificare_status(zimi):            #meniu_gemeinsam -> camera e ocupata? 1 = ocupata
    zimi.status = [0,1,0,0,0,1,0,1]
    test2 = verificare_status(zimi, 1, 4)
    assert test2 == 1
    print('*')


def test_less_than_price(zimmer):            #meniu_gemeinsam -> camera are pretul mai mic decat x? 1 = da
    pret_maxim = 200
    x = zimmer.preis
    test4 = less_than_price(x, pret_maxim)
    assert test4 == 1
    print('*')


def test_intre_preturi(zimmer):              #meniu_gemeinsam -> camera are pretul cuprins intre min si max? 1 = da
    pret_minim = 100
    pret_maxim = 300
    x = zimmer.preis
    test5 = intre_preturi(x, pret_maxim, pret_minim)
    assert test5 == 1
    print('*')


def test_mehrblick(zimmer):                   #meniu_gemeinsam -> camera are vedere la mare? 0 = nu
    mehrblick_opt = 'JA'
    x = zimmer.mehrblick
    test6 = mehrblick(x, mehrblick_opt)
    assert test6 == 0
    print('*')


def main():
    lista_guest = []
    lista_zimmer = []
    lista_reservierungen = []
    hotel = Hotel(lista_zimmer, lista_reservierungen)
    guest = 0

    lista_zimmer.append(Zimmer('101', 4, 200, 'blau', 'JA'))
    lista_zimmer.append(Zimmer('102', 3, 150, 'rot', 'NEIN'))
    lista_zimmer.append(Zimmer('103', 2, 100, 'weiß', 'JA'))

    lista_guest.append(Guest("Mihai", "Pop", "CJ.12346"))
    lista_guest.append(Guest("Bob", "Mahalesu", "CJ.12347"))
    lista_guest.append(Guest("Ionita", "Far", "CJ.12348"))
    lista_guest.append(Guest("Georgiana", "Iepan", "CJ.12349"))

    test_convert_data_nr()
    test_verificare_status(lista_zimmer[2])
    test_less_than_price(lista_zimmer[1])
    test_intre_preturi(lista_zimmer[0])
    test_mehrblick(lista_zimmer[1])

main()
