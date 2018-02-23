# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:21:09 2018

@author: Roee
"""

from dlgCreatorMain import DialogCreatorMain
from PyQt5 import QtWidgets

# %%

if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    MainWindow = DialogCreatorMain()
    ex_list=[{'name':'כפל'},{'name':'חיבור/חיסור'}]
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    sys.exit(app.exec_())

