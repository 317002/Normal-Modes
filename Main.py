# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:36:31 2019

@author: Nathan Richard
"""

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


#########################
####Defing the matrix####
#########################
N = 1

x = np.arange(-N,N + 1)
y = x.copy()


K = (np.diag(-4*np.ones(x.shape[0]**2)) + np.diag(([1,1,0]*x.shape[0])[:-1],1) + np.diag(([1,1,0]*x.shape[0])[:-1],-1) + \
np.diag(np.ones(x.shape[0]*2),3) + np.diag(np.ones(x.shape[0]*2),-3))*-1

x = np.zeros((x.shape[0],1),dtype=x.dtype) + x
y = x.transpose()

m = 1
#initial_x = np.ones(x.shape[0]**2)
initial_x = np.asarray([-.5,0,0,-.5,0,0,-.5,0,0])
A = K - m*np.diag(np.ones(x.shape[0]**2))

###########################
####Eigen Value Problem####
###########################
number = 10**3

t = np.linspace(0,100,number)

eigen_values,eigen_vectors = np.linalg.eigh(A)
eigen_vectors = eigen_vectors.transpose()

cn_vec = np.matmul(eigen_vectors,initial_x)
#cn_vec_test = np.dot(eigen_vectors.transpose()[0],initial_x)

time_component = np.asarray([c*np.exp(1j*sqrt(eig)*t) for eig,c in \
                             zip(eigen_values,cn_vec)])

final_components = np.matmul(eigen_vectors.transpose(),time_component)


#################
####Animating####
#################
fig, ax = plt.subplots(figsize = (12,12))


ax.set_xlim(-N - 2,N + 2)
ax.set_ylim(-N - 2,N + 2)

ax.grid()


box_vec = np.linspace(-N - 1,N + 1,4)
ones = np.ones(box_vec.shape)

bar_color = 'b'

ax.plot((N + 1)*ones,box_vec,color = bar_color)
ax.plot(-1*(N + 1)*ones,box_vec,color = bar_color)
ax.plot(box_vec,1*(N + 1)*ones,color = bar_color)
ax.plot(box_vec,-1*(N + 1)*ones,color = bar_color)

sc = ax.scatter(x,y,color = 'r')
ax.plot()




def convert(x,y):
    values = []
    for rowx,rowy in zip(x,y):
        for valuex,valuey in zip(rowx,rowy):
            value = [valuex,valuey]
            values.append(value)
    return values

values = convert(x,y)
values2 = convert(x,y)

zero_vec = np.zeros(final_components.shape).transpose()

def plot(a,x,y):
    print('Frame:' + str(a) + '//' + str(number))
    x_array = np.real(final_components).transpose()[a]
    y_array = x_array
    sc.set_offsets(np.asarray(values) + \
                   np.asarray([x_array,y_array]).transpose())


ani = animation.FuncAnimation(fig, plot, fargs=(x,y,),\
                              frames = number, interval=50) 

Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)

ani.save('line.mp4')


