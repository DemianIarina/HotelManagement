from Entities.guest import Guest
from Repository.hotel import Hotel
from Menu_Gemeinsam.meniu_gemeinsam import *
from Menu_Guests.meniu_guest import *
from Menu_Zimmer.menu_zimmer import *
from Entities.zimmer import Zimmer

from tkinter import *
from Menu_Gemeinsam import *
from Menu_Guests import *
from Menu_Zimmer import *
from UI.ui import GUI



def main():
    # lista_guest = []
    # lista_zimmer = []
    # lista_reservierungen = []
    # hotel = Hotel(lista_zimmer, lista_reservierungen)
    # guest = 0
    #
    # lista_zimmer.append(Zimmer('101', 4, 200, 'blau', 'JA'))
    # lista_zimmer.append(Zimmer('102', 3, 150, 'rot', 'NEIN'))
    # lista_zimmer.append(Zimmer('103', 2, 100, 'weiß', 'JA'))
    #
    # lista_guest.append(Guest("Mihai", "Pop", "CJ.12346"))
    # lista_guest.append(Guest("Bob", "Mahalesu", "CJ.12347"))
    # lista_guest.append(Guest("Ionita", "Far", "CJ.12348"))
    # lista_guest.append(Guest("Georgiana", "Iepan", "CJ.12349"))
    #
    # while True:  # meniu activ mereu
    #     print('-------------------------------------------')
    #     print('1. Meniu Gäst')
    #     print('2. Meniu Zimmer')
    #     print('3. Meniu Gemeinsam')
    #     print('4. Exit')
    #     print('-------------------------------------------')
    #
    #     rez = int(input('Wählen Sie eine Nummer: '))
    #     if rez == 1:
    #         meniu_guest(lista_guest)
    #     elif rez==2:
    #         meniu_zimmer(lista_zimmer)
    #     elif rez == 3:
    #         meniu_gemeinsam(hotel)
    #     elif rez == 4:
    #         print("Quiting...")
    #         break


    hotel = Hotel()
    control = Controller(hotel)

    root = Tk()
    g = GUI(control, root)
    g.draw_window()
    root.mainloop()  # BLOCKS


main()