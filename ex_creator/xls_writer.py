# -*- coding: utf-8 -*-
"""
Exercise creator
xls_writer.py - Excel sheet writer class

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
# %%

import xlwt


def get_styles_standard(ex_font_size=24):
    styles = {}
    text_font = xlwt.Font()
    num_font = xlwt.Font()
    num_pattern = xlwt.Pattern()
    borders_top_left = xlwt.Borders()
    borders_top_mid = xlwt.Borders()
    borders_top_right = xlwt.Borders()
    borders_left = xlwt.Borders()
    borders_mid = xlwt.Borders()
    borders_right = xlwt.Borders()
    borders_bot_left = xlwt.Borders()
    borders_bot_mid = xlwt.Borders()
    borders_bot_right = xlwt.Borders()
    text_style_left = xlwt.XFStyle()
    text_style_top_left = xlwt.XFStyle()
    text_style_right = xlwt.XFStyle()
    text_style_top_right = xlwt.XFStyle()
    text_style_bot_left = xlwt.XFStyle()
    text_style_bot_right = xlwt.XFStyle()
    num_style_top_left = xlwt.XFStyle()
    num_style_top_right = xlwt.XFStyle()
    num_style_left = xlwt.XFStyle()
    num_style_right = xlwt.XFStyle()
    num_style_bot_left = xlwt.XFStyle()
    num_style_bot_right = xlwt.XFStyle()
    text_font.name = "Arial"
    text_font.height = ex_font_size * 20
    num_font.name = "Arial"
    num_font.height = 24 * 20

    num_pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    num_pattern.pattern_fore_colour = xlwt.Style.colour_map["gray25"]

    borders_top_left.top = xlwt.Borders.THICK
    borders_top_left.left = xlwt.Borders.THICK
    borders_top_left.bottom = xlwt.Borders.THIN
    borders_top_left.right = xlwt.Borders.THIN

    borders_top_mid.top = xlwt.Borders.THICK
    borders_top_mid.left = xlwt.Borders.THIN
    borders_top_mid.bottom = xlwt.Borders.THIN
    borders_top_mid.right = xlwt.Borders.THIN

    borders_top_right.top = xlwt.Borders.THICK
    borders_top_right.left = xlwt.Borders.THIN
    borders_top_right.bottom = xlwt.Borders.THIN
    borders_top_right.right = xlwt.Borders.THICK

    borders_left.top = xlwt.Borders.THIN
    borders_left.left = xlwt.Borders.THICK
    borders_left.bottom = xlwt.Borders.THIN
    borders_left.right = xlwt.Borders.THIN

    borders_mid.top = xlwt.Borders.THIN
    borders_mid.left = xlwt.Borders.THIN
    borders_mid.bottom = xlwt.Borders.THIN
    borders_mid.right = xlwt.Borders.THIN

    borders_right.top = xlwt.Borders.THIN
    borders_right.left = xlwt.Borders.THIN
    borders_right.bottom = xlwt.Borders.THIN
    borders_right.right = xlwt.Borders.THICK

    borders_bot_left.top = xlwt.Borders.THIN
    borders_bot_left.left = xlwt.Borders.THICK
    borders_bot_left.bottom = xlwt.Borders.THICK
    borders_bot_left.right = xlwt.Borders.THIN

    borders_bot_mid.top = xlwt.Borders.THIN
    borders_bot_mid.left = xlwt.Borders.THIN
    borders_bot_mid.bottom = xlwt.Borders.THICK
    borders_bot_mid.right = xlwt.Borders.THIN

    borders_bot_right.top = xlwt.Borders.THIN
    borders_bot_right.left = xlwt.Borders.THIN
    borders_bot_right.bottom = xlwt.Borders.THICK
    borders_bot_right.right = xlwt.Borders.THICK

    text_style_left.font = text_font
    text_style_left.borders = borders_mid

    text_style_top_left.font = text_font
    text_style_top_left.borders = borders_top_mid

    text_style_right.font = text_font
    text_style_right.borders = borders_right

    text_style_top_right.font = text_font
    text_style_top_right.borders = borders_top_right

    text_style_bot_left.font = text_font
    text_style_bot_left.borders = borders_bot_mid

    text_style_bot_right.font = text_font
    text_style_bot_right.borders = borders_bot_right

    num_style_top_left.font = num_font
    num_style_top_left.pattern = num_pattern
    num_style_top_left.borders = borders_top_left

    num_style_top_right.font = num_font
    num_style_top_right.pattern = num_pattern
    num_style_top_right.borders = borders_top_mid

    num_style_left.font = num_font
    num_style_left.pattern = num_pattern
    num_style_left.borders = borders_left

    num_style_right.font = num_font
    num_style_right.pattern = num_pattern
    num_style_right.borders = borders_mid

    num_style_bot_left.font = num_font
    num_style_bot_left.pattern = num_pattern
    num_style_bot_left.borders = borders_bot_left

    num_style_bot_right.font = num_font
    num_style_bot_right.pattern = num_pattern
    num_style_bot_right.borders = borders_bot_mid

    styles['text_style_bot_right'] = text_style_bot_right
    styles['text_style_bot_left'] = text_style_bot_left
    styles['num_style_bot_right'] = num_style_bot_right
    styles['num_style_bot_left'] = num_style_bot_left
    styles['text_style_right'] = text_style_right
    styles['num_style_right'] = num_style_right
    styles['text_style_left'] = text_style_left
    styles['num_style_left'] = num_style_left
    styles['text_style_top_right'] = text_style_top_right
    styles['text_style_top_left'] = text_style_top_left
    styles['num_style_top_right'] = num_style_top_right
    styles['num_style_top_left'] = num_style_top_left
    return styles


def get_styles_vertical(ex_font_size=16):
    styles = {}
    text_font = xlwt.Font()
    num_font = xlwt.Font()
    borders_text = xlwt.Borders()

    style_num = xlwt.XFStyle()
    style_text = xlwt.XFStyle()

    text_font.name = "Courier New"
    text_font.height = ex_font_size * 20
    num_font.name = "Arial"
    num_font.height = ex_font_size * 20

    borders_text.bottom = xlwt.Borders.THIN

    style_text.font = text_font
    style_text.borders = borders_text
    style_text.alignment.wrap = 1

    style_num.font = num_font

    styles['style_text'] = style_text
    styles['style_num'] = style_num

    return styles

class exercise_xls_writer():
    def __init__(self):
        self.workbook=xlwt.Workbook()

    def create_ex_list(self, sheet_name, ex_list, ex_font_size=24):
        s = get_styles_standard(ex_font_size)
        sheet=self.workbook.add_sheet(sheet_name)

        sheet.write(0, 0, "{0}".format(1), style=s['num_style_top_left'])
        sheet.write(0, 2, "{0}".format(31), style=s['num_style_top_right'])

        count = len(ex_list)
        countd2 = count//2
        sheet.write(0, 1, ex_list[0], style=s['text_style_top_left'])
        sheet.write(0, 3, ex_list[countd2], style=s['text_style_top_right'])

        for i in range(1,countd2-1):
            sheet.write(i, 0, "{0}".format(i + 1), style=s['num_style_left'])
            sheet.write(i, 1, ex_list[i], style=s['text_style_left'])
            sheet.write(i, 2, "{0}".format(i + countd2+1), style=s['num_style_right'])
            sheet.write(i, 3, ex_list[i + countd2], style=s['text_style_right'])

        sheet.write(countd2-1, 0, "{0}".format(countd2), style=s['num_style_bot_left'])
        sheet.write(countd2-1, 2, "{0}".format(count), style=s['num_style_bot_right'])

        sheet.write(countd2-1, 1, ex_list[countd2-1], style=s['text_style_bot_left'])
        sheet.write(countd2-1, 3, ex_list[count-1], style=s['text_style_bot_right'])

        sheet.col(0).width=1800
        sheet.col(1).width=10400
        sheet.col(2).width=1800
        sheet.col(3).width=10400
        sheet.fit_num_pages=1
        return

    def create_ex_list_vertical(self, sheet_name, ex_list, ex_font_size=16):
        s = get_styles_vertical(ex_font_size)
        sheet = self.workbook.add_sheet(sheet_name)

        n = 10
        N = n * 3

        for i in range(0, n):
            sheet.write(2 * i, 0, "{0}".format(i + 1), style=s['style_num'])
            sheet.write(2 * i, 3, "{0}".format(i + 11), style=s['style_num'])
            sheet.write(2 * i, 6, "{0}".format(i + 21), style=s['style_num'])

            sheet.write(2 * i, 1, ex_list[i], style=s['style_text'])
            sheet.write(2 * i, 4, ex_list[i + 10], style=s['style_text'])
            sheet.write(2 * i, 7, ex_list[i + 20], style=s['style_text'])
            sheet.row(2 * i).height = 2050
            if i < n - 1:
                sheet.row(2 * i + 1).height = 30 * 20
                sheet.row(2 * i + 1).height_mismatch = True

        sheet.col(0).width = 1208
        sheet.col(1).width = 4138
        sheet.col(2).width = 2636
        sheet.col(3).width = 1208
        sheet.col(4).width = 4138
        sheet.col(5).width = 2636
        sheet.col(6).width = 1208
        sheet.col(7).width = 4138
        sheet.fit_num_pages = 1
        return


    def write(self,name):
        self.workbook.save(name)
    

if __name__=="__main__":
    import ex_creator.ex_generator as gen
    
    list1=gen.generate_sum_diff()
    
    writer=exercise_xls_writer()
    writer.create_ex_list("חיבור_חיסור",list1)
    
    
    writer.write("test2.xls")