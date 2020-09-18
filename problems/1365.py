#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


def smallerNumbersThanCurrent(nums):
    
    result= []

    for i in nums:
        count = 0
        reference = nums.copy()
        reference.remove(i)
        for j in reference:
            if i > j:
                count += 1
        
        result.append(count)
    
    return result
        
yoyo = smallerNumbersThanCurrent([8,1,2,2,3])