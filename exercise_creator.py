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

def create_sum_diff(sheet_name,min_sum,max_sum):
    ex_list=gen.generate_sum_diff(min_sum=min_sum,max_sum=max_sum)
    writer.create_ex_list(sheet_name,ex_list)

def create_sum_diff_w_parentheses(sheet_name,min_sum,max_sum):
    ex_list=gen.generate_sum_diff_with_parentheses(min_sum=min_sum,max_sum=max_sum)
    writer.create_ex_list(sheet_name,ex_list)

def create_sum_diff_var(sheet_name,min_sum,max_sum):
    ex_list=gen.generate_sumdiff_variable(min_sum=min_sum,max_sum=max_sum)
    writer.create_ex_list(sheet_name,ex_list)


def create_mult(sheet_name, range1_min, range1_max, range2_min, range2_max):
    ex_list=gen.generate_mult(range1=range(range1_min,range1_max+1), range2=range(range2_min,range2_max+1))
    writer.create_ex_list(sheet_name,ex_list)

def create_div(sheet_name, range1_min, range1_max, range2_min, range2_max):
    ex_list=gen.generate_div(range1=range(range1_min,range1_max+1), range2=range(range2_min,range2_max+1))
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
    ex_list=[
        {'name': '1. Add/subtract', "sheet": "sum", "method": create_sum_diff,
         "params": [
             {'name': 'min_sum', 'min': 0, 'max': 1000, 'default': 110},
             {'name': 'max_sum', 'min': 0, 'max': 1000, 'default': 220}
         ]
         },
        {'name': '2. Add/Subtract with variable', "sheet": "sum_var", "method": create_sum_diff_var,
         "params": [
             {'name': 'min_sum', 'min': 0, 'max': 1000, 'default': 110},
             {'name': 'max_sum', 'min': 0, 'max': 1000, 'default': 220}
         ]
         },
        {'name': '3. Multiplication', "sheet": "mult", "method": create_mult,
         "params": [
             {'name': 'range1_min', 'min': 0, 'max': 10, 'default': 1},
             {'name': 'range1_max', 'min': 0, 'max': 10, 'default': 9},
             {'name': 'range2_min', 'min': 0, 'max': 10, 'default': 1},
             {'name': 'range2_max', 'min': 0, 'max': 10, 'default': 9}]},
        {'name': '4. Division', "sheet": "div", "method": create_div,
         "params": [
             {'name': 'range1_min', 'min': 0, 'max': 10, 'default': 1},
             {'name': 'range1_max', 'min': 0, 'max': 10, 'default': 9},
             {'name': 'range2_min', 'min': 0, 'max': 10, 'default': 1},
             {'name': 'range2_max', 'min': 0, 'max': 10, 'default': 9}]},
        {'name': '5. Add/subtract with parentheses', "sheet": "parentheses", "method": create_sum_diff_w_parentheses,
         "params": [
             {'name': 'min_sum', 'min': 0, 'max': 1000, 'default': 110},
             {'name': 'max_sum', 'min': 0, 'max': 1000, 'default': 220}
         ]
         },
    ]
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    res=app.exec_()



    sys.exit(res)

