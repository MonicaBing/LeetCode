#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:34:30 2020

@author: temp
"""

def shuffle(nums,n):
    first = nums[0:n]
    second = nums[n:]
    
    final = []
    
    for i in range (0,n):
        final.append(first[i])
        final.append(second[i])
    


shuffle([1,1,2,2], 2)