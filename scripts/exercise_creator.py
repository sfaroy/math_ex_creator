# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Exercise creator
excercise_creator.py - Excel sheet writer class

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
from ex_creator.exlist_defines import get_exlist_dialogdef
from ex_creator.dlgCreatorMain import DialogCreatorMain
from PyQt5 import QtWidgets,QtGui,QtCore

import ex_creator.ex_generator as gen
from ex_creator.xls_writer import exercise_xls_writer

writer=exercise_xls_writer()


if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    assert isinstance(app,QtWidgets.QApplication)
    app_icon = QtGui.QIcon()
    app_icon.addFile('gui/icons/16x16.png', QtCore.QSize(16,16))
    app_icon.addFile('gui/icons/24x24.png', QtCore.QSize(24,24))
    app_icon.addFile('gui/icons/32x32.png', QtCore.QSize(32,32))
    app_icon.addFile('gui/icons/48x48.png', QtCore.QSize(48,48))
    app_icon.addFile('gui/icons/256x256.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)
    MainWindow = DialogCreatorMain(writer)
    ex_list=get_exlist_dialogdef()
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    res=app.exec_()

    sys.exit(res)

