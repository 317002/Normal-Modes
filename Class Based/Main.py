# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:56:12 2019

@author: Nathan Richard
"""



###############
####IMPORTS####
###############
import mylib as my
from mylib import np
from math import floor
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
        y = np.flip(x).transpose()
        return (x,y)


class grid:
    
    def __init__(self,x_m,y_m,initial_p,m = None,k = 1):
        self.x_m = x_m
        self.y_m = y_m
        self.initial_p = np.asarray(initial_p)
        #generating the k matrix
        self.K = my.gen_k(x_m.shape[0])
        #generating the mass matrix
        if m == None:
            self.M = np.zeros(self.K.shape)
        else:
            #assuming m is a vector value coresponding to each mass
            self.M = np.diag(m)
            if self.K.shape != self.M.shape:
                raise Exception('Incorect number of masses')

        if self.K.shape[0] != self.initial_p.shape[0]:
            raise Exception('Incorect number of initial posistions')
    
    def gen_basis(self,t):
        self.A = self.K - self.M#K - w^2M matrix
        #gathering the eigen value and eigen vectors for the K - w^2M matrix
        eigen_values,eigen_vectors = np.linalg.eigh(self.A)
        
        #this methode dosent work for negative eigen modes
        if np.any(eigen_values < 0):
            raise Exception('Negative Eigen Values')
            
        self.omegas = np.sqrt(eigen_values)#should all be real
        #makes it easier to handle
        self.eigen_vectors = np.transpose(eigen_vectors)
#        self.cn = [np.dot(eig,self.initial_p) for eig in \
#                             self.eigen_vectors]#find the cn values
        self.cn = np.matmul(self.eigen_vectors,self.initial_p)
        
        self.time_component = np.asarray([c*np.exp(1j*omg*t) for \
                                          omg,c in \
                             zip(self.omegas,self.cn)])
        '''
        vectors = []
        for time in self.time_component:
            for eig_vec in self.eigen_vectors:
                vec = np.asarray([np.real(a*time) for a in eig_vec])
                vectors.append(vec)
                
        self.vecctors = vectors
        '''
        self.final_component = np.matmul(eigen_vectors,self.time_component)

#        self.final_components = np.matmul(eigen_vectors.transpose(),time_component)
        
        
        

        

        
n = 21
x,y = gen_square_posistion_matrix(n)
t = np.linspace(0,100,10**3)

row_count = 2

a = [0]*(n**2 - n*row_count)
a.extend([1]*n*row_count)

#a = np.random.randn(n**2)*.1

matrix = grid(x,y,a,[.001]*n**2)
matrix.gen_basis(t)

#################
####Animating####
#################
number = 500

fig, ax = plt.subplots(figsize = (12,12))


N=floor(n/2)

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
ax.set_title('size:' + str(matrix.x_m.shape),fontsize = 20)




def convert(x,y):
    values = []
    for rowx,rowy in zip(x,y):
        for valuex,valuey in zip(rowx,rowy):
            value = [valuex,valuey]
            values.append(value)
    return values

values = convert(x,y)
values2 = convert(x,y)

zero_vec = np.zeros(matrix.final_component.shape).transpose()

def plot(a,x,y):
    print('Frame:' + str(a) + '//' + str(number))
    x_array = np.real(matrix.final_component).transpose()[a]
    y_array = zero_vec[a]
    sc.set_offsets(np.asarray(values) + \
                   np.asarray([x_array,y_array]).transpose())


ani = animation.FuncAnimation(fig, plot, fargs=(x,y,),\
                              frames = number, interval=50) 

Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)

ani.save('line.mp4')
    
    
    
    
    
    
    
    
    