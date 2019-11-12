# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:38:11 2019

@author: Nathan Richard
"""

import numpy as np
from math import floor


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
        
        
    K = np.array(K)
    return(-K)
    
def gen_square_posistion_matrix(N):
    
    
    if N%2 != 1:
        #checking if the value is odd
        raise Exception('N must be odd')
        '''So the matrix can be centered around zero'''
    
    if N == 1:
        a = 1
        return np.asarray([1]),np.asarray([1])
    else:
        a = floor(N/2)#gives me the exstent of the x vector
 
        x = np.linspace(-a,a,N)          
        y = x.copy()
        x = np.zeros((x.shape[0],1),dtype=x.dtype) + x
        y = x.transpose()
        return (x,y)