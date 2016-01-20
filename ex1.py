#!/usr/bin/python
# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as mpl


position = np.loadtxt("p.txt")
temps = np.loadtxt("t.txt")
mpl.plot(position, temps, ".")

y = 2*temps+3
mpl.plot(y, temps)

mpl.savefig("graph.jpeg")

N = position.size

Jabs = sum(abs(position-y))/N
print("Jabs: \t\t" + str(Jabs))

# Jl1_test = (sum((position-y)**2)**(0.5))/N
# print("Jl1_test: \t" + str(Jl1_test))

# Jl2_test = sum((position-y)**2)/N
# print("Jl2_test: \t" + str(Jl2_test))

coef = np.matrix('2;3') # O

position_matrix = np.matrix(position).transpose() # y

one_array = [1]*temps.size
temps_matrix_transpose = np.matrix(np.vstack((one_array, temps))).transpose() # Xt

part_1 = (position_matrix - np.dot(temps_matrix_transpose, coef)).transpose()
part_2 =  position_matrix - np.dot(temps_matrix_transpose, coef)

JL1 = np.dot(part_1,part_2).item(0)**0.5/N
print("JL1: \t\t" + str(JL1))

Jl2 = np.dot(part_1,part_2).item(0)/N
print("JL2: \t\t" + str(Jl2))

Jlinf = max(position-y)
print("Jlinf: \t\t" + str(Jlinf))
