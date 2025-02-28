# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InterfParamsDialog.ui'
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
    QLineEdit, QSizePolicy, QSpacerItem, QWidget)

class Ui_InterfParamsDialog(object):
    def setupUi(self, InterfParamsDialog):
        if not InterfParamsDialog.objectName():
            InterfParamsDialog.setObjectName(u"InterfParamsDialog")
        InterfParamsDialog.resize(385, 300)
        self.gridLayout = QGridLayout(InterfParamsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(InterfParamsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.groupBox = QGroupBox(InterfParamsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.retranslateUi(InterfParamsDialog)
        self.buttonBox.accepted.connect(InterfParamsDialog.accept)
        self.buttonBox.rejected.connect(InterfParamsDialog.reject)

        QMetaObject.connectSlotsByName(InterfParamsDialog)
    # setupUi

    def retranslateUi(self, InterfParamsDialog):
        InterfParamsDialog.setWindowTitle(QCoreApplication.translate("InterfParamsDialog", u"Interferometer Parameters", None))
        self.groupBox.setTitle(QCoreApplication.translate("InterfParamsDialog", u"Enter Interferometer Parameters", None))
        self.label.setText(QCoreApplication.translate("InterfParamsDialog", u"Beam Width [m]:", None))
        self.lineEdit.setText(QCoreApplication.translate("InterfParamsDialog", u"0.062", None))
        self.label_2.setText(QCoreApplication.translate("InterfParamsDialog", u"Wavelength [m]:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("InterfParamsDialog", u"1064e-9", None))
        self.label_3.setText(QCoreApplication.translate("InterfParamsDialog", u"Temperature [K]:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("InterfParamsDialog", u"290", None))
    # retranslateUi

