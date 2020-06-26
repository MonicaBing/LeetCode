#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:07:39 2020

"""

def lengthOfLongestSubstring(s):
    
    final = ""
    temp = ""
    
    for i in range (len(s)):
        if s[i] not in final:
            final += s[i] 
        else: #  repeat
            if len(temp)<len(final):
                temp = final
                final = final[final.index(s[i])+1::] + s[i]
    
    return max(len(temp), len(final))
    
    
    
lengthOfLongestSubstring("abcabcbb")

lengthOfLongestSubstring("bbbbb")

lengthOfLongestSubstring("pwwkew")

            
            
        