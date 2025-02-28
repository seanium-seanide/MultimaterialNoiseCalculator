# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAddMaterial = QAction(MainWindow)
        self.actionAddMaterial.setObjectName(u"actionAddMaterial")
        self.actionViewMaterials = QAction(MainWindow)
        self.actionViewMaterials.setObjectName(u"actionViewMaterials")
        self.actionInterfParams = QAction(MainWindow)
        self.actionInterfParams.setObjectName(u"actionInterfParams")
        self.actionOutputParams = QAction(MainWindow)
        self.actionOutputParams.setObjectName(u"actionOutputParams")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.removeLayerButton = QPushButton(self.groupBox)
        self.removeLayerButton.setObjectName(u"removeLayerButton")

        self.gridLayout.addWidget(self.removeLayerButton, 1, 1, 1, 1)

        self.importStackButton = QPushButton(self.groupBox)
        self.importStackButton.setObjectName(u"importStackButton")

        self.gridLayout.addWidget(self.importStackButton, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.addLayerButton = QPushButton(self.groupBox)
        self.addLayerButton.setObjectName(u"addLayerButton")

        self.gridLayout.addWidget(self.addLayerButton, 1, 0, 1, 1)

        self.exportStackButton = QPushButton(self.groupBox)
        self.exportStackButton.setObjectName(u"exportStackButton")

        self.gridLayout.addWidget(self.exportStackButton, 1, 3, 1, 1)

        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 4)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.computeStackButton = QPushButton(self.centralwidget)
        self.computeStackButton.setObjectName(u"computeStackButton")

        self.verticalLayout.addWidget(self.computeStackButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuMaterials = QMenu(self.menubar)
        self.menuMaterials.setObjectName(u"menuMaterials")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMaterials.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuMaterials.addAction(self.actionAddMaterial)
        self.menuMaterials.addAction(self.actionViewMaterials)
        self.menuOptions.addAction(self.actionInterfParams)
        self.menuOptions.addAction(self.actionOutputParams)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Thermal Noise Calculator", None))
        self.actionAddMaterial.setText(QCoreApplication.translate("MainWindow", u"Add Material", None))
        self.actionViewMaterials.setText(QCoreApplication.translate("MainWindow", u"View Materials", None))
        self.actionInterfParams.setText(QCoreApplication.translate("MainWindow", u"Interferometer Parameters", None))
        self.actionOutputParams.setText(QCoreApplication.translate("MainWindow", u"Output Parameters", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Multilayer Stack", None))
        self.removeLayerButton.setText(QCoreApplication.translate("MainWindow", u"Remove Layer", None))
        self.importStackButton.setText(QCoreApplication.translate("MainWindow", u"Import Stack", None))
        self.addLayerButton.setText(QCoreApplication.translate("MainWindow", u"Add Layer", None))
        self.exportStackButton.setText(QCoreApplication.translate("MainWindow", u"Export Stack", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Thickness [m]", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Layer 1 is the substrate!", None))
        self.computeStackButton.setText(QCoreApplication.translate("MainWindow", u"Compute Stack Properties", None))
        self.menuMaterials.setTitle(QCoreApplication.translate("MainWindow", u"Materials", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

