# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 19:00:07 2018

dlgCreatorMain.py

@author: Roee
"""

from dlgCreatorMainUi import Ui_MainWindow as uiCreator
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets

class DialogCreatorMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=uiCreator()
        self.ui.setupUi(self)
        self.ui.cmdCreate.clicked.connect(self.CreateSlot)
        self.ex_idx=0

    def CreateSlot(self):
        idx=self.ui.lstTypes.currentRow()
        ex_name="{0}_{1}".format(self.ex_list[idx]['sheet'],self.ex_idx)
        self.ex_list[idx]['method'](ex_name)
        self.ex_idx=self.ex_idx+1
        return

    def SetExerciseList(self,ex_list):
        self.ex_list=ex_list
        self.ui.lstTypes.clear()
        for item in self.ex_list:
            self.ui.lstTypes.addItem(item['name'])
        

if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    MainWindow = DialogCreatorMain()
    ex_list=[{'name':'exercise1'},{'name':'exercise2'}]
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    sys.exit(app.exec_())

