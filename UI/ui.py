from tkinter import *
from Repository.hotel import Hotel
from Entities.guest import Guest
from Menu_Zimmer import *
from Menu_Guests import *
from Menu_Gemeinsam import *
from Entities.zimmer import Zimmer
from Entities.reservierung import Reservierung

from UI_Gemeinsam.gemeinsam_window import *
from UI_Zimmer.zimmer_window import *
from UI_Guest.guest_window import *


# class Main:
#     def __init__(self, root):
#         self.root = root
#         self.root.title('Multi Window Demo')
#         self.root.geometry('500x250')
#
#         self.button = tk.Button(self.root,  text='Press ME', command=self.create_new_window)
#         self.button.pack(fill=tk.BOTH)
#
#     def create_new_window(self):
#         self.second_window = tk.Toplevel(self.root)
#         self.second = Second(self.second_window)


class GUI:
    def __init__(self, root):
        self.root = root

        self.root.title("MENU HOTEL")
        self.root.geometry("400x400")

        btn1 = Button(self.root, text="Menü Gäste", command=self.create_guest_window())
        btn1.grid(column=0, row=0)

        btn2 = Button(self.root, text="Menü Zimmern", command=self.create_zimmer_window())
        btn2.grid(column=1, row=0)

        btn3 = Button(self.root, text="Menü für Reservierungen", command=self.create_gemeinsam_window())
        btn3.grid(column=2, row=0)

        btn4 = Button(self.root, text="Help", command=self.__help)
        btn4.grid(column=0, row=1)

        btn5 = Button(self.root, text="Exit", command=self.__exit)
        btn5.grid(column=1, row=1)


    def create_guest_window(self):pass
        # self.guest_window = tk.Toplevel(self.root)
        # self.gui_guest = GUI_Guest(self.gui_guest)

    def create_zimmer_window(self):pass
        # self.zimmer_window = tk.Toplevel(self.root)
        # self.gui_zimmer = GUI_Guest(self.gui_zimmer)

    def create_gemeinsam_window(self):pass
        # self.gemeinsam_window = tk.Toplevel(self.root)
        # self.gui_gemeinsam = GUI_Guest(self.gui_gemeinsam)


    def __exit(self):
        self.root.destroy()

    def __help(self):
        pass


