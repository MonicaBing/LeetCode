#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 21:31:50 2020

"""

def reverse (x):

    polar = 1
    
    if x < 0 :
        x *= -1
        polar = -1
       
    temp = list(str(x))
    return polar*int("".join(temp[::-1]))


reverse(1534236469)

