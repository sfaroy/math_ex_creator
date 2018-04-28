# -*- coding: utf-8 -*-
"""
Exercise creator
xls_writer.py - Excel sheet writer class

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
# %%

import xlwt

text_font=xlwt.Font()
text_font.name="Arial"
text_font.height = 24 * 20;

num_pattern = xlwt.Pattern()
num_pattern.pattern= xlwt.Pattern.SOLID_PATTERN
num_pattern.pattern_fore_colour=xlwt.Style.colour_map["gray25"]

borders_top_left=xlwt.Borders()
borders_top_left.top=xlwt.Borders.THICK
borders_top_left.left=xlwt.Borders.THICK
borders_top_left.bottom=xlwt.Borders.THIN
borders_top_left.right=xlwt.Borders.THIN

borders_top_mid=xlwt.Borders()
borders_top_mid.top=xlwt.Borders.THICK
borders_top_mid.left=xlwt.Borders.THIN
borders_top_mid.bottom=xlwt.Borders.THIN
borders_top_mid.right=xlwt.Borders.THIN

borders_top_right=xlwt.Borders()
borders_top_right.top=xlwt.Borders.THICK
borders_top_right.left=xlwt.Borders.THIN
borders_top_right.bottom=xlwt.Borders.THIN
borders_top_right.right=xlwt.Borders.THICK

borders_left=xlwt.Borders()
borders_left.top=xlwt.Borders.THIN
borders_left.left=xlwt.Borders.THICK
borders_left.bottom=xlwt.Borders.THIN
borders_left.right=xlwt.Borders.THIN

borders_mid=xlwt.Borders()
borders_mid.top=xlwt.Borders.THIN
borders_mid.left=xlwt.Borders.THIN
borders_mid.bottom=xlwt.Borders.THIN
borders_mid.right=xlwt.Borders.THIN

borders_right=xlwt.Borders()
borders_right.top=xlwt.Borders.THIN
borders_right.left=xlwt.Borders.THIN
borders_right.bottom=xlwt.Borders.THIN
borders_right.right=xlwt.Borders.THICK

borders_bot_left=xlwt.Borders()
borders_bot_left.top=xlwt.Borders.THIN
borders_bot_left.left=xlwt.Borders.THICK
borders_bot_left.bottom=xlwt.Borders.THICK
borders_bot_left.right=xlwt.Borders.THIN

borders_bot_mid=xlwt.Borders()
borders_bot_mid.top=xlwt.Borders.THIN
borders_bot_mid.left=xlwt.Borders.THIN
borders_bot_mid.bottom=xlwt.Borders.THICK
borders_bot_mid.right=xlwt.Borders.THIN

borders_bot_right=xlwt.Borders()
borders_bot_right.top=xlwt.Borders.THIN
borders_bot_right.left=xlwt.Borders.THIN
borders_bot_right.bottom=xlwt.Borders.THICK
borders_bot_right.right=xlwt.Borders.THICK


text_style_left=xlwt.XFStyle()
text_style_left.font=text_font
text_style_left.borders=borders_mid

text_style_top_left=xlwt.XFStyle()
text_style_top_left.font=text_font
text_style_top_left.borders=borders_top_mid

text_style_right=xlwt.XFStyle()
text_style_right.font=text_font
text_style_right.borders=borders_right

text_style_top_right=xlwt.XFStyle()
text_style_top_right.font=text_font
text_style_top_right.borders=borders_top_right


text_style_bot_left=xlwt.XFStyle()
text_style_bot_left.font=text_font
text_style_bot_left.borders=borders_bot_mid

text_style_bot_right=xlwt.XFStyle()
text_style_bot_right.font=text_font
text_style_bot_right.borders=borders_bot_right


num_style_top_left=xlwt.XFStyle()
num_style_top_left.font=text_font
num_style_top_left.pattern=num_pattern
num_style_top_left.borders=borders_top_left


num_style_top_right=xlwt.XFStyle()
num_style_top_right.font=text_font
num_style_top_right.pattern=num_pattern
num_style_top_right.borders=borders_top_mid


num_style_left=xlwt.XFStyle()
num_style_left.font=text_font
num_style_left.pattern=num_pattern
num_style_left.borders=borders_left

num_style_right=xlwt.XFStyle()
num_style_right.font=text_font
num_style_right.pattern=num_pattern
num_style_right.borders=borders_mid


num_style_bot_left=xlwt.XFStyle()
num_style_bot_left.font=text_font
num_style_bot_left.pattern=num_pattern
num_style_bot_left.borders=borders_bot_left


num_style_bot_right=xlwt.XFStyle()
num_style_bot_right.font=text_font
num_style_bot_right.pattern=num_pattern
num_style_bot_right.borders=borders_bot_mid


class exercise_xls_writer():
    def __init__(self):
        self.workbook=xlwt.Workbook()
    def create_ex_list(self,sheet_name,ex_list):
        sheet=self.workbook.add_sheet(sheet_name)

        sheet.write(0,0,"{0}".format(1),style=num_style_top_left)
        sheet.write(0,2,"{0}".format(31),style=num_style_top_right)

        sheet.write(0,1,ex_list[0],style=text_style_top_left)
        sheet.write(0,3,ex_list[30],style=text_style_top_right)


        for i in range(1,29):
            sheet.write(i,0,"{0}".format(i+1),style=num_style_left)
            sheet.write(i,1,ex_list[i],style=text_style_left)
            sheet.write(i,2,"{0}".format(i+31),style=num_style_right)
            sheet.write(i,3,ex_list[i+30],style=text_style_right)

        sheet.write(29,0,"{0}".format(30),style=num_style_bot_left)
        sheet.write(29,2,"{0}".format(60),style=num_style_bot_right)

        sheet.write(29,1,ex_list[29],style=text_style_bot_left)
        sheet.write(29,3,ex_list[59],style=text_style_bot_right)

        sheet.col(0).width=1800
        sheet.col(1).width=10400
        sheet.col(2).width=1800
        sheet.col(3).width=10400
        sheet.fit_num_pages=1
        return
    def write(self,name):
        self.workbook.save(name)
    

if __name__=="__main__":
    import ex_generator as gen
    
    list1=gen.generate_sum_diff()
    
    writer=exercise_xls_writer()
    writer.create_ex_list("חיבור_חיסור",list1)
    
    
    writer.write("test2.xls")