# -*- coding: utf-8 -*-
"""
Exercise creator
ex_generator.py - The excercises generator script

Licensed under the MIT License (see LICENSE for details)
Written by Roee Sfaradi
"""
# %%

import random
from random import shuffle

def generate_sum_diff(count=60,min_sum=110,max_sum=220,plus_rate=0.5):
    ex_list=[]
    for i in  range(0,count):
        sum=random.randint(min_sum,max_sum)
        a=random.randint(0,sum)
        xx=random.random()
        if xx<plus_rate:
            b=sum-a;
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
