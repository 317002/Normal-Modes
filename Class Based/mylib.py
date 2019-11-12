# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:56:42 2019

@author: Nathan Richard
"""

import numpy as np


n = 4


def gen_k(n):
    index = []
    ind = []
    
    for i in range(0,n+2):
        ind += [0]
    for i in range(0,n+2):
        index += [ind]
    
    for i in range(0,len(index)):
        for j in range(0,len(index)):
            index[i][j] = n**2
            
    index = np.array(index)
    
    c = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            index[i][j] = c
            c += 1
            
    K = []        
    for i in range(1,n+1):
        for j in range(1,n+1):
            
        
            m = []
            for l in range(0,n**2+1):
                m += [0]
        
            m[index[i][j]] = -4
            m[index[i+1][j]] = 1
            m[index[i-1][j]] = 1
            m[index[i][j+1]] = 1
            m[index[i][j-1]] = 1
        
            K += [m[:-1]]
        
        
    return -np.array(K)
