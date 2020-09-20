#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
def canConstruct(ransomNote, magazine):
    
    if not ransomNote.strip():
        if len(magazine) != 0 :
            return True 
        if not magazine.strip():
            return True

    if not magazine.strip():
        if len(ransomNote) != 0:
            return False
    
    magazine = sorted(magazine)
    ransomNote = sorted(ransomNote)
    
    end = len(ransomNote)

    start = 0
    count = 0
    
    for i in range (0,len(magazine)):
        print(i)
        if magazine[i] == ransomNote[start]:
            count += 1
            start += 1
        if count == end:
            return True
        
    return False

final = canConstruct(" ", "a")