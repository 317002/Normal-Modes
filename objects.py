# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:08:45 2019

@author: Nathan Richard
"""


'''Imports'''
import numpy as np


def gen_spring_line(particle,spring):
    vecs = []
    for p,o in zip(particle.posistion,spring.orientation):
        vecs.append(np.linspace(p,p + o*spring.l,2))
    return(vecs)



class particle:
    def __init__(self,m,posistion,springs):
        self.m = m
        self.posistion = posistion#the posistion of the particle
        self.springs = springs


class spring:
    def __init__(self,k,l,orientation,posistion):
        self.k = k#spring constant
        self.l = l#lenght of the spring
        self.orientation = orientation#[x,y,z] Ex: [1,0,0]#unit vectors
        self.posistion = posistion
    
    def get_potential(self,x):
        return 1/2*(self.k*x**2)
        



        
        
