# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AddMaterialDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_AddMaterialDialog(object):
    def setupUi(self, AddMaterialDialog):
        if not AddMaterialDialog.objectName():
            AddMaterialDialog.setObjectName(u"AddMaterialDialog")
        AddMaterialDialog.resize(439, 451)
        self.gridLayout = QGridLayout(AddMaterialDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.importMaterialButton = QPushButton(AddMaterialDialog)
        self.importMaterialButton.setObjectName(u"importMaterialButton")

        self.gridLayout.addWidget(self.importMaterialButton, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.groupBox = QGroupBox(AddMaterialDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_name = QLineEdit(self.groupBox)
        self.le_name.setObjectName(u"le_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_name)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_abs = QLineEdit(self.groupBox)
        self.le_abs.setObjectName(u"le_abs")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_abs)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.le_alpha = QLineEdit(self.groupBox)
        self.le_alpha.setObjectName(u"le_alpha")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_alpha)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.le_beta = QLineEdit(self.groupBox)
        self.le_beta.setObjectName(u"le_beta")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_beta)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.le_kappa = QLineEdit(self.groupBox)
        self.le_kappa.setObjectName(u"le_kappa")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_kappa)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.le_C = QLineEdit(self.groupBox)
        self.le_C.setObjectName(u"le_C")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_C)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.le_n = QLineEdit(self.groupBox)
        self.le_n.setObjectName(u"le_n")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.le_n)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.le_Y = QLineEdit(self.groupBox)
        self.le_Y.setObjectName(u"le_Y")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.le_Y)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_10)

        self.le_phi = QLineEdit(self.groupBox)
        self.le_phi.setObjectName(u"le_phi")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.le_phi)

        self.le_prat = QLineEdit(self.groupBox)
        self.le_prat.setObjectName(u"le_prat")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.le_prat)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(AddMaterialDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)


        self.retranslateUi(AddMaterialDialog)
        self.buttonBox.accepted.connect(AddMaterialDialog.accept)
        self.buttonBox.rejected.connect(AddMaterialDialog.reject)

        QMetaObject.connectSlotsByName(AddMaterialDialog)
    # setupUi

    def retranslateUi(self, AddMaterialDialog):
        AddMaterialDialog.setWindowTitle(QCoreApplication.translate("AddMaterialDialog", u"Add Material", None))
        self.importMaterialButton.setText(QCoreApplication.translate("AddMaterialDialog", u"Import Material", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddMaterialDialog", u"Enter material properties", None))
        self.label.setText(QCoreApplication.translate("AddMaterialDialog", u"Name", None))
        self.le_name.setText(QCoreApplication.translate("AddMaterialDialog", u"Tantala", None))
        self.label_2.setText(QCoreApplication.translate("AddMaterialDialog", u"Absorption Coefficient (a) [m\u207b\u00b9]", None))
        self.le_abs.setText(QCoreApplication.translate("AddMaterialDialog", u"0", None))
        self.label_3.setText(QCoreApplication.translate("AddMaterialDialog", u"Thermal Expansion Coefficient (\u03b1) [K\u207b\u00b9]", None))
        self.le_alpha.setText(QCoreApplication.translate("AddMaterialDialog", u"0", None))
        self.label_4.setText(QCoreApplication.translate("AddMaterialDialog", u"Thermo-optic Coefficient (dn/d\u03b8) [K\u207b\u00b9]", None))
        self.le_beta.setText(QCoreApplication.translate("AddMaterialDialog", u"0", None))
        self.label_5.setText(QCoreApplication.translate("AddMaterialDialog", u"Thermal Conductivity (\u03ba) [W m\u207b\u00b9 K\u207b\u00b9]", None))
        self.le_kappa.setText(QCoreApplication.translate("AddMaterialDialog", u"0", None))
        self.label_6.setText(QCoreApplication.translate("AddMaterialDialog", u"Volumetric Heat Capacity (C/V) [J K\u207b\u00b9 m\u207b\u00b3]", None))
        self.le_C.setText(QCoreApplication.translate("AddMaterialDialog", u"0", None))
        self.label_7.setText(QCoreApplication.translate("AddMaterialDialog", u"Refractive Index (n) [1]", None))
        self.le_n.setText(QCoreApplication.translate("AddMaterialDialog", u"0", None))
        self.label_8.setText(QCoreApplication.translate("AddMaterialDialog", u"Young's Modulus (Y) [Pa]", None))
        self.le_Y.setText(QCoreApplication.translate("AddMaterialDialog", u"0", None))
        self.label_9.setText(QCoreApplication.translate("AddMaterialDialog", u"Poisson's Ratio (\u03bd) [1]", None))
        self.label_10.setText(QCoreApplication.translate("AddMaterialDialog", u"Mechanical Loss (\u03d5\u2098) [1]", None))
        self.le_phi.setText(QCoreApplication.translate("AddMaterialDialog", u"0", None))
        self.le_prat.setText(QCoreApplication.translate("AddMaterialDialog", u"0", None))
    # retranslateUi

