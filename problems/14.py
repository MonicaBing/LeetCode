#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:59:55 2020

"""

def longestCommonPrefix(strs):
    
    #  number of words
    num_words = len(strs)
    
    for i in range (len(strs)):
        strs[i] = list(strs[i])
    
    # cut at min length 
    temp = []
    
    for i in range (len(strs)):
        temp += str(len(strs[i]))
        
    min_length = int(min(temp))
    
    for i in range (len(strs)):
        strs[i] = strs[i][:min_length]
    
    score = 0
    final_score = 10000000000
    
    # comparsion
    for i in range (num_words-1):
        for j in range (min_length):
    
            if strs[i][j] == strs[i+1][j]:
                score += 1
            else:
                break
        
        if score < final_score:
            final_score = score
        else:
            final_score = score
        score = 0
    
    if final_score == 0:
        return ''
    else:
        return str("".join(strs[0][:final_score]))
    
words = longestCommonPrefix(['flower', 'flow', 'flight'])

