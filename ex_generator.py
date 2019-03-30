# -*- coding: utf-8 -*-
"""
Exercise creator
ex_generator.py - The excercises generator script

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
# %%

import random
from random import randint
from random import shuffle
import numpy as np


def generate_measurements1(count=60, min_val=1, max_val=100, level_dist=1):
    measure_list = [
        ("מילימטר", 1E-3),
        ("סנטימטר", 1E-2),
        ("מטר", 1),
        ("קילומטר", 1000)
    ]

    list = []
    listlen = len(measure_list)
    for i in range(0, count):
        idx1 = randint(0, listlen - 2)
        idx2 = randint(idx1 + 1, idx1 + level_dist)
        idx2 = min(idx2, listlen - 1)

        num = randint(min_val, max_val)
        measure1 = measure_list[idx1][0]
        measure2 = measure_list[idx2][0]
        if random.random() < 0.5:
            ex = "{1} {0} =  _______ {2}".format(measure2, num, measure1)
        else:
            ex = " _______  {2} = {1} {0}".format(measure2, num, measure1)

        list.append(ex)

    return list



def generate_vertical_sub(count=30, min_val=1000, max_val=9999, more_zeros=0):
    list = []
    num_of_digits = int(np.ceil(np.log(max_val + 1) / np.log(10)))
    i = 0
    while i < count:
        val1 = random.randint(min_val, max_val)
        val2 = random.randint(min_val, max_val)


        if val2 > val1:
            val1, val2 = val2, val1

        if more_zeros > 0:
            digit_to_zero = random.randint(0, num_of_digits - 2)
            digit = val1
            if digit_to_zero > 0:
                digit = int(np.floor(digit / (10 ** digit_to_zero)))
            digit = np.mod(digit, 10)
            val1 = val1 - (10 ** digit_to_zero) * digit
            if val1 < val2:
                continue  # try again

        text = " {0}\n-{1}".format(val1, val2)
        list.append(text)
        i +=1

    return list



def get_devisor_list(a, max_div):
    l = []
    for i in range(1, max_div + 1):
        if (a % i) == 0 and a / i <= max_div:
            l.append(i)
    return l


def generate_mult_div_parentheses(count=60, mult_range=range(1, 10)):
    ex_list = []

    all_perms = []

    for j in mult_range:
        for k in mult_range:
            all_perms.append((min(j, k), max(j, k)))

    shuffle(all_perms)

    j = 0
    for n in range(0, count):
        i, k = all_perms[j]
        j = j + 1
        if j == len(all_perms):
            j = 0
            shuffle(all_perms)

        if random.random() < 0.5:
            i, k = k, i  # swap

        # {i} x {k}

        if random.random() < 0.5:
            lst = get_devisor_list(i * k, min(mult_range[-1], i * k) + 1)
            l = random.randint(0, len(lst) - 1)
            if lst[l] == i or lst[l] == k or lst[l] == 1:
                l = random.randint(0, len(lst) - 1)
            l = lst[l]  # {i} x {k} : {l}

            if random.random() < 0.5:
                ex = '({0} x {1}) : {2} = '.format(i, k, l)
            else:
                ex = '{0} x {1} : {2} = '.format(i, k, l)
        else:
            lst = get_devisor_list(k, min(mult_range[-1], k) + 1)
            l = random.randint(0, len(lst) - 1)
            if lst[l] == i or lst[l] == 1 or lst[l] == k:
                l = random.randint(0, len(lst) - 1)

            l = lst[l]  # {k} : {l} x {i}

            if random.random() < 0.5:
                if random.random() < 0.5:
                    ex = '({0} : {1}) x {2} = '.format(k, l, i)
                else:
                    ex = '{2} x ({0} : {1}) = '.format(k, l, i)

            else:
                ex = '{0} : {1} x {2} = '.format(k, l, i)

        ex_list.append(ex)

    return ex_list


# randomize single of the following:
# a*b+c*d
def rand_2mult_sum(mult_range):
    # TODO: we need to actually choose numbers from the range list - not by its limits
    a = random.randint(mult_range[0], mult_range[-1])
    b = random.randint(mult_range[0], mult_range[-1])
    c = random.randint(mult_range[0], mult_range[-1])
    d = random.randint(mult_range[0], mult_range[-1])

    if random.random() < 0.5:
        exp1 = "({0} x {1})".format(a, b)
    else:
        exp1 = "{0} x {1}".format(a, b)

    if random.random() < 0.5:
        exp2 = "({0} x {1})".format(c, d)
    else:
        exp2 = "{0} x {1}".format(c, d)

    ex = "{0} + {1} = ".format(exp1, exp2)

    return ex


# randomize single of the following:
# a*b+c
# a*b-c
# c+a*b
# c-a*b
def rand_mult_sum_diff(a, b, min_sum, max_sum, plus_rate=0.5):
    sum = random.randint(min_sum, max_sum)
    if random.random() <= plus_rate:
        if random.random() < 0.5:
            return "({0} x {1}) + {2} =".format(a, b, sum - a * b)
        else:
            return "{2} + ({0} x {1}) =".format(a, b, sum - a * b)
    else:
        if random.random() < 0.5:
            c = random.randint(0, a * b)
            return "({0} x {1}) - {2} = ".format(a, b, c)
        else:
            sum = random.randint(max(min_sum, a * b), max(max_sum, a * b))
            return "{2} - ({0} x {1}) = ".format(a, b, sum)


def integer_decompose(n):
    fact = []
    i = 2
    stop_value = round(sqrt(n))
    while i <= stop_value:
        if n % i == 0:
            fact.append(i)
            n //= i
            stop_value = int(round(sqrt(n)))
        else:
            i += 1
    fact.append(n)
    return fact


def rand_according_to_list(prob_list):
    x = random.rand()
    for i in range(0, len(prob_list)):
        if x < prob_list[i]:
            return i

    return len(prob_list) - 1


def generate_mult_sum_diff_parentheses_2(count=60, max_mult=100, plus_rate=0.5):
    div_counts = [0]
    prob_list = [0.0]
    div_counts_sum = 0
    for i in range(1, max_mult):
        divs = integer_decompose(i)
        div_counts = divs.append(len(divs))
        div_counts_sum += len(divs)

    div_counts_sum = float(div_counts_sum)
    for i in range(1, max_mult):
        prob_list.append(float(i) / div_counts_sum)
        prob_list[-1] = prob_list[-1] + prob_list[-2]

    ex_list = []

    all_perms = []

    for j in mult_range:
        for k in mult_range:
            all_perms.append((min(j, k), max(j, k)))

    shuffle(all_perms)

    j = 0
    for n in range(0, count):
        i, k = all_perms[j]
        j = j + 1
        if j == len(all_perms):
            j = 0
            shuffle(all_perms)
        xx = random.random()
        if xx < 0.5:
            i, k = k, i  # swap
        if random.random() < 0.5:
            if random.random() < 0.5:
                ex = rand_mult_sum_diff(i, k, min_sum, max_sum, plus_rate)
            else:
                ex = rand_2mult_sum(mult_range)

        else:
            ex = rand_sum_diff_mult(i, k, min_sum, max_sum, plus_rate)
        ex_list.append(ex)

    return ex_list


def rand_sum_diff_mult2(max_mult, plus_rate=0.5):
    mult_value = rand_according_to_list(prob_list)

    if random.random() <= plus_rate:
        a = random.randint(0, mult_a)
        b = mult_a - a
        c = mult_b
        if random.random() < 0.5:
            return "({0} + {1}) x {2} = ".format(a, b, c)
        else:
            return "{2} x ({0} + {1}) = ".format(a, b, c)
    else:
        val_sum = random.randint(min_sum, max_sum)
        a = val_sum
        b = val_sum - mult_a
        c = mult_b
        if random.random() < 0.5:
            return "({0} - {1}) x {2} = ".format(a, b, c)
        else:
            return "{2} x ({0} - {1}) = ".format(a, b, c)

def rand_sum_diff_mult(mult_a, mult_b, min_sum, max_sum, plus_rate=0.5):
    if random.random() <= plus_rate:
        a = random.randint(0, mult_a)
        b = mult_a - a
        c = mult_b
        if random.random() < 0.5:
            return "({0} + {1}) x {2} = ".format(a, b, c)
        else:
            return "{2} x ({0} + {1}) = ".format(a, b, c)
    else:
        val_sum = random.randint(min_sum, max_sum)
        a = val_sum
        b = val_sum - mult_a
        c = mult_b
        if random.random() < 0.5:
            return "({0} - {1}) x {2} = ".format(a, b, c)
        else:
            return "{2} x ({0} - {1}) = ".format(a, b, c)


def generate_mult_sum_diff_parentheses(count=60, min_sum=110, max_sum=220, mult_range=range(1, 10), plus_rate=0.5):
    ex_list = []

    all_perms = []

    for j in mult_range:
        for k in mult_range:
            all_perms.append((min(j, k), max(j, k)))

    shuffle(all_perms)

    j = 0
    for n in range(0, count):
        i, k = all_perms[j]
        j = j + 1
        if j == len(all_perms):
            j = 0
            shuffle(all_perms)
        xx = random.random()
        if xx < 0.5:
            i, k = k, i  # swap
        if random.random() < 0.5:
            if random.random() < 0.5:
                ex = rand_mult_sum_diff(i, k, min_sum, max_sum, plus_rate)
            else:
                ex = rand_2mult_sum(mult_range)

        else:
            ex = rand_sum_diff_mult(i, k, min_sum, max_sum, plus_rate)
        ex_list.append(ex)

    return ex_list

def generate_sum_diff(count=60,min_sum=110,max_sum=220,plus_rate=0.5):
    ex_list=[]
    for i in  range(0,count):
        sum=random.randint(min_sum,max_sum)
        a=random.randint(0,sum)
        xx=random.random()
        if xx<plus_rate:
            b = sum - a
            ex="{0}+{1}=".format(a,b)
        else:
            ex="{0}-{1}=".format(sum,a)

        ex_list.append(ex)

    return ex_list

def generate_sum_diff_expression(result,min_sum,max_sum,plus_rate):
    xx=random.random()
    if xx<plus_rate:
        a=random.randint(0,result)
        b=result-a
        ex="{0}+{1}".format(a,b)
    else:
        sum=random.randint(result,max_sum)
        a=sum-result
        ex="{0}-{1}".format(sum,a)

    return ex


def generate_sum_diff_with_parentheses(count=60,min_sum=110,max_sum=220,plus_rate=0.5):
    ex_list=[]
    for i in  range(0,count):
        sum=random.randint(min_sum,max_sum)
        a=random.randint(0,sum)
        xx=random.random()
        expression_right=random.random()<0.5
        if xx<plus_rate:
            b=sum-a
            if expression_right:
                sub_expression=generate_sum_diff_expression(b,min_sum,max_sum,plus_rate)
                ex="{0}+({1})=".format(a,sub_expression)
            else:
                sub_expression=generate_sum_diff_expression(a,min_sum,max_sum,plus_rate)
                ex="({0})+{1}=".format(sub_expression,b)

        else:
            if expression_right:
                sub_expression=generate_sum_diff_expression(a,min_sum,max_sum,plus_rate)
                ex="{0}-({1})=".format(sum,sub_expression)
            else:
                sub_expression=generate_sum_diff_expression(sum,min_sum,max_sum,plus_rate)
                ex="({0})-{1}=".format(sub_expression,a)

        ex_list.append(ex)

    return ex_list


def generate_mult_div_var(count=60, var_range=range(1, 10)):
    ex_list = []

    all_perms = []

    for j in var_range:
        for k in var_range:
            all_perms.append((min(j, k), max(j, k)))

            #  all_perms_set=set(all_perms)
            #  all_perms=list(all_perms_set) #make this list unique

    shuffle(all_perms)

    this_count = min(count, len(all_perms))

    j = 0
    for n in range(0, count):
        i, k = all_perms[j]
        j = j + 1
        if j == len(all_perms):
            j = 0
            shuffle(all_perms)
        xx = random.random()
        if xx < 0.5:
            i, k = k, i  # swap
        if random.random() < 0.5:
            if random.random() < 0.5:
                ex = "{0} x ___ = {1}".format(i, k * i)
            else:
                ex = "___ x {0} = {1}".format(i, k * i)
        else:
            if random.random() < 0.5:
                ex = "{0} : ___ = {1}".format(i * k, i)
            else:
                ex = "___ : {0} = {1}".format(i, k)

        ex_list.append(ex)

    if this_count < count:  # fill rest of the list with empty spaces
        for i in range(0, count - this_count):
            ex_list.append("")

    return ex_list


def generate_mult(count=60,range1=range(1,10),range2=range(1,10)):
    ex_list=[]

    all_perms=[]

    for j in range1:
        for k in range2:
            all_perms.append((min(j,k),max(j,k)))

            #  all_perms_set=set(all_perms)
            #  all_perms=list(all_perms_set) #make this list unique

    shuffle(all_perms)

    this_count=min(count,len(all_perms))

    j=0
    for n in range(0,count):
        i,k=all_perms[j]
        j=j+1
        if j==len(all_perms):
            j=0
            shuffle(all_perms)
        xx=random.random()
        if xx<0.5:
            i,k=k,i #swap
        ex="{0} x {1} = ".format(i,k)
        ex_list.append(ex)

    if this_count<count: #fill rest of the list with empty spaces
        for i in range(0,count-this_count):
            ex_list.append("")

    return ex_list

def generate_div(count=60,range1=range(1,10),range2=range(1,10)):
    ex_list=[]

    all_perms=[]

    for j in range1:
        for k in range2:
            all_perms.append((min(j,k),max(j,k)))

            #  all_perms_set=set(all_perms)
            #  all_perms=list(all_perms_set) #make this list unique

    shuffle(all_perms)

    this_count=min(count,len(all_perms))

    j=0
    for n in range(0,count):
        i,k=all_perms[j]
        j=j+1
        if j==len(all_perms):
            j=0
            shuffle(all_perms)
        xx=random.random()
        if xx<0.5:
            i,k=k,i #swap
        ex="{0} : {1} = ".format(i*k,k)
        ex_list.append(ex)

    if this_count<count: #fill rest of the list with empty spaces
        for i in range(0,count-this_count):
            ex_list.append("")

    return ex_list


def generate_sumdiff_variable(count=60,min_sum=70,max_sum=140,positive_ratio=0.5):

    ex_list=[]
    left_ratio=0.5

    for i in range(0,count):

        xx=random.random()
        if xx<=positive_ratio:
            sum=random.randint(min_sum,max_sum)
            a=random.randint(0,sum)
            xx=random.random()
            is_left=(xx>left_ratio)
            if not is_left:
                ex='{0} + _____ = {1}'.format(a,sum)
            else:
                ex='_____ + {0} = {1}'.format(a,sum)
        else:
            sum=random.randint(min_sum,max_sum)
            a=random.randint(0,sum)
            xx=random.random()
            is_left=(xx>left_ratio)
            if not is_left:
                ex='{0} - _____ = {1}'.format(sum,a)
            else:
                ex='_____ - {0} = {1}'.format(a,sum-a)
        ex_list.append(ex)

    return ex_list
