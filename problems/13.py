#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:02:03 2020

"""



    
def romanToInt(s):
    
    roman_convert = {
      'I':1,
      'V':5,
      'X':10,
      'L':50 ,
      'C':100 ,
      'D':500,
      'M':1000,
      'IV' :4,
      'IX' :9,
      'XL' : 40,
      'XC':90,
      'CD': 400,
      'CM': 900
      }

    s = list(s)
    i = 0 
    value = 0
    result = 0
    
    while i < len(s):
        print(i)
        
        if i < len(s)-1:
            first= [s[i],s[i+1]]
            combine = "".join(first)
            
        if combine in roman_convert:  # find in the dictionary
            value = roman_convert[combine]
            i += 2
            combine = 0
        else:
            value = roman_convert[s[i]]
            i += 1
            
        result += value
        
    return result

result = romanToInt('IV')
