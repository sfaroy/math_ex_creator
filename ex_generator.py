# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:48:44 2018

@author: Roee
"""


# %%

import random

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
    
           
#list1=generate_sum_diff()