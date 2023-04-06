def ispis_kolegija(kolegij):
    print(f"\tKolegij {kolegij['ime']} nosi {kolegij['ects']} bodova.")

def get_kolegij(redni_broj, kolegij):
    return f"\t{redni_broj}. {kolegij['ime']}"
