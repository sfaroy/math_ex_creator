# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgCreatorMain.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lstExercises = QtWidgets.QListWidget(self.centralwidget)
        self.lstExercises.setObjectName("lstExercises")
        self.horizontalLayout.addWidget(self.lstExercises)
        self.lstTypes = QtWidgets.QListWidget(self.centralwidget)
        self.lstTypes.setObjectName("lstTypes")
        self.horizontalLayout.addWidget(self.lstTypes)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.txtFilter = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFilter.setEnabled(False)
        self.txtFilter.setObjectName("txtFilter")
        self.horizontalLayout_3.addWidget(self.txtFilter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmdCreate = QtWidgets.QPushButton(self.centralwidget)
        self.cmdCreate.setObjectName("cmdCreate")
        self.horizontalLayout_2.addWidget(self.cmdCreate)
        self.cmdAddSheet = QtWidgets.QPushButton(self.centralwidget)
        self.cmdAddSheet.setObjectName("cmdAddSheet")
        self.horizontalLayout_2.addWidget(self.cmdAddSheet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Exercise creator for 1st grades"))
        self.label.setText(_translate("MainWindow", "Filter:"))
        self.cmdCreate.setText(_translate("MainWindow", "Create excel"))
        self.cmdAddSheet.setText(_translate("MainWindow", "Add exercise sheet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

