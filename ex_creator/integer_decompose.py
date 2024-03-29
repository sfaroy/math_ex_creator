"""
Created on Tue Nov 27 06:45:55 2018

@author: Roee
"""
from pylab import sqrt


def integer_decompose(n:int) -> list[int]:
    fact:list[int] = []
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


