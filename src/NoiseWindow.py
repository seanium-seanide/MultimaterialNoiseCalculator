from PyQt6 import QtWidgets
from PyQt6 import QtCore
from PyQt6 import QtGui

from getCoatAbsorption import getCoatAbsorption
from getCoatNoise import getCoatNoise
from getCoatRefl import getCoatRefl
from Material import Material

class NoiseWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """
        """
        super().__init__(parent)

        self.init()

        # Create window layout
        self.layout = QtWidgets.QHBoxLayout()

        # Populate window layout
        self.createLeftLayout()
        self.createRightLayout()

        # Add layout to window
        self.setLayout(self.layout)

    def init(self):
        """
        """
        self.setWindowTitle("Thermal Noise Calculator")
        self.resize(640, 480)

    def createLeftLayout(self):
        """
        """
        self.leftLayout = QtWidgets.QVBoxLayout()

        # Title
        title = QtWidgets.QLabel("Material Properties")
        self.leftLayout.addWidget(title)

        self.createLineEdits()

        self.layout.addLayout(self.leftLayout)
        pass

    def createRightLayout(self):
        """
        """
        self.rightLayout = QtWidgets.QVBoxLayout()

        self.createCheckBoxes()
        self.createButton()

        self.layout.addLayout(self.rightLayout)
        pass

    def createButton(self):
        """
        """
        self.button = QtWidgets.QPushButton("Run")

        self.button.clicked.connect(self.buttonCallback)

        self.rightLayout.addWidget(self.button)

    def createLineEdits(self):
        """
        """
        self.labels = [
            "Name"
            , "a"
            , "alpha"
            , "beta"
            , "kappa"
            , "C"
            , "Refractive Index"
            , "Young's Modulus"
            , "prat"
            , "Mechanical Loss"
        ]

        # Create input fields
        self.inputFields = {}
        for label in self.labels:
            # New layout for current roe
            rowLayout = QtWidgets.QHBoxLayout()

            # Add row title
            rowLayout.addWidget(QtWidgets.QLabel(label))

            # Add row input
            rowInputField = QtWidgets.QLineEdit()
            rowLayout.addWidget(rowInputField)
            self.inputFields[label] = rowInputField

            # Add row layout to left layout
            self.leftLayout.addLayout(rowLayout)

    def createCheckBoxes(self):
        """
        """
        checkboxTitles = [
            "Show Absorption Plot"
            , "Show Noise Weights Plot"
            , "Show Thermal Noise Plot"
            , "Save Data to Disk"
            , "Save Plots to Disk"
        ]

        self.checkboxNames = [
            "abs"
            , "noiseWeight"
            , "noise"
            , "saveData"
            , "savePlots"
        ]

        for title, name in zip(checkboxTitles, self.checkboxNames):
            rowLayout = QtWidgets.QHBoxLayout()

            # Checkbox
            checkbox = QtWidgets.QCheckBox()
            rowLayout.addWidget(checkbox)

            # Label
            rowLayout.addWidget(QtWidgets.QLabel(title))

            # Add layout to right layout
            self.rightLayout.addLayout(rowLayout)

    def buttonCallback(self):
        self.getData()
        self.thermalNoiseCalculation()

        print("Hello! :)")

    def getData(self):
        pass

    def thermalNoiseCalculation(self):
        pass
