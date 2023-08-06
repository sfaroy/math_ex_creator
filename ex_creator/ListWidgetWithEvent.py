"""
Exercise creator
ListWidgetWithEvent.py - Main dialog

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget,QListWidget

class ListWidgetWithEvent(QListWidget):
    selection_changed = pyqtSignal()
    def __init__(self, *args):
        QWidget.__init__(self,*args)


    def selectionChanged(self, *args, **kwargs):
        self.selection_changed.emit() #type: ignore

