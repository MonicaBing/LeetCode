#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""


def runningSum(nums):
    
    length = len(nums)
    
    result = []
    
    for i in range (0,length):
        result.append(0)
        
    result[0] = nums[0]
    
    for i in range (1,length):
        result[i] = result[i-1] + nums[i] 
        
    return result


yoyo = runningSum([3,1,2,10,1])