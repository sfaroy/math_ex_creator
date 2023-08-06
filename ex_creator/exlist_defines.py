# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Exercise creator
excercise_creator.py - Excel sheet writer class

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""



import ex_creator.ex_generator as gen
from ex_creator.xls_writer import exercise_xls_writer


def create_mult_div_parentheses(sheet_name,writer:exercise_xls_writer, min_mult, max_mult):
    ex_list = gen.generate_mult_div_parentheses(mult_range=range(min_mult, max_mult + 1))
    writer.create_ex_list(sheet_name, ex_list, ex_font_size=18)

def create_sum_diff(sheet_name,writer:exercise_xls_writer,min_sum,max_sum,ex_count):
    ex_list=gen.generate_sum_diff(min_sum=min_sum,max_sum=max_sum,count=ex_count)
    writer.create_ex_list(sheet_name,ex_list)


def create_sum_diff_mult_w_parentheses(sheet_name,writer:exercise_xls_writer, min_mult, max_mult, min_sum, max_sum):
    mult_range = range(min_mult, max_mult + 1)
    ex_list = gen.generate_mult_sum_diff_parentheses(min_sum=min_sum, max_sum=max_sum, mult_range=mult_range)
    writer.create_ex_list(sheet_name, ex_list, ex_font_size=18)

def create_sum_diff_w_parentheses(sheet_name,writer:exercise_xls_writer,min_sum,max_sum):
    ex_list=gen.generate_sum_diff_with_parentheses(min_sum=min_sum,max_sum=max_sum)
    writer.create_ex_list(sheet_name,ex_list)

def create_sum_diff_var(sheet_name,writer:exercise_xls_writer,min_sum,max_sum,ex_count):
    ex_list=gen.generate_sumdiff_variable(min_sum=min_sum,max_sum=max_sum,count=ex_count)
    writer.create_ex_list(sheet_name,ex_list)


def create_mult(sheet_name,writer:exercise_xls_writer, range1_min, range1_max, range2_min, range2_max,ex_count):
    ex_list=gen.generate_mult(range1=range(range1_min,range1_max+1), range2=range(range2_min,range2_max+1),count=ex_count)
    writer.create_ex_list(sheet_name,ex_list)


def create_mult_div_var(sheet_name,writer:exercise_xls_writer, range_min, range_max):
    ex_list = gen.generate_mult_div_var(var_range=range(range_min, range_max + 1))
    writer.create_ex_list(sheet_name, ex_list)



def create_div(sheet_name,writer:exercise_xls_writer, range1_min, range1_max, range2_min, range2_max):
    ex_list=gen.generate_div(range1=range(range1_min,range1_max+1), range2=range(range2_min,range2_max+1))
    writer.create_ex_list(sheet_name,ex_list)


def create_vertical_sub(sheet_name,writer:exercise_xls_writer, range_min, range_max, more_zeros):
    ex_list = gen.generate_vertical_sub(min_val=range_min, max_val=range_max, more_zeros=more_zeros)
    writer.create_ex_list_vertical(sheet_name, ex_list)


def create_vertical_mult_3digits_single(sheet_name,writer:exercise_xls_writer, conversion_difficulty):
    ex_list = gen.generate_vertical_mult_3digits_single(conversion_difficulty=conversion_difficulty)
    writer.create_ex_list_vertical(sheet_name, ex_list)


def create_measurements(sheet_name,writer:exercise_xls_writer, min_val, max_val, level_dist, both_directions):
    ex_list = gen.generate_measurements1(min_val=min_val, max_val=max_val, level_dist=level_dist,
                                         both_directions=both_directions)
    writer.create_ex_list(sheet_name, ex_list)


def get_exlist_dialogdef() -> list[dict]:
    """Create the array of execrise types and handles that build the exlist dialog

    Returns:
        list[dict]: The list of execrise types and handlers
    """
    ex_list=[
        {'name': '1. Add/subtract', "sheet": "sum", "method": create_sum_diff,
         "params": [
             {'name': 'min_sum', 'min': 0, 'max': 1000, 'default': 110},
             {'name': 'max_sum', 'min': 0, 'max': 1000, 'default': 220},
             {'name': 'ex_count', 'min': 0, 'max': 60, 'default': 60}
         ]
         },
        {'name': '2. Add/Subtract with variable', "sheet": "sum_var", "method": create_sum_diff_var,
         "params": [
             {'name': 'min_sum', 'min': 0, 'max': 1000, 'default': 110},
             {'name': 'max_sum', 'min': 0, 'max': 1000, 'default': 220},
             {'name': 'ex_count', 'min': 0, 'max': 60, 'default': 60}
         ]
         },
        {'name': '3. Multiplication', "sheet": "mult", "method": create_mult,
         "params": [
             {'name': 'range1_min', 'min': 0, 'max': 20, 'default': 1},
             {'name': 'range1_max', 'min': 0, 'max': 20, 'default': 10},
             {'name': 'range2_min', 'min': 0, 'max': 20, 'default': 1},
             {'name': 'range2_max', 'min': 0, 'max': 20, 'default': 10},
             {'name': 'ex_count', 'min': 0, 'max': 60, 'default': 60}]},
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
        {'name': '10. Vertical multiply with conversion', "sheet": "vert_mult_conv",
         "method": create_vertical_mult_3digits_single,
         "params": [
             {'name': 'conversion_difficulty', 'min': 0, 'max': 3, 'default': 1}
         ]
         },
        {'name': '11. Measurements', "sheet": "measure",
         "method": create_measurements,
         "params": [
             {'name': 'min_val', 'min': 1, 'max': 100, 'default': 1},
             {'name': 'max_val', 'min': 1, 'max': 100, 'default': 1},
             {'name': 'level_dist', 'min': 1, 'max': 4, 'default': 1},
             {'name': 'both_directions', 'min': 0, 'max': 1, 'default': 0}
         ]
         }
    ]
    return ex_list



