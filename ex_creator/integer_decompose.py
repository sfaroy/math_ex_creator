# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 06:45:55 2018

@author: Roee
"""

from pylab import *


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


print(integer_decompose(64))
