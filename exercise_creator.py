# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:21:09 2018

@author: Roee
"""

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
    ex_list=[{'name':'כפל',"sheet":"mult","method":create_mult},
             {'name':'חיבור/חיסור',"sheet":"sum","method":create_sum_diff},
             {'name':'חיבור/חיסור עם נעלם',"sheet":"sum_var","method":create_sum_diff_var}]
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    res=app.exec_()


    # writer.write("exercises.xls")
    # from win32com.client import Dispatch

    # xl = Dispatch("Excel.Application")
    # xl.Visible = True # otherwise excel is hidden

    # from os import path as osp

    # ex_file=osp.join(osp.abspath("."),'exercises.xls')

    # # newest excel does not accept forward slash in path
    # wb = xl.Workbooks.Open(ex_file)

    sys.exit(res)

