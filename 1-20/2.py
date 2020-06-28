#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:59:14 2020

@author: kathykiutang
"""


def convert(list): 
    res = int("".join(map(str, list))) 
      
    return res 

#  flip it
def addTwoNumbers(l1,l2):
    
    new_l1 = []
    new_l2 = []
    
    for i in range (len(l1)-1,0-1,-1):
        new_l1.append(l1[i])
        new_l2.append(l2[i])

    return (convert(new_l1) + convert(new_l2))
            

addTwoNumbers([2,4,3], [5,6,4])
