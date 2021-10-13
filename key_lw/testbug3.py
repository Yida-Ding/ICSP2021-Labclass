# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:21:15 2019

@author: HUAWEI
"""

#BUG 3
def find_max(L):
    max_L=L[0]
    i=0
    while i<len(L):
        if max_L<L[i]:
            max_L=L[i]
            i=i+1
    return (max_L)
L=[4,6,2,5,7]
print (find_max(L))
"""
Result: 7
"""