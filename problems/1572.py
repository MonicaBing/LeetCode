#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""



    
def diagonalSum(mat):
    
    result, n = 0,len(mat)
    
    for i in range (0, n):
        result += mat[i][i] + mat[i][n-1-i]
        
        if i == n-1-i:
            result -= mat[i][i]
    return result



final = diagonalSum([[1,2,3],
[4,5,6],
[7,8,9]])
