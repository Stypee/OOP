def ispis_studenta(student):
    print(f"Student {student['ime']} {student['prezime']} je prijavio:\n\t Ispit iz kolegija {student['ispit']['kolegij']['ime']} koji će se održati {student['ispit']['datum']}")


def ispis_svih_studenata(studenti):
    print('Popis svih studenata:')
    for student in studenti:
        ispis_studenta(student)