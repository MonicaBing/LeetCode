#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


def restoreString(s, indices):
    
    length = len(indices)
    result= []
    
    for i in range (0,length):
        result.append(0)
        
    for i in range (0,length):
        result[indices[i]] = s[i]
    return ''.join(result)


yoyo = restoreString("codeleet", [4,5,6,7,0,2,1,3]) 

