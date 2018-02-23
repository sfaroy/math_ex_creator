# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:27:19 2018

@author: Roee
"""
# %%

import xlwt


class exercise_xls_writer():
    def __init__(self):
        self.workbook=xlwt.Workbook()
    def create_ex_list(sheet_name,list):
        return
    def write(self,name):
        self.workbook.save(name)
    


writer=exercise_xls_writer()

writer.write("test2.xls")