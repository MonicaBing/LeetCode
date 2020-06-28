#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:37:51 2020

@author: kathykiutang
"""


def twoSum(nums, target):
    for i in range (len(nums)):
        for j in range (len(nums)):
            if nums[j] == nums[i]:
                break
            else:
                result = nums[i]+nums[j]
            if result == target:
                final_i = i
                final_j = j
    return [final_i, final_j]

twoSum([2,7,11,15],9)