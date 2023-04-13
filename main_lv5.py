from utilities import unos_intervala
from kolegij import unos_kolegija, ispis_svih_kolegija
from ispiti import unos_ispita, ispis_svih_ispita
from student import unos_studenta, ispis_svih_studenata

kolegiji = []
ispiti = []
studenti = []

running = True

while running:
    print("-"*20)
    print("1. Unos novog kolegija")
    print("2. Unos novog ispita")
    print("3. Unos novog studenta")
    print("4. Ispis kolegija")
    print("5. Ispis ispita")
    print("6. Ispis studenata")
    print("7. Zaustavi program")
    print("-" * 20)

    akcija = unos_intervala(1,7)

    if akcija == 1:
        kolegiji.append(unos_kolegija(len(kolegiji)+1))
    elif akcija == 2:
        ispiti.append(unos_ispita(kolegiji,len(ispiti)+1))
    elif akcija == 3:
        studenti.append(unos_studenta(ispiti,len(studenti)+1))
    elif akcija == 4:
        ispis_svih_kolegija(kolegiji)
    elif akcija == 5:
        ispis_svih_ispita(ispiti)
    elif akcija == 6:
        ispis_svih_studenata(studenti)
    if akcija == 7:
        running = False



