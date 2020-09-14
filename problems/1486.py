#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from functools import reduce


def xorOperation(n, start):

    final = [start]
    temp = start
    
    for i in range (1,n):
        final.append(temp+2)
        temp = temp + 2
    
    return reduce(lambda x, y: x ^ y, final)


