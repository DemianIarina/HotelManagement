


class Reservierung:
    def __init__(self, guest, start_date, end_date):
        self.__guest = guest
        self.__zimmer = 0
        if start_date not in range(1, 1461):
            raise ValueError()
        self.__start_date = start_date
        if end_date not in range(1, 1461):
            raise ValueError()
        self.__end_date = end_date

    def __str__(self):
        return "{} {}".format(self.guest, self.zimmer)

    def __repr__(self):
        return "{}".format(self.zimmer)

    def __getitem__(self, item):
        return self.__dict__[item]  # __dict__ contains all the attributes
        # returnez valoarea unui anumit atribut a unui guest

    def __setitem__(self, item, value):
        self.__dict__[item] = value  # accesez unul dintre atributele unui anumit guest

    @property
    def guest(self):
        return self.__guest

    @guest.setter
    def guest(self, guest):
        self.__guest = guest

    @property
    def zimmer(self):
        return self.__zimmer

    @zimmer.setter
    def zimmer(self, zimmer):
        self.__zimmer = zimmer

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):
        self.__end_date = end_date

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        self.__start_date = start_date
