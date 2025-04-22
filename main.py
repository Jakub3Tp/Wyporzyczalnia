import sys

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

    def order(self):
        name = self.ui.name.text()
        surname = self.ui.surname.text()
        birth = self.ui.dateBirth.date()
        date = self.ui.days.text()
        dateTrial = self.ui.dateTrial.date().currentDate()
        if " " in name:
            message = QMessageBox()
            message.setText("Pusto na polach")
            message.exec()

        if birth.year() <= 21:
        #now = datetime.now()
        #date21 = datetime.date(now.year - 21, now.month, now.day)
        #if birthDate > date21
            message = QMessageBox()
            message.setText("Za młody jestaś na takie wybryki")
            message.exec()

        if date.isdigit() > 0 and dateTrial.day() > 3:
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
        date = self.ui.days.text()
        dateTrial = self.ui.dateTrial.date().currentDate()
        ending = dateTrial.day() - date
        file, _ = QFileDialog().getSaveFileName(self, "Zapisz Plik", ".", "")
        with open(file, "w") as file:
            file.write(self.ui.comboVechicle.currentText())
            file.write(self.ui.dateTrial.date().currentDate())
            file.write(ending)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())