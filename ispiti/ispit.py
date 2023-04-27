class Ispit:
    def __init__(self, kolegij, datum):
        self.__kolegij = kolegij
        self.__datum = datum

    @property
    def kolegij(self):
        return self.__kolegij

    @kolegij.setter
    def kolegij(self, kolegij):
        self.__kolegij = kolegij

    @property
    def datum(self):
        return self.__datum

    def ispis(self):
        print("\t Ispit iz kolegija", self.kolegij.ime, ", koji nosi", self.kolegij.ECTS, "odrzati ce se",
              self.datum)