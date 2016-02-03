#!/usr/bin/python
# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as mpl


def jl2(coef):
    part_1 = (position_matrix - np.dot(temps_matrix_transpose, coef)).transpose()
    part_2 =  position_matrix - np.dot(temps_matrix_transpose, coef)
    return np.dot(part_1,part_2).item(0)/N

coef = np.matrix('2;3') # O

position = np.loadtxt("p.txt")
temps = np.loadtxt("t.txt")

N = position.size

position_matrix = np.matrix(position).transpose() # Y

one_array = [1]*temps.size
temps_matrix = np.matrix(np.vstack((temps, one_array))) # X
temps_matrix_transpose = temps_matrix.transpose()

A_const = 100000.
B_const = 30.
C_const = 400.
min_diff = 0.00000001
t = 100.

def alpha_t(t):
    return A_const/(B_const+C_const*t)

def gradient_descent(teta_old, t):
    step_1 = np.dot(temps_matrix_transpose, teta_old)
    step_2 = np.dot(temps_matrix, (position_matrix - step_1))
    teta_new = teta_old + alpha_t(t) * step_2 / N
    return teta_new

teta_old = coef
teta_new = gradient_descent(teta_old, t)

list_jl2_teta = []

while abs(jl2(teta_new) - jl2(teta_old)) > min_diff:
    teta_old = teta_new
    t+=1
    teta_new = gradient_descent(teta_old, t)
    list_jl2_teta.append(jl2(teta_new))

print(teta_new)

mpl.plot(list_jl2_teta)
mpl.savefig("graph.jpeg")
