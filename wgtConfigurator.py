# -*- coding: utf-8 -*-
"""
Exercise creator
wgtConfigurator.py - Configurator widget

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
# %%


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QWidget



def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class SliderTextbox(QWidget):
    def __init__(self, name, _min, _max, default):
        QWidget.__init__(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        label = QtWidgets.QLabel(self)
        label.setText(name +":")
        text_box = QtWidgets.QLineEdit(self)
        text_box.setText('{}'.format(default))
        self.text_box=text_box

        slider = QtWidgets.QSlider()
        slider.setMinimum(_min)
        slider.setMaximum(_max)
        slider.setValue(default)
        self.slider=slider

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(slider.sizePolicy().hasHeightForWidth())
        slider.setSizePolicy(sizePolicy)


        slider.valueChanged.connect(self.slider_value_changed)
        slider.setOrientation(QtCore.Qt.Horizontal)

        text_box.textChanged.connect(self.text_box_update)

        self._min_val=_min
        self._max_val=_max

        self.horizontalLayout.addWidget(label)
        self.horizontalLayout.addWidget(text_box)
        self.horizontalLayout.addWidget(slider)

    def slider_value_changed(self):
        self.text_box.setText('{}'.format(self.slider.value()))

    def text_box_update(self):
        if is_number(self.text_box.text()):
            val=float(self.text_box.text())
            val=int(val+0.5)
            val=max(min(val,self._max_val),self._min_val)

            self.text_box.setText("{}".format(val))
            self.slider.setValue(val)



    def get_value(self):
        return self.slider.value()



class Configurator(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self._params=[]
        self._ui=[]

    def set_parameters(self, param_list):
        for item in self._ui:
            self.verticalLayout.removeItem(item)
        for param in param_list:
            slider_textbox=SliderTextbox(param['name'],param['min'],param['max'],param['default'])

            self.verticalLayout.addWidget(slider_textbox)

            self._ui.append(slider_textbox)


if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():  # to work with the same interperter (such as in spyder)
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    MainWindow = Configurator()
    MainWindow.set_parameters([{'name':'param1','min':0,'max':10,'default':4},{'name':'param2','min':0,'max':20,'default':6}])
    MainWindow.show()
    sys.exit(app.exec_())

