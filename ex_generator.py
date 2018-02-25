# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:48:44 2018

@author: Roee
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

def generate_mult(count=60,range1=range(1,10),range2=range(1,10)):
    ex_list=[]

    all_perms=[]

    for j in range1:
       for k in range2:
           all_perms.append((min(i,k),max(i,k)))

    all_perms=list(set(all_perms)) #make this list unique

    all_perms=shuffle(all_perms)
   
    this_count=min(count,len(all_perms))

    for n in range(0,this_count):
       i,k=all_perms(n)
       xx=random.random()
       if xx<0.5:
           i,k=k,i #swap
       ex="{0}x{1}=".format(i,k)
       ex_list.append(ex)

    if this_count<count: #fill rest of the list with empty spaces
        for i in range(0,count-this_count):
            ex_list.append("")
       
    return ex_list
    
           
#list1=generate_sum_diff()