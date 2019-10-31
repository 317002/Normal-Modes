# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:08:45 2019

@author: Nathan Richard
"""


'''Imports'''
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as alg




class spring:
    def __init__(self,k,d,orientation):
        self.k = k#spring constant
        self.d = d#lenght of the spring
        self.orientation = orientation#[x,y,z] Ex: [1,1,-1]#unit vectors
    
    def get_potential(self,x):
        return 1/2*(self.k*x**2)
        

class partical:
    def __init__(self,m,springs):
        self.m = m
        self.springs = springs#a list of spring objects
        
        
