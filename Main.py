# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:36:31 2019

@author: Nathan Richard
"""

import numpy as np
import matplotlib.pyplot as plt
import objects as my



#contants
N = 3#should be odd
bounds = [-10,10]
#test_spring = my.spring(1,.5,[1,0,0],[0,0,0])
#test_mass = my.particle(1,[0,0,0])




###########################
####Defining the figure####
###########################

fig = plt.figure(figsize = (12,12))
ax = fig.add_subplot(111)


'''setting the bounds of the graph'''
ax.set_xlim(bounds)
ax.set_ylim(bounds)


################################
####Generating the locations####
################################

x = np.arange(-N,N + 1)
y = x.copy()


x = np.zeros((x.shape[0],1),dtype=x.dtype) + x
y = x.transpose()
z = np.zeros(x.shape)*0

ax.scatter(x,y)




################################
#####Generating the springs#####
################################




################################
####Generating the particles####
################################




#particles = []
#for line1,line2,line3 in zip(x,y,z):
#    for q1,q2,q3 in zip(line1,line2,line3):
#        part = my.particle(1,[q1,q2,q3])
#        particles.append(part)
#        ax.scatter(*part.posistion[0:2])


    
















