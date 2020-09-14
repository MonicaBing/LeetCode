#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:44:20 2020

"""

def isPalindrome(x):
    
    number = str(x)
    reverse = number[::-1]
    
    if number == reverse:
        return True
    else:
        return False
    
result = isPalindrome(10)