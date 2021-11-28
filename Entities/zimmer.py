class Zimmer:
    def __init__(self, nr_zimmer, anzahl_g, preis, farbe, mehrblick):
        self.__nr_zimmer = nr_zimmer
        self.__anzahl_g = anzahl_g
        self.__preis = preis
        self.__farbe = farbe
        if mehrblick not in ["JA", "NEIN"]:
            raise ValueError()
        self.__mehrblick = mehrblick
        self.__status = [0] * 1461  # fiecare camera are o lista de disponibilitati initial 0 pe durata a 4 ani

    def __str__(self):
        return "Kameranummer: {}; Anzahl Personen: {}; Preis: {}; Farbe: {}; Mehrblick: {}".format(self.nr_zimmer, self.anzahl_g, self.preis, self.farbe, self.mehrblick)

    def __repr__(self):
        return "Kameranummer: {}; Anzahl Personen: {}; Preis: {}; Farbe: {}; Mehrblick: {}".format(self.nr_zimmer, self.anzahl_g, self.preis, self.farbe, self.mehrblick)

    def __eq__(self, other):
        return self.nr_zimmer == other.nr_zimmer

    def __getitem__(self, item):
        return self.__dict__[item]  # __dict__ contains all the attributes
        # returnez valoarea unui anumit atribut a unui guest

    def __setitem__(self, item, value):
        self.__dict__[item] = value  # accesez unul dintre atributele unui anumit guest

    def set_status(self, start_date, end_date):
        for s in range(start_date, end_date):
            self.status[s] = 1  # pe perioada cand se ocupa, il facem 1

    @property
    def nr_zimmer(self):  # se acceseaza atributul privat
        return self.__nr_zimmer

    @nr_zimmer.setter
    def nr_zimmer(self, nr_zimmer):
        self.__nr_zimmer = nr_zimmer

    @property
    def anzahl_g(self):
        return self.__anzahl_g

    @anzahl_g.setter
    def anzahl_g(self, anzahl_g):
        self.__anzahl_g = anzahl_g

    @property
    def preis(self):
        return self.__preis

    @preis.setter
    def preis(self, preis):
        self.__preis = preis

    @property
    def farbe(self):
        return self.__farbe

    @farbe.setter
    def farbe(self, farbe):
        self.__farbe = farbe

    @property
    def mehrblick(self):
        return self.__mehrblick

    @mehrblick.setter
    def mehrblick(self, mehrblick):
        self.__mehrblick = mehrblick

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status