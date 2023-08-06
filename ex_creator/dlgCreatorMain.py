# -*- coding: utf-8 -*-
"""
Exercise creator
dlgCreatorMain.py - Main dialog

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
# %%


from dlgCreatorMainUi import Ui_MainWindow as uiCreator
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from ex_creator.xls_writer import exercise_xls_writer


class DialogCreatorMain(QMainWindow):

    def __init__(self,writer):
        QMainWindow.__init__(self)
        self.ui=uiCreator()
        self.ui.setupUi(self)
        self.ui.cmdAddSheet.clicked.connect(self.AddSheet)
        self.ui.cmdCreate.clicked.connect(self.CreateExcel)
        self.ex_idx=0
        self.writer=writer
        #self.ui.wgtParams.set_parameters([{'name':'param1','min':0,'max':10,'default':4},{'name':'param2','min':0,'max':20,'default':6}])
        self.ui.lstTypes.selection_changed.connect(self.TypeSelectionChanged)

    def TypeSelectionChanged(self):
        idx=self.ui.lstTypes.currentRow()
        ex=self.ex_list[idx]
        if 'params' in ex:
            self.ui.wgtParams.set_parameters(ex['params'])
        else:
            self.ui.wgtParams.set_parameters([])


    def CreateExcel(self):
        if self.ui.lstExercises.count()>0:
            self.writer.write("exercises.xls")
            from win32com.client import Dispatch

            xl = Dispatch("Excel.Application")
            xl.Visible = True # otherwise excel is hidden

            from os import path as osp

            ex_file=osp.join(osp.abspath("."),'exercises.xls')

            # newest excel does not accept forward slash in path
            wb = xl.Workbooks.Open(ex_file)
            self.close()
        
    def AddSheet(self):
        idx=self.ui.lstTypes.currentRow()
        ex=self.ex_list[idx]
        ex_name="{0}_{1}".format(ex['sheet'],self.ex_idx)
        self.ui.lstExercises.addItem(ex_name)
        if 'params' in ex:
            d=self.ui.wgtParams.get_result()
            ex['method'](ex_name,**d)
        else:
            ex['method'](ex_name)
        self.ex_idx=self.ex_idx+1

    def SetExerciseList(self,ex_list):
        self.ex_list=ex_list
        self.ui.lstTypes.clear()
        for item in self.ex_list:
            self.ui.lstTypes.addItem(item['name'])
        

if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance(): #to work with the same interperter (such as in spyder)
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    writer=exercise_xls_writer()
    MainWindow = DialogCreatorMain(writer)
    ex_list=[{'name':'exercise1'},{'name':'exercise2'}]
    MainWindow.show()
    MainWindow.SetExerciseList(ex_list)
    sys.exit(app.exec_())

