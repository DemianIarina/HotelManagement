

class Hotel:
    def __init__(self, zimmern, reservierungen, file1 = 'guest.txt', file2 = 'zimmer.txt', file3 = 'reservierungen.txt'):
        self.__zimmern = zimmern
        self.__reservierungen = reservierungen
        self.__guests = []
        # super().__init__()
        self.__fGuests = file1
        self.__fZimmern = file2
        self.__fReservierungen = file3
        self.__loadFromFile()

    def __str__(self):
        return "{}: {}".format(self.zimmern, self.reservierungen, self.guests)

    def __repr__(self):
        return "{}: {}".format(self.zimmern, self.reservierungen, self.guests)

    def add_zimmern(self, Z):
        l = self.zimmern
        l.append(Z)
        self.zimmern=l

    def los_zimmern(self, Z):
        l = self.zimmern
        l.remove(Z)
        self.zimmern=l

    def add_reservierungen(self, R):
        l = self.reservierungen
        l.append(R)
        self.reservierungen=l

    def los_reservierungen(self, R):
        l = self.reservierungen
        l.remove(R)
        self.reservierungen=l

    def add_guest(self, G):
        l = self.guests
        l.append(G)
        self.guests = l

    def los_guest(self, G):
        l = self.guests
        l.remove(G)
        self.guests = l

    def __loadFromFile(self):
        f = open(self.__fGuests, 'r')

        for line in f:
            data = line.strip().split(':')
            vorname = data[0].split(';')[0]
            nachname = data[0].split(';')[1]
            serie_nr_buletin = data[0].split(';')[2]
            guests = []

            for lineroom in data[1].split('/'):
                roomnumber = lineroom.split(',')[0]
                roomsits = lineroom.split(',')[1]
                r = Raum(roomnumber, roomsits)
                rooms.append(r)

            g = Gebaude(rooms, name, id, stadt)
            self.__data.append(g)

    @property
    def zimmern(self):
        return self.__zimmern

    @zimmern.setter
    def zimmern(self, zimmern):
        self.__zimmern = zimmern

    @property
    def reservierungen(self):
        return self.__reservierungen

    @reservierungen.setter
    def reservierungen(self, reservierungen):
        self.__reservierungen = reservierungen

    @property
    def guests(self):
        return self.__guests

    @guests.setter
    def guests(self, guests):
        self.__guests = guests