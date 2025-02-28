import sys
from copy import deepcopy

from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from numpy import float64

from ui.Ui_InterfParamsDialog import Ui_InterfParamsDialog

from containers.Interferometer import Interferometer

from numpy import float64

class InterfParamsDialog(qtw.QDialog, Ui_InterfParamsDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setupUi(self)

        # Set input validators
        formLayout = self.groupBox.layout()
        for i in range(0,2):
            formLayout.itemAt(i, qtw.QFormLayout.FieldRole).widget()\
                    .setValidator(qtg.QDoubleValidator())

        # Populate interferometer params

        self.interferometer = deepcopy(self.parent().interferometer)

        beamWidth = str(self.interferometer.w)
        wavelength = str(self.interferometer.wl)
        temperature = str(self.interferometer.T)

        formLayout.itemAt(0, qtw.QFormLayout.FieldRole).widget().setText(beamWidth)
        formLayout.itemAt(1, qtw.QFormLayout.FieldRole).widget().setText(wavelength)
        formLayout.itemAt(2, qtw.QFormLayout.FieldRole).widget().setText(temperature)

    def accept(self):
        formLayout = self.groupBox.layout()

        try:
            self.interferometer = Interferometer(
                float64(formLayout.itemAt(0, qtw.QFormLayout.FieldRole).widget()\
                    .text())
                , float64(formLayout.itemAt(1, qtw.QFormLayout.FieldRole).widget()\
                    .text())
                , float64(formLayout.itemAt(2, qtw.QFormLayout.FieldRole).widget()\
                    .text())
            )
        except ValueError:
            messageBox = qtw.QMessageBox(parent=self)
            messageBox.setText("Invalid interferometer parameters!")
            messageBox.setIcon(qtw.QMessageBox.Warning)
            messageBox.setWindowTitle("Warning")
            messageBox.exec()
        
            return

        super().accept()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = InterfParamsDialog()
    window.show()

    sys.exit(app.exec())
