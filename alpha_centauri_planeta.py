# -*- coding: UTF-8 -*-

import constantes
from integrador import euler_step
import scipy as sp
import numpy as np
import scipy.constants
import matplotlib.pyplot as plt
from calculos import calcula_energia_total
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# inicializacion de condiciones iniciales


visualizacion = raw_input("Como desea visualizar resultados? estatico o animado? ")

# OJO, cambiar a mas pequeño y ver valor de conservacion de energia
dt = 60. * 60. * 24.

# Condiciones iniciales

estrella1 = {'masa': constantes.MASA_SOL*1.09,
             'posicion': np.array([-10.9 * sp.constants.astronomical_unit, 0, 0]),
             'velocidad': np.array([0, 2.1E3, 0]),
             'nombre': "Alpha Centauri A"}

estrella2 = {'masa': constantes.MASA_SOL*0.9,
             'posicion': np.array([12.8 * sp.constants.astronomical_unit, 0, 0]),
             'velocidad': np.array([0, -2.1E3, 0]),
             'nombre': "Alpha Centauri B"}

planeta = {'masa': constantes.MASA_TIERRA,
           'posicion': np.array([-9.9 * sp.constants.astronomical_unit, 0, 0]),
           'velocidad': np.array([0, -3.1E4, 0]),
           'nombre': "Planeta"}

# 150 años
steps = 366 * 150

# Lista de cuerpos que componen el sistema
cuerpos = [estrella1, estrella2, planeta]

# Listas en memoria para guardar todos los datos de la evolución para luego graficarlos.

guarde_cada = 50

historia_x1 = []
historia_y1 = []
historia_z1 = []

historia_x2 = []
historia_y2 = []
historia_z2 = []

historia_x3 = []
historia_y3 = []
historia_z3 = []

# Guardamos la energia total al inicio de la simulación
# para verificar que al final el sistema conserve la energía
etot_inicial = calcula_energia_total(cuerpos)

while steps >= 0:
    euler_step(cuerpos, dt)
    # Mensaje para ir viendo el avance del proceso
    if steps % 1000 == 0:
        print "Faltan %d steps " % (steps)

    # En cada paso, guardamos los valores de posición y velocidad para graficarlos al final

    if steps % guarde_cada == 0:

        historia_x1.append(estrella1['posicion'][0])
        historia_y1.append(estrella1['posicion'][1])
        historia_z1.append(estrella1['posicion'][2])

        historia_x2.append(estrella2['posicion'][0])
        historia_y2.append(estrella2['posicion'][1])
        historia_z2.append(estrella2['posicion'][2])

        historia_x3.append(planeta['posicion'][0])
        historia_y3.append(planeta['posicion'][1])
        historia_z3.append(planeta['posicion'][2])

    steps -= 1

etot_final = calcula_energia_total(cuerpos)
print "Energia total inicial: %s" % (str(etot_inicial))
print "Energia total final: %s" % (str(etot_final))


if visualizacion.lower() == 'estatico':
    plt.plot(historia_x1, historia_y1, 'r.')
    plt.plot(historia_x2, historia_y2, 'g.')
    plt.plot(historia_x3, historia_y3, 'b.')
    #
    plt.show()
else:
    fig = plt.figure("Alfa Centauri")

    ax = plt.axes(projection='3d')

    # Dibujo el origen de coordenadas. Ejercicio: centro de masa del sistema
    ax.plot([0], [0], [0], 'g+')

    sp, = ax.plot([], [], [], 'r.')

    ax.set_ylim(min([min(historia_y1), min(historia_y2), min(historia_y3)]),
                max([max(historia_y1), max(historia_y2), max(historia_y3)]))

    ax.set_xlim(min([min(historia_x1), min(historia_x2), min(historia_x3)]),
                max([max(historia_x1), max(historia_x2), max(historia_x3)]))

    ax.set_zlim(min([min(historia_z1), min(historia_z2), min(historia_z3)]),
                max([max(historia_z1), max(historia_z2), max(historia_z3)]))

    def update(i):
        x = [historia_x1[i], historia_x2[i], historia_x3[i]]
        y = [historia_y1[i], historia_y2[i], historia_y3[i]]
        z = [historia_z1[i], historia_z2[i], historia_z3[i]]
        sp.set_data(x, y)
        sp.set_3d_properties(z)
        return sp,

    # Creacion de la animación, 100 frames signifca que cada 100 ms
    # llama a update con un valor entre 0 y 99
    # Con repeat = False hace que solo se dibujen los frames una vez
    ani = animation.FuncAnimation(fig, update, frames=len(historia_x1), interval=20, repeat=False)
    plt.show()

