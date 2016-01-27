#!/usr/bin/python
# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as mpl


def calc_errors(coef):
    y = coef.item(0)*temps+coef.item(1)
    mpl.plot(y, temps, label= u'\u0398\u2081: '+ str(coef.item(0)) + u'\t\u0398\u2082: ' + str(coef.item(1)))
    
    Jabs = sum(abs(position-y))/N
    print("Jabs: \t\t" + str(Jabs))

    # Jl1_test = (sum((position-y)**2)**(0.5))/N
    # print("Jl1_test: \t" + str(Jl1_test))

    # Jl2_test = sum((position-y)**2)/N
    # print("Jl2_test: \t" + str(Jl2_test))

    part_1 = (position_matrix - np.dot(temps_matrix_transpose, coef)).transpose()
    part_2 =  position_matrix - np.dot(temps_matrix_transpose, coef)

    JL1 = np.dot(part_1,part_2).item(0)**0.5/N
    print("JL1: \t\t" + str(JL1))

    Jl2 = np.dot(part_1,part_2).item(0)/N
    print("JL2: \t\t" + str(Jl2))

    Jlinf = max(abs(position-y))
    print("Jlinf: \t\t" + str(Jlinf))

coef = np.matrix('2;3') # O

position = np.loadtxt("p.txt")
temps = np.loadtxt("t.txt")
mpl.plot(position, temps, ".")

N = position.size

position_matrix = np.matrix(position).transpose() # y

one_array = [1]*temps.size
temps_matrix = np.matrix(np.vstack((temps, one_array))) # X
temps_matrix_transpose = temps_matrix.transpose()

calc_errors(coef)

teta_part_one = np.dot(temps_matrix, temps_matrix_transpose)**(-1)
teta_part_two = np.dot(temps_matrix, position_matrix)

teta = np.dot(teta_part_one, teta_part_two)

print("Teta: " + str(teta))

calc_errors(teta)

mpl.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)
mpl.savefig("graph.jpeg")
