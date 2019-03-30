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


def create_mult_div_parentheses(sheet_name, min_mult, max_mult):
    ex_list = gen.generate_mult_div_parentheses(mult_range=range(min_mult, max_mult + 1))
    writer.create_ex_list(sheet_name, ex_list, ex_font_size=18)

def create_sum_diff(sheet_name,min_sum,max_sum):
    ex_list=gen.generate_sum_diff(min_sum=min_sum,max_sum=max_sum)
    writer.create_ex_list(sheet_name,ex_list)


def create_sum_diff_mult_w_parentheses(sheet_name, min_mult, max_mult, min_sum, max_sum):
    mult_range = range(min_mult, max_mult + 1)
    ex_list = gen.generate_mult_sum_diff_parentheses(min_sum=min_sum, max_sum=max_sum, mult_range=mult_range)
    writer.create_ex_list(sheet_name, ex_list, ex_font_size=18)

def create_sum_diff_w_parentheses(sheet_name,min_sum,max_sum):
    ex_list=gen.generate_sum_diff_with_parentheses(min_sum=min_sum,max_sum=max_sum)
    writer.create_ex_list(sheet_name,ex_list)

def create_sum_diff_var(sheet_name,min_sum,max_sum):
    ex_list=gen.generate_sumdiff_variable(min_sum=min_sum,max_sum=max_sum)
    writer.create_ex_list(sheet_name,ex_list)


def create_mult(sheet_name, range1_min, range1_max, range2_min, range2_max):
    ex_list=gen.generate_mult(range1=range(range1_min,range1_max+1), range2=range(range2_min,range2_max+1))
    writer.create_ex_list(sheet_name,ex_list)


def create_mult_div_var(sheet_name, range_min, range_max):
    ex_list = gen.generate_mult_div_var(var_range=range(range_min, range_max + 1))
    writer.create_ex_list(sheet_name, ex_list)



def create_div(sheet_name, range1_min, range1_max, range2_min, range2_max):
    ex_list=gen.generate_div(range1=range(range1_min,range1_max+1), range2=range(range2_min,range2_max+1))
    writer.create_ex_list(sheet_name,ex_list)


def create_vertical_sub(sheet_name, range_min, range_max, more_zeros):
    ex_list = gen.generate_vertical_sub(min_val=range_min, max_val=range_max, more_zeros=more_zeros)
    writer.create_ex_list_vertical(sheet_name, ex_list)


def create_measurements(sheet_name, min_val, max_val, level_dist, both_directions):
    ex_list = gen.generate_measurements1(min_val=min_val, max_val=max_val, level_dist=level_dist,
                                         both_directions=both_directions)
    writer.create_ex_list(sheet_name, ex_list)


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
             {'name': 'range1_min', 'min': 0, 'max': 20, 'default': 1},
             {'name': 'range1_max', 'min': 0, 'max': 20, 'default': 10},
             {'name': 'range2_min', 'min': 0, 'max': 20, 'default': 1},
             {'name': 'range2_max', 'min': 0, 'max': 20, 'default': 10}]},
        {'name': '4. Division', "sheet": "div", "method": create_div,
         "params": [
             {'name': 'range1_min', 'min': 0, 'max': 20, 'default': 1},
             {'name': 'range1_max', 'min': 0, 'max': 20, 'default': 10},
             {'name': 'range2_min', 'min': 0, 'max': 20, 'default': 1},
             {'name': 'range2_max', 'min': 0, 'max': 20, 'default': 10}]},
        {'name': '5. Mult/Div with variables', "sheet": "mult_div_var", "method": create_mult_div_var,
         "params": [
             {'name': 'range_min', 'min': 0, 'max': 20, 'default': 1},
             {'name': 'range_max', 'min': 0, 'max': 20, 'default': 10}]},
        {'name': '6. Add/subtract with parentheses', "sheet": "parentheses", "method": create_sum_diff_w_parentheses,
         "params": [
             {'name': 'min_sum', 'min': 0, 'max': 1000, 'default': 110},
             {'name': 'max_sum', 'min': 0, 'max': 1000, 'default': 220}
         ]
         },
        {'name': '7. Add/subtract/multiply with parentheses', "sheet": "parentheses_mult",
         "method": create_sum_diff_mult_w_parentheses,
         "params": [
             {'name': 'min_sum', 'min': 0, 'max': 1000, 'default': 110},
             {'name': 'max_sum', 'min': 0, 'max': 1000, 'default': 220},
             {'name': 'min_mult', 'min': 1, 'max': 100, 'default': 1},
             {'name': 'max_mult', 'min': 1, 'max': 100, 'default': 10}
         ]
         },
        {'name': '8. Multiply divide with parentheses', "sheet": "mult_div",
         "method": create_mult_div_parentheses,
         "params": [
             {'name': 'min_mult', 'min': 1, 'max': 100, 'default': 1},
             {'name': 'max_mult', 'min': 1, 'max': 100, 'default': 10}
         ]
         },
        {'name': '9. Vertical subtract', "sheet": "vert_sub",
         "method": create_vertical_sub,
         "params": [
             {'name': 'range_min', 'min': 1000, 'max': 9999, 'default': 1000},
             {'name': 'range_max', 'min': 1000, 'max': 9999, 'default': 9999},
             {'name': 'more_zeros', 'min': 0, 'max': 1, 'default': 0}
         ]
         },
        {'name': '9. Measurements', "sheet": "measure",
         "method": create_measurements,
         "params": [
             {'name': 'min_val', 'min': 1, 'max': 100, 'default': 1},
             {'name': 'max_val', 'min': 1, 'max': 100, 'default': 1},
             {'name': 'level_dist', 'min': 1, 'max': 4, 'default': 1},
             {'name': 'both_directions', 'min': 0, 'max': 1, 'default': 0}
         ]
         }
    ]
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    res=app.exec_()



    sys.exit(res)

