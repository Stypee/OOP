from datetime import date

kolegij = {
}

kolegij['ime'] = input('Unesite ime kolegija: ').upper()
kolegij['broj_ects'] = int(input('Unesite ECTS bodove za kolegij: '))

# print('Kolegij',kolegij['ime'],'nosi',kolegij['broj_ects'],'ECTS bodova')

ispit = {

}

dan = int(input('Unesite dan ispita: '))
mjesec = int(input('Unesite mjesec ispita: '))
godina = int(input('Unesite godinu ispita: '))
ispit['datum'] = date(godina,mjesec,dan)
ispit['kolegij'] = kolegij

# print('Kolegij',ispit['kolegij']['ime'],'nosi',ispit['kolegij']['broj_ects'],'ECTS bodova.')
# print('Datum ispita je:',ispit['datum'])

student = {

}

student['ime'] = input('Unesite ime studenta: ').capitalize()
student['prezime'] = input('Unesite ime studenta: ').capitalize()
student['kolegij'] = ispit['kolegij']['ime']
student['ispit'] = ispit

print('Student',student['ime'],student['prezime'],'je prijavio ispit iz kolegija',student['kolegij'],
      'koji će se održati',student['ispit']['datum'])

