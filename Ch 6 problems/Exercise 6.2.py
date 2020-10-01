# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:36:34 2020

@author: dbrown
"""

def ack(m,n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    if m < 0 or n < 0:
        print("incorrect entry")

print(ack(3,4))

