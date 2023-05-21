from iznimke import IznimkaPrazanTekst

def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u intervalu od {min} do {max}: "))

            if broj<min or broj>max:
                raise Exception('Broj nije u intervalu!')

        except ValueError:
            print('Unijeli ste znak, a ne cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj


def provjera_informacija(ime, prezime):
    while True:
        try:
            if len(ime) == 0 or len(prezime) == 0:
                raise IznimkaPrazanTekst()

        except IznimkaPrazanTekst as e:
            return str(e)
        else:
            return None
