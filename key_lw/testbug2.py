# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:14:18 2019

@author: HUAWEI
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

#BUG 2

def find_max(L):
    if len(L)==1:
        return (L[0])
    else:
        submax=find_max(L[1:len(L)])
        if submax<L[0]:
            max_L=L[0]
        else:
            max_L=submax
        return (max_L)

L=[1024,5,3,89,107,54,296,300] 
maxi = find_max(L)
print(maxi)
         
"""
Result: 5
"""






        