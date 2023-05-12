from ispiti import get_ispit
from utilities import unos_intervala
from .vanredni_student import VanredniStudent
from .redovni_student import RedovniStudent

def unos_studenta(ispiti, redni_broj):
    print('Odaberite tip studenta: ')
    print('\t1. Redovni')
    print('\t2. Vanredni')

    tip_studenta = int(input('Unesite tip studenta: '))

    ime = input(f"Unesite ime {redni_broj}. studenta: ")
    prezime = input(f"Unesite prezime {redni_broj}. studenta: ")

    for i, ispit in enumerate(ispiti, start=1):
        get_ispit(i,ispit)

    #odabrani_ispit = int(input('Unesite ispit: '))
    odabrani_ispit = unos_intervala(1,len(ispiti))
    ispit = ispiti[odabrani_ispit - 1]

    if tip_studenta == 1:

        broj_prijava = int(input('Unesite broj prijava:'))
        return RedovniStudent(ime, prezime, ispit, broj_prijava)

    elif tip_studenta == 2:

        return VanredniStudent(ime, prezime, ispit)

