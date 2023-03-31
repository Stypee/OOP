from datetime import date

kolegiji = []

br_kolegija = int(input('Unesite broj kolegija: '))

for i in range(br_kolegija):
   kolegij = {}

   kolegij['ime'] = input(f'Unesite ime {i+1}. kolegija: ')
   kolegij['ects'] = input(f'Unesite ECTS bodove za {i+1}. kolegij: ')

   kolegiji.append(kolegij)

#print('Popis svih kolegija: ')
#for kolegij in kolegiji:
#  print('\t\tKolegij',kolegij['ime'],'nosi',kolegij['ects'],'bodova')

ispiti = []

br_ispita = int(input('Unesite broj ispita: '))
for i in range(1,br_ispita+1):
   ispit = {}

   for j, kolegij in enumerate(kolegiji, start=1):
      print(f"\t{j}. {kolegij['ime']}")

   odabrani_kolegij = int(input('Unesite kolegij: '))

   ispit['kolegij'] = kolegiji[odabrani_kolegij-1]

   dan = int(input(f'Unesite dan {i}. ispita: '))
   mjesec = int(input(f'Unesite mjesec {i}. ispita: '))
   godina = int(input(f'Unesite godinu {i}. ispita: '))
   ispit['datum'] = date(godina, mjesec, dan)

   ispiti.append(ispit)

#print('Popis svih ispita: ')
#for ispit in ispiti:
#   print("\t Ispit iz kolegija",ispit['kolegij']['ime'],", koji nosi",ispit['kolegij']['ects'],"odrzati ce se",ispit['datum'])

studenti = []
br_studenta = int(input("Unesite broj studenata: "))

for k in range(1, br_studenta+1):
   student = {}
   student['ime'] = input(f"Unesite ime {k}. studenta: ")
   student['prezime'] = input(f"Unesite prezime {k}. studenta: ")

   for l, ispit in enumerate(ispiti, start=1):
      print(f"\t{l}. ispit iz kolegija {kolegij['ime']}")

   odabrani_ispit = int(input('Unesite ispit: '))
   student['ispit'] = ispiti[odabrani_ispit-1]
   studenti.append(student)

print("Popis svih studenata: ")
for student in studenti:
   print(f"Student {student['ime']} {student['prezime']} je prijavio:\n\t Ispit iz kolegija {student['ispit']['kolegij']['ime']} koji će se održati {student['ispit']['datum']}")

