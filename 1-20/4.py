#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:04:44 2020

@author: kathykiutang
"""

import math

def findMedianSortedArrays(nums1, nums2):

    test = sorted(nums1 + nums2)
    
    if len(test) %2 == 0: #  even number
        median = (test[int((len(test)/2))-1] + test[int(len(test)/2)])*0.5
    else: #odd number 
        median = test[math.floor(len(test)/2)]
    
    return median 
        
findMedianSortedArrays([1, 3], [2])

findMedianSortedArrays([1,2], [3,4])
