import sys
from datetime import datetime

from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.order.clicked.connect(self.order)
        self.ui.export_2.clicked.connect(self.export)
        self.show()

        self.name = self.ui.name.text()
        self.surname = self.ui.surname.text()
        self.birth = self.ui.dateBirth.date()
        self.date = self.ui.days.text()
        self.dateTrial = self.ui.dateTrial.date().currentDate()


    def order(self):
        #if " " in self.name:
        if self.name == " " or self.surname == " ":
            message = QMessageBox()
            message.setText("Pusto na polach")
            message.exec()

        if self.birth.year() <= 21:
        #now = datetime.now()
        #date21 = datetime.date(now.year - 21, now.month, now.day)
        #if birthDate > date21
            message = QMessageBox()
            message.setText("Za młody jestaś na takie wybryki")
            message.exec()

        if self.date.isdigit() > 0 and self.dateTrial.day() > 3:
            message = QMessageBox()
            message.setText("Nie podróżuj w czasie!")
            message.exec()

        #code, ok = QInputDialog().getInt(self, "Weryfikacja","Podaj kod")
        #if ok:
        #   code = int(code)
        #   if code % 3 == 0:
        #       self.ui.button.setEnabled(True)
        #       self.ui.button.clicked.connect(self.export)

    def export(self):
        ending = self.dateTrial.day() - self.date
        file, _ = QFileDialog().getSaveFileName(self, "Zapisz Plik", ".", "")
        with open(file, "w") as file:
            file.write(self.ui.comboVechicle.currentText())
            file.write(self.ui.dateTrial.date().currentDate())
            file.write(ending)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())