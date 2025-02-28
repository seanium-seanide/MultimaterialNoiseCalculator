import sys

from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from numpy import float64

from ui.Ui_ViewMaterialsDialog import Ui_ViewMaterialsDialog

from containers.Material import Material

class ViewMaterialsDialog(qtw.QDialog, Ui_ViewMaterialsDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setupUi(self)

        # Populate table
        table = self.tableWidget
        materials = list(parent.materials.values())
        
        for i in range(len(materials)):
            # Insert new row
            table.insertColumn(i)

            # TODO: write a function to unpack objects of Material dataclass
            #   type into a list of QLabels. Can this be done without turning
            #   Material into a full class?
            # Make labels for data
            name = qtw.QLabel(materials[i].name)
            a = qtw.QLabel(str(materials[i].a))
            alpha = qtw.QLabel(str(materials[i].alpha))
            beta = qtw.QLabel(str(materials[i].beta))
            kappa = qtw.QLabel(str(materials[i].kappa))
            C = qtw.QLabel(str(materials[i].C))
            n = qtw.QLabel(str(materials[i].n))
            Y = qtw.QLabel(str(materials[i].Y))
            prat = qtw.QLabel(str(materials[i].prat))
            phiM = qtw.QLabel(str(materials[i].phiM))

            # Populate table row with labels
            fields = [name, a, alpha, beta, kappa, C, n, Y, prat, phiM]
            for j in range(len(fields)):
                table.setCellWidget(j, i, fields[j])
