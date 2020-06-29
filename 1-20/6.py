#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:21:29 2020

@author: kathykiutang
"""

def convert (s,numRows):
    line = 0
    pl = 1
    
    output = [""]*numRows
    
    for i in range (len(s)): # for every letter
        output[line] += s[i]
        
        if numRows > 1:
            line += pl
            
            if line == 0 or line == numRows -1 :  # change direction ehaad tail 
                pl *= -1
                
    
    final = ""
    
    for i in range (numRows):
        final += output[i]
        
    return final





convert("PAYPALISHIRING", 3)