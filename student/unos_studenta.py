from ispiti import get_ispit
from utilities import unos_intervala

def unos_studenta(ispiti, redni_broj):
    student = {
    }

    student['ime'] = input(f"Unesite ime {redni_broj}. studenta: ")
    student['prezime'] = input(f"Unesite prezime {redni_broj}. studenta: ")

    for i, ispit in enumerate(ispiti, start=1):
        get_ispit(i,ispit)

    #odabrani_ispit = int(input('Unesite ispit: '))
    odabrani_ispit = unos_intervala(1,len(ispiti))
    student['ispit'] = ispiti[odabrani_ispit - 1]

    return student