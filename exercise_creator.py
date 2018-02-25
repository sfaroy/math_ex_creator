# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:21:09 2018

@author: Roee
"""

from dlgCreatorMain import DialogCreatorMain
from PyQt5 import QtWidgets

import ex_generator as gen
from xls_writer import exercise_xls_writer
# %%
writer=exercise_xls_writer()

def create_sum_diff(sheet_name):
    ex_list=gen.generate_sum_diff()
    writer.create_ex_list(sheet_name,ex_list)

def create_mult(sheet_name):
    ex_list=gen.generate_sum_diff()
    writer.create_ex_list(sheet_name,ex_list)


if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    MainWindow = DialogCreatorMain()
    ex_list=[{'name':'כפל',"sheet":"mult","method":create_mult},{'name':'חיבור/חיסור',"sheet":"sum","method":create_sum_diff}]
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    res=app.exec_()


    writer.write("exercises.xls")

    sys.exit(res)

