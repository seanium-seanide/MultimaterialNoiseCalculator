from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui

class NoiseWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Thermal Noise Calculator")
        self.resize(640, 480)

        self.createMaterialEntry()

    def createMaterialEntry(self):
        # Data field 1
        self.field1 = QtWidgets.QLineEdit(parent=self)
        self.field1.setValidator(QtGui.QDoubleValidator())

        # Data field 2
        self.field2 = QtWidgets.QLineEdit(parent=self)
        self.field2.setValidator(QtGui.QDoubleValidator())

        # Data field 3
        self.field3 = QtWidgets.QLineEdit(parent=self)
        self.field3.setValidator(QtGui.QDoubleValidator())

        # Layout
        layout = QtWidgets.QFormLayout()
        layout.addRow("Field 1:", self.field1)
        layout.addRow("Field 2:", self.field2)
        layout.addRow("Field 3:", self.field3)

        self.setLayout(layout)

    def createButton(self):
        self.button = QPushButton("Enter")
