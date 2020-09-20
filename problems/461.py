#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


def hammingDistance(x, y):
    
    temp = map(lambda x:int(x),list(bin(x^y)[2:]))
    return sum(i for i in list(temp))


yoyo = hammingDistance(1, 4)