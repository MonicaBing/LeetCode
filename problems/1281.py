#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

def subtractProductAndSum(n):
    
    temp = [int(x) for x in str(n)]
    product =0
    sum = 1
    
    for i in range (0,len(temp)):
    
        sum = sum*temp[i]
        product += temp[i] 
        
    return sum - product 


yoyo = subtractProductAndSum(4421)