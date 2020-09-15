#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

        
def decompressRLElist(nums):
    
    result = []
    
    for i in range (0,len(nums),2):
        freq = nums[i]
        val = nums[i+1]
        
        for j in range (0,freq):
            result.append(val)
    return result

yoyo = decompressRLElist([1,1,2,3])