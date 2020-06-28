#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:01:01 2020

@author: kathykiutang
"""



def longestPalindrome(s):
    if len(s) == 1:
        print("1")
        return s
    else:
        final = ""
        
        for i in range (len(s)):
            j = i+1
            
            while j <= len(s) and len(final) <= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(final) < len(s[i:j]):
                    final = s[i:j]
                
                j += 1
            
            
        return final


ans = longestPalindrome("bb")



    
        
