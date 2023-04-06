from ispiti import get_ispit

def unos_studenta(ispiti, redni_broj):
    student = {
    }

    student['ime'] = input(f"Unesite ime {redni_broj}. studenta: ")
    student['prezime'] = input(f"Unesite prezime {redni_broj}. studenta: ")

    for i, ispit in enumerate(ispiti, start=1):
        print(get_ispit(i,ispit))

    odabrani_ispit = int(input('Unesite ispit: '))
    student['ispit'] = ispiti[odabrani_ispit - 1]

    return student