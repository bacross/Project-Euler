# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 10:17:38 2017

@author: bacro
"""

nums = [x for x in range(1,1000)]
        
nsum = sum(nums[i] for i in range(len(nums)) if nums[i]%3==0 or nums[i]%5==0)