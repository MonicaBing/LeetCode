#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:31:04 2020

"""


def isValid(s):
    
    s = list(s)
    FIFO = [ ]
    
    dictionary ={
            '(':1,
            ')':-1,
            '[':2,
            ']':-2,
            '{':3,
            '}':-3
            }
    
    if len(s) % 2 != 0 :
        return False
    
    for i in range (len(s)):
        print(i)
        # left
        if dictionary[s[i]] > 0: 
            FIFO.append(s[i])
            # right
        else:
            if len(FIFO) == 0:
                return False
            
            if dictionary[s[i]] + dictionary[FIFO[-1]] == 0:
                FIFO.pop()
                
            
    if len(FIFO) == 0:
        return True
    else:
        return False

result = isValid('))')