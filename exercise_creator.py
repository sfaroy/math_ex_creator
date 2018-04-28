# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Exercise creator
excercise_creator.py - Excel sheet writer class

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
# %%

from dlgCreatorMain import DialogCreatorMain
from PyQt5 import QtWidgets,QtGui,QtCore

import ex_generator as gen
from xls_writer import exercise_xls_writer
# %%
writer=exercise_xls_writer()

def create_sum_diff(sheet_name):
    ex_list=gen.generate_sum_diff()
    writer.create_ex_list(sheet_name,ex_list)

def create_sum_diff_var(sheet_name):
    ex_list=gen.generate_sumdiff_variable()
    writer.create_ex_list(sheet_name,ex_list)


def create_mult(sheet_name):
    ex_list=gen.generate_mult()
    writer.create_ex_list(sheet_name,ex_list)

def create_div(sheet_name):
    ex_list=gen.generate_div()
    writer.create_ex_list(sheet_name,ex_list)


if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    app_icon = QtGui.QIcon()
    app_icon.addFile('gui/icons/16x16.png', QtCore.QSize(16,16))
    app_icon.addFile('gui/icons/24x24.png', QtCore.QSize(24,24))
    app_icon.addFile('gui/icons/32x32.png', QtCore.QSize(32,32))
    app_icon.addFile('gui/icons/48x48.png', QtCore.QSize(48,48))
    app_icon.addFile('gui/icons/256x256.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)
    MainWindow = DialogCreatorMain(writer)
    ex_list=[{'name':'Multiplication',"sheet":"mult","method":create_mult},
             {'name':'Division',"sheet":"div","method":create_div},
             {'name':'Add/subtract',"sheet":"sum","method":create_sum_diff},
             {'name':'Add/Subtract with variable',"sheet":"sum_var","method":create_sum_diff_var}]
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    res=app.exec_()



    sys.exit(res)

