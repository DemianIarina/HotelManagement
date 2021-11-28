class Guest:
    def __init__(self, vorname, nachname, serie_nr_buletin):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__serie_nr_buletin = serie_nr_buletin
        self.__reservierungen = []

    def __str__(self):
        return "{} {} - {}: {}".format(self.vorname, self.nachname, self.serie_nr_buletin, self.reservierungen)

    def __repr__(self):
        return "{} {} - {}: {}".format(self.vorname, self.nachname, self.serie_nr_buletin, self.reservierungen)

    def add_reservierung(self, reservierung):
        self.__reservierungen.append(reservierung)

    def __eq__(self, other):
        return self.vorname == other.vorname and self.nachname == other.nachname

    def __getitem__(self, item):
        return self.__dict__[item]  # __dict__ contains all the attributes
        # returnez valoarea unui anumit atribut a unui guest

    def __setitem__(self, item, value):
        self.__dict__[item] = value  # accesez unul dintre atributele unui anumit guest

    @property
    def vorname(self):
        return self.__vorname

    @vorname.setter
    def vorname(self, vorname):
        self.__vorname = vorname

    @property
    def nachname(self):
        return self.__nachname

    @nachname.setter
    def nachname(self, nachname):
        self.__nachname = nachname

    @property
    def reservierungen(self):
        return self.__reservierungen

    @reservierungen.setter
    def reservierungen(self, reservierungen):
        self.__reservierungen = reservierungen

    @property
    def serie_nr_buletin(self):
        return self.__serie_nr_buletin

    @serie_nr_buletin.setter
    def serie_nr_buletin(self, serie_nr_buletin):
        self.__serie_nr_buletin = serie_nr_buletin
