from PyQt6 import QtWidgets
from PyQt6 import QtCore

from NoiseWindow import NoiseWindow

import sys

def main():
    app = QtWidgets.QApplication(sys.argv)

    window = NoiseWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()

