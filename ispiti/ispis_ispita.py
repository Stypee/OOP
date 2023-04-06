def ispis_ispita(ispit):
    print("\t Ispit iz kolegija", ispit['kolegij']['ime'], ", koji nosi", ispit['kolegij']['ects'], "odrzati ce se",
          ispit['datum'])

def get_ispit(redni_broj, ispit):
    print(f"\t{redni_broj}. Ispit iz kolegija {ispit['kolegij']['ime']}")