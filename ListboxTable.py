# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Exercise creator
ListboxTable.py

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
# %%

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget,QAbstractItemView,QAbstractScrollArea

class NumericTableWidgetItem(QTableWidgetItem):
    def __init__(self,text,sortKey):
        QTableWidgetItem.__init__(self,text,QTableWidgetItem.UserType)
        self.sortKey=sortKey
    
    #QT uses a simple < check for sorting items, override this to use the sortKey
    def __lt__(self,other):
        return self.sortKey < other.sortKey
    
    
class ListboxTable(QTableWidget):
    def __init__(self,*__args):
        QTableWidget.__init__(self,*__args)
        
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.editTriggers=QAbstractItemView.NoEditTriggers
#        self.setSelectiuonBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSortingEnabled(True)
        
    def setData(self,data):
        self.data=data
        horHeaders =[]
        self.setColumnCount(len(self.data.keys()))
        self.setRowCOunt(len(self.data[self.data.keys()[0]]))
        
        for n,key in enumerate(self.data.keys()):
            horHeaders.append(key)
            for m,item in enumerate(self.data[key]):
                newitem=QTableWidgetItem(str(item))
                self.setItem(m,n,newitem)
                
        self.setHorizontalHeader(horHeaders)



if __name__ == "__main__":
    import sys
    from collections import OrderedDict
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    data=OrderedDict()
    data['col1']=['1','2','3']
    data['col2']=['3','4','5']
    data['col3']=['6','7','8']
    
    Table=ListboxTable()
    Table.setData(data)
    Table.show()
    
    sys.exit(app.exec_())

