from kolegij import get_kolegij
from datetime import date
from utilities import unos_intervala
from .ispit import Ispit
def unos_ispita(kolegiji, redni_broj):
    ispit = {
    }
    print('Popis kolegija: ')
    for i, kolegij in enumerate(kolegiji, start=1):
        print(get_kolegij(i, kolegij))

    #odabrani_kolegij = int(input('Unesite kolegij: '))
    odabrani_kolegij = unos_intervala(1,len(kolegiji))


    kolegij = kolegiji[odabrani_kolegij - 1]

    dan = int(input(f'Unesite dan {redni_broj}. ispita: '))
    mjesec = int(input(f'Unesite mjesec {redni_broj}. ispita: '))
    godina = int(input(f'Unesite godinu {redni_broj}. ispita: '))
    datum = date(godina, mjesec, dan)

    return Ispit(kolegij, datum)