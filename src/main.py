import sys

from PySide6 import QtWidgets

from MainWindow import MainWindow

def main():
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()
