import sys
import os

import tomlkit as tmk

from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from numpy import float64

from Ui_AddMaterialDialog import Ui_AddMaterialDialog

from Material import Material

class AddMaterialDialog(qtw.QDialog, Ui_AddMaterialDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setupUi(self)

        # Set input validators
        formLayout = self.groupBox.layout()
        for i in range(1,10):
            formLayout.itemAt(i, qtw.QFormLayout.FieldRole).widget()\
                    .setValidator(qtg.QDoubleValidator())

        # Connect signals and slots
        self.importMaterialButton.clicked.connect(self.onImportMaterial)

    def accept(self):
        formLayout = self.groupBox.layout()
        #for i in range(formLayout.rowCount()):
        #    self.material.append(formLayout.itemAt(i, qtw.QFormLayout.FieldRole) \
        #            .widget().text())

        try:
            self.material = Material(
                str(formLayout.itemAt(0, qtw.QFormLayout.FieldRole).widget().text())
                , float64(formLayout.itemAt(1, qtw.QFormLayout.FieldRole).widget()\
                        .text())
                , float64(formLayout.itemAt(2, qtw.QFormLayout.FieldRole).widget()\
                        .text())
                , float64(formLayout.itemAt(3, qtw.QFormLayout.FieldRole).widget()\
                        .text())
                , float64(formLayout.itemAt(4, qtw.QFormLayout.FieldRole).widget()\
                        .text())
                , float64(formLayout.itemAt(5, qtw.QFormLayout.FieldRole).widget()\
                        .text())
                , float64(formLayout.itemAt(6, qtw.QFormLayout.FieldRole).widget()\
                        .text())
                , float64(formLayout.itemAt(7, qtw.QFormLayout.FieldRole).widget()\
                        .text())
                , float64(formLayout.itemAt(8, qtw.QFormLayout.FieldRole).widget()\
                        .text())
                , float64(formLayout.itemAt(9, qtw.QFormLayout.FieldRole).widget()\
                        .text())
            )
        except ValueError:
            messageBox = qtw.QMessageBox(parent=self)
            messageBox.setText("Invalid material parameters!")
            messageBox.setIcon(qtw.QMessageBox.Warning)
            messageBox.setWindowTitle("Warning")
            messageBox.exec()

            return

        super().accept()

    def onImportMaterial(self):
        filename = qtw.QFileDialog.getOpenFileName()[0]

        if not os.path.exists(filename):
            messageBox = qtw.QMessageBox()
            messageBox.setText()
            messageBox.setIcon(qtw.QMessageBox.Warning)
            messageBox.setWindowTitle("Warning")
            messageBox.exec()

            return

        material = Material()

        with open(filename, "r") as file:
            doc = tmk.parse(file.read())

            formLayout = self.groupBox.layout()

            name: str = ""          # Description
            a: float64 = 0.0        # Absorption per length
            alpha: float64 = 0.0    # Thermal expansion coefficient
            beta: float64 = 0.0     # Derivative of refractive index w.r.t temperature
            kappa: float64 = 0.0    # Thermal conductivity
            C: float64 = 0.0        # Heat capacity per volume
            n: float64 = 0.0        # Refractive index
            Y: float64 = 0.0        # Young's modulus
            prat: float64 = 0.0     # Poisson's rratio
            phiM: float64 = 0.0     # Mechanical loss

            formLayout.itemAt(0, qtw.QFormLayout.FieldRole).widget() \
                .setText(doc["name"])
            formLayout.itemAt(1, qtw.QFormLayout.FieldRole).widget() \
                .setText(f"{doc['a']:.16g}")
            formLayout.itemAt(2, qtw.QFormLayout.FieldRole).widget() \
                .setText(f"{doc['alpha']:.16g}")
            formLayout.itemAt(3, qtw.QFormLayout.FieldRole).widget() \
                .setText(f"{doc['beta']:.16g}")
            formLayout.itemAt(4, qtw.QFormLayout.FieldRole).widget() \
                .setText(f"{doc['kappa']:.16g}")
            formLayout.itemAt(5, qtw.QFormLayout.FieldRole).widget() \
                .setText(f"{doc['C']:.16g}")
            formLayout.itemAt(6, qtw.QFormLayout.FieldRole).widget() \
                .setText(f"{doc['n']:.16g}")
            formLayout.itemAt(7, qtw.QFormLayout.FieldRole).widget() \
                .setText(f"{doc['Y']:.16g}")
            formLayout.itemAt(8, qtw.QFormLayout.FieldRole).widget() \
                .setText(f"{doc['prat']:.16g}")
            formLayout.itemAt(9, qtw.QFormLayout.FieldRole).widget() \
                .setText(f"{doc['phiM']:.16g}")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = AddMaterialDialog()
    window.show()

    sys.exit(app.exec())
