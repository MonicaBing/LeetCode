#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
def countOdds(low, high):
    return (high-low+2)//2 - int(low%2==high%2==0)

final = countOdds(8, 10)

    