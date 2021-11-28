

class Controller:
    def __init__(self, hotel):
        self.__hotel = hotel

    def add_zimmer(self, zimmer):
        self.__hotel.add_zimmern(zimmer)

    def los_zimmer(self, zimmer):
        self.__hotel.los_zimmer(zimmer)

    # def update_zimmer(self, zimmer):
    #     self.__hotel.update_zimmer(zimmer)



    def add_reservierung(self, reservierung):
        self.__hotel.add_reservierung(reservierung)

    def los_reservierung(self, reservierung):
        self.__hotel.los_reservierung(reservierung)



    def add_guest(self, guest):
        self.__hotel.add_guest(guest)

    # def update_guest(self, guest):
    #     self.__hotel.update_guest(guest)

    def los_guest(self, guest):
        self.__hotel.los_guest(guest)

    #Anzeige?