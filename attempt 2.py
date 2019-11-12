# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 14:37:28 2019

@author: Nathan Richard
"""


import matplotlib.pyplot as plt
import basic_functions as my
from basic_functions import np
from math import sqrt
import matplotlib.animation as animation

number = 1000

n = 3

x,y = my.gen_square_posistion_matrix(n)

K = my.gen_k(abs(x.shape[0]))
M = np.diag(np.ones(x.shape[0]**2)*.1)
A = K-M
eigen_values,eigen_vectors = np.linalg.eigh(A)
eigen_vectors = eigen_vectors.transpose()

initial_posistion = [1]*9
cn_vec = [np.dot(vec,initial_posistion) for vec in eigen_vectors]

t = np.linspace(0,10,number)

time_vectors = np.asarray([cn*np.exp(1j*sqrt(eig_val)*t) for cn,eig_val in \
                           zip(cn_vec,eigen_values)])


for vec in posisition_time_vectors:
    plt.plot(t,vec)