class Student:
    def __init__(self, ime, prezime, ispit):
        self.ime = ime
        self.prezime = prezime
        self.ispit = ispit
    def ispis(self):
        print(f"Student {self.ime} {self.prezime} je prijavio:\n\t Ispit iz kolegija {self.ispit.kolegij.ime} koji će se održati {self.ispit.datum}")

