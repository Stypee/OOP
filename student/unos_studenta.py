from ispiti import get_ispit
from utilities import unos_intervala
from .student import Student
def unos_studenta(ispiti, redni_broj):
    student = {
    }

    ime = input(f"Unesite ime {redni_broj}. studenta: ")
    prezime = input(f"Unesite prezime {redni_broj}. studenta: ")

    for i, ispit in enumerate(ispiti, start=1):
        get_ispit(i,ispit)

    #odabrani_ispit = int(input('Unesite ispit: '))
    odabrani_ispit = unos_intervala(1,len(ispiti))
    ispit = ispiti[odabrani_ispit - 1]

    return Student(ime, prezime, ispit)