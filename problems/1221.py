#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:48:14 2020

@author: temp
"""


        
    
def balancedStringSplit(s):
    check = {'R':0, 'L':0}
    count = 0
    
    for word in s:
        check[word] += 1   
        if check['L'] == check['R']:
            count += 1
            check['L'] = 0
            check['R'] = 0
    return count


yoyo = balancedStringSplit("RLRRLLRLRL")