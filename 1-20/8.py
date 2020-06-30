#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:40:21 2020

"""

def myAtoi(str):
    
    lower = -2**31
    upper = 2**31 - 1
    polar = 1
    point = 0
    
    temp = list("".join(str))
    
    
    
    if temp[0].isdigit() == 0 and temp[0] != '-' and temp[0] != ' ':
        return 0
    else:
        
        no_space = [s for s in temp if s != ' ']
     
        
        if no_space[0] == '-':
            polar = -1
            
        for i in range (len(no_space)):
            if no_space[i] == '.':
                point += 1
        
        if point != 0:
            return (int("".join(no_space[0:no_space.index('.')])))
            
        else:
        
        
        
            new_temp  = [s for s in no_space if s.isdigit()]    
            
            final = polar*int("".join(new_temp))
            
            if final > upper:
                print('1')
                return upper
        
            if final < lower:
                print('2')
                return lower
        
            if final < upper and final > lower:
                print('3')
                return final



ans = myAtoi('    42')
