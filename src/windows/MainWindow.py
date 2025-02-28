import os
from copy import deepcopy

import tomlkit as tmk

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from ui.Ui_MainWindow import Ui_MainWindow

from windows.AddMaterialDialog import AddMaterialDialog
from windows.InterfParamsDialog import InterfParamsDialog
from windows.ViewMaterialsDialog import ViewMaterialsDialog

from containers.Interferometer import Interferometer
from containers.Material import Material

import numpy as np
from numpy import float64
from numpy import int32

import matplotlib
#matplotlib.use("Agg")

import matplotlib.pyplot as plt
plt.rcParams["text.usetex"] = True
plt.rcParams["figure.dpi"] = 100
plt.rcParams["savefig.dpi"] = 100

from calculations.getCoatAbsorption import getCoatAbsorption
from calculations.getCoatRefl import getCoatRefl
from calculations.getCoatNoise import getCoatNoise

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setupUi(self)

        self.actionAddMaterial.triggered.connect(self.onAddMaterial)
        self.actionInterfParams.triggered.connect(self.onInterfParams)
        self.actionViewMaterials.triggered.connect(self.onViewMaterials)
        self.actionOutputParams.triggered.connect(self.onOutputParams)

        self.addLayerButton.clicked.connect(self.onAddLayer)
        self.removeLayerButton.clicked.connect(self.onRemoveLayer)
        self.computeStackButton.clicked.connect(self.onComputeStack)
        self.importStackButton.clicked.connect(self.onImportStack)
        self.exportStackButton.clicked.connect(self.onExportStack)

        self.materials = {}
        #tigeo2 = Material("TiGeO_2-ave", 0, 1e-6, 1e-6, 1, 1e6, 1.88, 74e9, 0.216, 3.21e-4)
        #sio2 = Material("SiO_2-ave", 0, 1e-6, 1e-6, 1, 1e6, 1.445, 74e9, 0.216, 3.21e-4)
        #substrate = Material("SiO_2-bulk", 1e-9, 1e-6, 1e-6, 1, 1e6, 1.45, 73.2e9, 0.17, 1e-9)
        tigeo2 = Material("TiGeO_2-ave", 0, 1e-6, 1e-6, 1, 1e6, 1.88, 74e9, 0.216, 3.21e-4)
        sio2 = Material("SiO_2-ave", 0, 1e-6, 1e-6, 1, 1e6, 1.445, 74e9, 0.216, 3.21e-4)
        substrate = Material("SiO_2-bulk", 1e-9, 1e-6, 1e-6, 1, 1e6, 1.45, 73.2e9, 0.17, 1e-9)
        self.materials["TiGeO_2-ave"] = tigeo2
        self.materials["SiO_2-ave"] = sio2
        self.materials["SiO_2-bulk"] = substrate

        self.materialErrors = {}
        tigeo2 = Material("TiGeO_2-ave", 0, 0, 0, 0, 0, 0, 16.1e9, 0, 1.03e-5)
        sio2 = Material("SiO_2-ave", 0, 0, 0, 0, 0, 0, 16.1e9, 0, 1.03e-5)
        substrate = Material("SiO_2-bulk", 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.materialErrors["TiGeO_2-ave"] = tigeo2
        self.materialErrors["SiO_2-ave"] = sio2
        self.materialErrors["SiO_2-bulk"] = substrate

        tigeo2 = self.addMaterials(self.materials["TiGeO_2-ave"], self.materialErrors["TiGeO_2-ave"])
        sio2 = self.addMaterials(self.materials["SiO_2-ave"], self.materialErrors["SiO_2-ave"])
        #substrate = self.addMaterials(self.materials["SiO_2-bulk"], self.materialErrors["SiO_2-bulk"])
        tigeo2.name = "TiGeoO_2-ave_max"
        sio2.name = "SiO_2-ave_max"
        substrate.name = "SiO_2-bulk_max"
        self.materials["TiGeO_2-ave_max"] = tigeo2
        self.materials["SiO_2-ave_max"] = sio2
        #self.materials["SiO_2-bulk_max"] = substrate

        tigeo2 = self.subMaterials(self.materials["TiGeO_2-ave"], self.materialErrors["TiGeO_2-ave"])
        sio2 = self.subMaterials(self.materials["SiO_2-ave"], self.materialErrors["SiO_2-ave"])
        #substrate = self.subMaterials(self.materials["SiO_2-bulk"], self.materialErrors["SiO_2-bulk"])
        tigeo2.name = "TiGeoO_2-ave_min"
        sio2.name = "SiO_2-ave_min"
        substrate.name = "SiO_2-bulk_min"
        self.materials["TiGeO_2-ave_min"] = tigeo2
        self.materials["SiO_2-ave_min"] = sio2
        #self.materials["SiO_2-bulk_min"] = substrate

        # Initialise interferometer params
        self.interferometer = Interferometer(0.062, 1064e-9, 290)

        # Output file count

        #self.outcount = 0

    def addMaterials(self, mata, matb):
        newMaterial = Material(
            mata.name
            , mata.a + matb.a
            , mata.alpha + matb.alpha
            , mata.beta + matb.beta
            , mata.kappa + matb.kappa
            , mata.C + matb.C
            , mata.n + matb.n
            , mata.Y + matb.Y
            , mata.prat + matb.prat
            , mata.phiM + matb.phiM
        )

        return newMaterial

    def subMaterials(self, mata, matb):
        newMaterial = Material(
            mata.name
            , mata.a - matb.a
            , mata.alpha - matb.alpha
            , mata.beta - matb.beta
            , mata.kappa - matb.kappa
            , mata.C - matb.C
            , mata.n - matb.n
            , mata.Y - matb.Y
            , mata.prat - matb.prat
            , mata.phiM - matb.phiM
        )

        return newMaterial

    @qtc.Slot()
    def onAddMaterial(self):
        addMaterialDialog = AddMaterialDialog(self)

        # Add material dialog
        if addMaterialDialog.exec():
            material = addMaterialDialog.material
            name = material.name

            if name in self.materials:
                messageBox = qtw.QMessageBox(parent=self)
                messageBox.setText("Material name already defined!")
                messageBox.setIcon(qtw.QMessageBox.Warning)
                messageBox.setWindowTitle("Warning")
                messageBox.exec()

                return

            self.materials[name] = material

            # Update table comboboxes
            stack = self.tableWidget
            for i in range(stack.rowCount()):
                stack.cellWidget(i, 0).addItem(name)

    @qtc.Slot()
    def onInterfParams(self):
        interfParamsDialog = InterfParamsDialog(self)

        if interfParamsDialog.exec():
            self.interferometer = interfParamsDialog.interferometer
        
    @qtc.Slot()
    def onViewMaterials(self):
        viewMaterialsDialog = ViewMaterialsDialog(self)
        viewMaterialsDialog.exec()

    # TODO
    @qtc.Slot()
    def onOutputParams(self):
        print("I herd u like outputs")

    @qtc.Slot()
    def onAddLayer(self):
        stack = self.tableWidget
        layerIndex = stack.rowCount()
        stack.insertRow(layerIndex)

        # Create combobox
        dropdown = qtw.QComboBox()
        for key in self.materials:
            dropdown.addItem(key)
        
        # Add combobox
        stack.setCellWidget(layerIndex, 0, dropdown)

        # Create line entry
        entry = qtw.QLineEdit()
        entry.setValidator(qtg.QDoubleValidator())

        # Add line entry
        stack.setCellWidget(layerIndex, 1, entry)

    @qtc.Slot()
    def onRemoveLayer(self):
        stack = self.tableWidget
        currentRowIndex = stack.currentRow()

        if currentRowIndex != -1:
            stack.removeRow(currentRowIndex)

    @qtc.Slot()
    def onImportStack(self):
        # Get filenme safely
        filename = qtw.QFileDialog.getOpenFileName()[0]
        if not os.path.exists(filename):
            messageBox = qtw.QMessageBox()
            messageBox.setText("File already exists!")
            messageBox.setIcon(qtw.QMessageBox.Warning)
            messageBox.setWindowTitle("Warning")
            messageBox.exec()

            return

        stackMaterials = []
        stackThicknesses = []

        # Open file
        with open(filename, "r") as file:
            doc = tmk.parse(file.read())
            stackMaterials += doc["materials"]
            stackThicknesses += doc["thicknesses"]

        # material and thickness vectors identical in length?
        lengthsIdentical = (len(stackMaterials) == len(stackThicknesses))

        # Materials in database?
        materialsInDatabase = True

        materialKeys = list(self.materials.keys())
        for material in set(stackMaterials):
            if material not in materialKeys:
                materialsInDatabase = False
                break

        if not (lengthsIdentical and materialsInDatabase):

            msg = "Invalid stack specification!\n"

            if not lengthsIdentical:
                msg += "\n- Material vectors not identical in length"
            if not materialsInDatabase:
                msg += "\n- Some materials not in database"

            messageBox = qtw.QMessageBox(self)
            messageBox.setText(msg)
            messageBox.setIcon(qtw.QMessageBox.Warning)
            messageBox.setWindowTitle("Warning")
            messageBox.exec()

            return

        # Clear table

        table = self.tableWidget
        #table.clearContents()
        table.setRowCount(0)
        #print(f"Num rows: {table.rowCount()}")

        """
        for i in range(table.rowCount()):
            table.removeRow(i)
        """

        # Populate table

        for i in range(len(stackMaterials)):
            table.insertRow(i)

            # Create combobox
            dropdown = qtw.QComboBox()
            for key in self.materials:
                dropdown.addItem(key)
            index = materialKeys.index(stackMaterials[i])
            dropdown.setCurrentIndex(index)
            
            # Add combobox
            table.setCellWidget(i, 0, dropdown)

            # Create line entry
            entry = qtw.QLineEdit()
            entry.setValidator(qtg.QDoubleValidator())
            entry.setText(f"{stackThicknesses[i]:.16g}")

            # Add line entry
            table.setCellWidget(i, 1, entry)

    @qtc.Slot()
    def onExportStack(self):
        print("So I herd u like exports")

        # Enter file name
        filename = qtw.QFileDialog.getSaveFileName()[0]
        print(filename)

        # Get stack data from table

        table = self.tableWidget

        stackMaterials = []
        stackThicknesses = []

        for i in range(table.rowCount()):
            # Get material
            layerMaterial = table.cellWidget(i, 0).currentText()
            stackMaterials.append(layerMaterial)

            # get thickness
            layerThickness = float64(table.cellWidget(i, 1).text())
            stackThicknesses.append(layerThickness)

        # Write output to toml file

        doc = tmk.document()

        doc.add(tmk.comment("Multilayer Stack Specification"))
        doc.add(tmk.nl())

        doc["materials"] = stackMaterials
        doc["thicknesses"] = stackThicknesses

        with open(filename, "w") as f:
            f.write(doc.as_string())

    @qtc.Slot()
    def onComputeStack(self):
        # Get stack data from tablewidget
        table = self.tableWidget
        numRows = table.rowCount()

        materials = []
        thicknesses = []

        for i in range(numRows):
            material = table.cellWidget(i, 0).currentText()
            thickness = float64(table.cellWidget(i, 1).text())

            materials.append(material)
            thicknesses.append(thickness)

        # Decide on material indices
        materialKeys = list(self.materials.keys())
        materialValues = list(self.materials.values())

        # Package stack data into arrays for computations

        numLayers = len(materials) - 1

        # materialLayer
        materialLayer = np.empty(numLayers, dtype=int32)
        for i in range(numLayers):
            materialLayer[i] = int32(materialKeys.index(materials[i + 1]))

        # dOpt
        dOpt = np.empty(numLayers, dtype=float64)
        for i in range(numLayers):
            n = self.materials[materials[i + 1]].n
            wl = self.interferometer.wl
            d = thicknesses[i + 1]
            dOpt[i] = d * n / wl

        # Substrate
        materialSub = materialKeys.index(materials[0])
        nSub = self.materials[materials[0]].n
        ySub = self.materials[materials[0]].Y
        pratSub = self.materials[materials[0]].prat

        # Layer property vectors
        nLayer = np.zeros(numLayers, dtype=float64)
        aLayer = np.zeros(numLayers, dtype=float64)
        for i in range(numLayers):
            nLayer[i] = self.materials[materials[i]].n
            aLayer[i] = self.materials[materials[i]].a

        # Material params
        materialParams = materialValues

        ######################################################
        # Compute reflectance, absorption, and thermal noise #
        ######################################################

        # Params
        f = np.logspace(0, 3, 1000)
        wBeam = self.interferometer.w
        wl = self.interferometer.wl
        Temp = self.interferometer.T

        rCoat, dcdp, rbar, r = getCoatRefl(1, nSub, nLayer, dOpt)
        absCoat, absLayer, powerLayer, rho = getCoatAbsorption(
                wl, dOpt, aLayer, nLayer, rbar, r
        );
        SbrZ, StoZ, SteZ, StrZ, brLayer = getCoatNoise(
            f, wl, wBeam, Temp, materialParams, materialSub, materialLayer, dOpt, dcdp
        )

        ##############
        # Write data #
        ##############

        # Get output file name
        filename = qtw.QFileDialog.getSaveFileName()[0]

        data = np.column_stack((f, np.sqrt(SbrZ)))
        np.savetxt(filename, data)

        #########
        # Plots #
        #########

        #
        # Absorption
        #

        fig1, ax1 = plt.subplots()
        ax1.set_yscale("log")

        ax1.scatter(np.arange(1, len(rho) + 1), rho, marker='o', label=r"$\rho_j$")
        ax1.scatter(np.arange(1, len(rho) + 1), powerLayer, marker='o', label=r"$P_j/P_0$")
        ax1.scatter(np.arange(1, len(rho) + 1), rho * powerLayer, marker='o', label=r"$\bar{\rho}_j$")

        ax1.legend(loc="upper right")

        ax1.set_title("Absorption Values")
        ax1.set_xlabel("Layer Number")
        ax1.set_xlim([0, len(rho) + 1])
        #ax1.set_ylim([1e-6, 1e1])
        ax1.grid(axis='x')
        ax1.grid(axis='y', linestyle='--')

        #
        # Noise weights for each layer
        #

        fig2, ax2 = plt.subplots()

        ax2.scatter(np.arange(1, len(rho) + 1), -dcdp, marker='o'
                , label=r"$-\partial\phi_c/\partial\phi_j$")
        ax2.scatter(np.arange(1, len(rho) + 1), brLayer, marker='o'
                , label=r"$b_j$")

        ax2.legend(loc="upper right")

        ax2.set_title("Noise Weights for Each Layer")
        ax2.set_xlabel("Layer Number")
        ax2.set_xlim([0, len(rho) + 1])
        #ax2.set_ylim([0, 2.5])
        ax2.grid(axis='x')
        ax2.grid(axis='y', linestyle='--')

        #
        # Noise plots
        #

        fig3, ax3 = plt.subplots()
        ax3.set_xscale("log")
        ax3.set_yscale("log")

        ax3.plot(f, np.sqrt(SbrZ), "r", label="Brownian Noise")
        ax3.plot(f, np.sqrt(StoZ), "b", label="Thermo-optic Noise")
        ax3.plot(f, np.sqrt(SteZ), "-.", label="TE Component")
        ax3.plot(f, np.sqrt(StrZ), "-.", label="TR Component")

        ax3.legend(loc="upper right")

        ax3.set_title("Thermal Noise")
        ax3.set_xlabel("frequency [Hz]")
        ax3.set_ylabel(r"thermal noise [$\textrm{m}/\sqrt{\textrm{Hz}}$]")
        ax3.set_xlim([1e0, 1e3])
        
        freqVal = float64(100.0)
        index = (np.abs(f - freqVal)).argmin()
        noiseVal = np.sqrt(SbrZ[index])
        ax3.text(0.1, 0.1, f"CTN @ 100 Hz = {noiseVal:.8g}", weight="bold"
            , ha="left", va="top", transform=ax3.transAxes
        )

        # Display plots
        plt.show()
