from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from datetime import date

from enumeratori import TipStudenta
from kolegij import Kolegij
from ispiti import Ispit
from student import RedovniStudent, VanredniStudent
from utilities import provjera_informacija


kolegiji = [
    Kolegij("PURS", 6),
    Kolegij("URS", 6),
    Kolegij("Objektno", 5),
]

ispiti = [
    Ispit(kolegiji[0], date(2023, 2, 3)),
    Ispit(kolegiji[1], date(2023, 2, 5)),
    Ispit(kolegiji[2], date(2023, 2, 4)),
]

studenti = []

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle('Objektno')
        self.setWindowIcon(QtGui.QIcon('images/python.png'))
        self.initUI()

    def initUI(self):
        offset = 30
        self.font = QtGui.QFont('Helvetica', 10)

        #Input tip korisnika
        self.tip_studenta = QtWidgets.QComboBox(self) #Padajuci izbornik

        for korisnik in TipStudenta:
            self.tip_studenta.addItem(str(korisnik.value)) #Dodane opcije u padajući izbornik(enumerator)

        self.tip_studenta.setGeometry(QtCore.QRect(150, offset, 150, 25)) #Geometrija i polozaj izbornika
        self.tip_studenta.currentTextChanged.connect(self.on_combobox_changed) #pozivanje metode kad se odabere tip studenta

        #Label ime
        self.label_ime = QtWidgets.QLabel(self) #Kreiranje labela
        self.label_ime.setFont(self.font) #Pridodati isti font kao padajućem izb.
        self.label_ime.setText('Ime') #Tekst unutar label-a
        self.label_ime.move(50, offset * 2) #Pozicija label-a

        #Input ime
        self.text_ime = QtWidgets.QLineEdit(self) #Kreiranje tekstualnog unosa
        self.text_ime.setGeometry(QtCore.QRect(150, offset * 2, 150, 25))

        #Label prezime (isti postupak kao label ime)
        self.label_prezime = QtWidgets.QLabel(self)
        self.label_prezime.setFont(self.font)
        self.label_prezime.setText('Prezime')
        self.label_prezime.move(50, offset * 3)

        #Input prezime (isti postupak kao input ime)
        self.text_prezime = QtWidgets.QLineEdit(self)
        self.text_prezime.setGeometry(QtCore.QRect(150, offset * 3, 150, 25))

        #Label broj prijava(isto kao label ime i prezime)
        self.label_broj_prijava = QtWidgets.QLabel(self)
        self.label_broj_prijava.setFont(self.font)
        self.label_broj_prijava.setText('Broj prijava')
        self.label_broj_prijava.move(50, offset * 4)

        #Input broj prijava(isto kao input ime i prezime
        self.text_broj_prijava = QtWidgets.QLineEdit(self)
        self.text_broj_prijava.setGeometry(QtCore.QRect(150, offset * 4, 150, 25))

        #Label ispit(isto)
        self.label_ispit = QtWidgets.QLabel(self)
        self.label_ispit.setFont(self.font)
        self.label_ispit.setText('Ispit')
        self.label_ispit.move(50, offset * 5)

        #Input ispit(padajući izbornik kao za tip studenta)
        self.text_ispit = QtWidgets.QComboBox(self)
        #Dodavanje ispita u padajući izbornik(iz liste ispiti)
        for ispit in ispiti:
            self.text_ispit.addItem(str(ispit.kolegij.ime))

        self.text_ispit.setGeometry(QtCore.QRect(150, offset * 5, 150 ,25))

        #Label error
        self.label_error = QtWidgets.QLabel(self)
        self.label_error.setFont(self.font)
        self.label_error.setAlignment(QtCore.Qt.AlignCenter) #Poruka se prikazuje na sredini labela
        self.label_error.setStyleSheet('color : red') #Crvena boja poruke
        self.label_error.setGeometry(QtCore.QRect(50, offset * 6, 150, 30))

        #Gumb za unos studenta
        self.unos_studenta_button = QtWidgets.QPushButton(self) #Kreiranje gumba
        self.unos_studenta_button.setFont(self.font)
        self.unos_studenta_button.setText('Unesi studenta')
        self.unos_studenta_button.setGeometry(QtCore.QRect(100, offset * 7, 150, 30))
        self.unos_studenta_button.clicked.connect(self.unos_studenta) #Metoda koja se izvodi pritiskom na gumb

    #Metoda za prikazivanje/skrivanje labela i inputa ovisno o tipu studenta
    def on_combobox_changed(self):
        if self.tip_studenta.currentText() == TipStudenta.REDOVNI.value:
            self.label_broj_prijava.show() #Prikazi label i input
            self.text_broj_prijava.show()
        elif self.tip_studenta.currentText() == TipStudenta.VANREDNI.value:
            self.label_broj_prijava.hide() #Sakri label i input
            self.text_broj_prijava.hide()

    #Metoda za spremanje unesenih podataka o studentu
    def unos_studenta(self):
        error = provjera_informacija(self.text_ime.text(),self.text_prezime.text())

        if error is None:
            if self.tip_studenta.currentText() == TipStudenta.REDOVNI.value:
                studenti.append(RedovniStudent(self.text_ime.text(), self.text_prezime.text(),
                                               ispiti[self.text_ispit.currentIndex()], self.text_broj_prijava.text()))

            elif self.tip_studenta.currentText() == TipStudenta.VANREDNI.value:
                studenti.append(VanredniStudent(self.text_ime.text(), self.text_prezime.text(),
                                                ispiti[self.text_ispit.currentIndex()]))

            self.text_ime.setText('')
            self.text_prezime.setText('')
            self.text_broj_prijava.setText('')
            self.label_error.setText('')

            student = studenti[len(studenti)-1]
            student.ispis()
        else:
            self.label_error.setText(error)



app = QtWidgets.QApplication(sys.argv)
win = App()
win.show()
sys.exit(app.exec_())

