#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
combination sum
"""
from itertools import combinations_with_replacement

def combinationSum(candidates, target):
    
    output = []
    candidates.sort()

    for i in range (len(candidates)):
        for k in range (1,int(target/candidates[0])+1):
            l = list(combinations_with_replacement(candidates, k))
            for j in range (0,len(l)):
                if sum(l[j]) == target:
                    output.append(l[j])
                
    return list(set(output))            

result = combinationSum([2,7,6,3,5,1],9)