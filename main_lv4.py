from kolegij import unos_kolegija, ispis_kolegija, get_kolegij
from ispiti import unos_ispita, ispis_ispita, get_ispit
from student import unos_studenta, ispis_studenta

kolegiji = []
ispiti = []
studenti = []

br_kolegija = int(input('Unesite broj kolegija: '))
for i in range(1,br_kolegija+1):
   kolegiji.append(unos_kolegija(i))

br_ispita = int(input('Unesite broj ispita: '))
for i in range(1,br_ispita+1):
    ispiti.append(unos_ispita(kolegiji,i))


#print("Ispis svih kolegija: ")
#for kolegij in kolegiji:
    #ispis_kolegija(kolegij)

#for ispit in ispiti:
    #ispis_ispita(ispit)

br_studenata = int(input('Unesite broj studenata: '))
for i in range(1,br_studenata+1):
    studenti.append(unos_studenta(ispiti,i))

print('Popis svih studenata: ')
for student in studenti:
    ispis_studenta(student)