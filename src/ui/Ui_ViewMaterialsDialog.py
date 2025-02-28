# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ViewMaterialsDialog.ui'
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
    QGridLayout, QGroupBox, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_ViewMaterialsDialog(object):
    def setupUi(self, ViewMaterialsDialog):
        if not ViewMaterialsDialog.objectName():
            ViewMaterialsDialog.setObjectName(u"ViewMaterialsDialog")
        ViewMaterialsDialog.resize(593, 395)
        self.gridLayout = QGridLayout(ViewMaterialsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(ViewMaterialsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.groupBox = QGroupBox(ViewMaterialsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.rowCount() < 11):
            self.tableWidget.setRowCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(ViewMaterialsDialog)
        self.buttonBox.accepted.connect(ViewMaterialsDialog.accept)
        self.buttonBox.rejected.connect(ViewMaterialsDialog.reject)

        QMetaObject.connectSlotsByName(ViewMaterialsDialog)
    # setupUi

    def retranslateUi(self, ViewMaterialsDialog):
        ViewMaterialsDialog.setWindowTitle(QCoreApplication.translate("ViewMaterialsDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("ViewMaterialsDialog", u"Material Properties", None))
        ___qtablewidgetitem = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Absorption Coefficient (a) [m\u207b\u00b9]", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Thermal Expansion Coefficient (\u03b1) [K\u207b\u00b9]", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Thermo-optic Coefficient (dn/d\u03b8) [K\u207b\u00b9]", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Thermal Conductivity (\u03ba) [W m\u207b\u00b9 K\u207b\u00b9]", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Volumetric Heat Capacity (C/V) [J K\u207b\u00b9 m\u207b\u00b3]", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Refractive Index (n) [1]", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Young's Modulus (Y) [Pa]", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Poisson's Ratio (\u03bd) [1]", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ViewMaterialsDialog", u"Mechanical Loss (\u03d5\u2098) [1]", None));
    # retranslateUi

