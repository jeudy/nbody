# -*- coding: UTF-8 -*-

import constantes
from integrador import euler_step
import scipy as sp
import numpy as np
import scipy.constants
import matplotlib.pyplot as plt
from calculos import calcula_energia_total

# inicializacion de condiciones iniciales

# Un minuto
dt = 60

# Condiciones iniciales
# La estrella estará en el origen de coordenadas y en reposo
estrella = {'masa': constantes.MASA_SOL,
             'posicion': np.array([0., 0., 0.]),
             'velocidad': np.array([0., 0., 0.])}
# Datos aproximadamente como 51 Pegasi
hot_jupiter = {'masa': constantes.MASA_JUPITER,
             'posicion': np.array([0.05 * sp.constants.astronomical_unit, 0., 0.]),
             'velocidad': np.array([0., 106E3, 0.])}

# 5 Dias
steps = 24 * 5 * 60

# Lista de cuerpos que componen el sistema
cuerpos = [estrella, hot_jupiter]

# Listas en memoria para guardar todos los datos de la evolución para luego graficarlos.

historia_x1 = []
historia_y1 = []
historia_z1 = []

historia_x2 = []
historia_y2 = []
historia_z2 = []

# Guardamos la energia total al inicio de la simulación
# para verificar que al final el sistema conserve la energía
etot_inicial = calcula_energia_total(cuerpos)

while steps >= 0:
    euler_step(cuerpos, dt)
    # Mensaje para ir viendo el avance del proceso
    if steps % 1000 == 0:
        print "Faltan %d steps " % (steps)

    # En cada paso, guardamos los valores de posición y velocidad para graficarlos al final

    historia_x1.append(estrella['posicion'][0])
    historia_y1.append(estrella['posicion'][1])
    historia_z1.append(estrella['posicion'][2])

    historia_x2.append(hot_jupiter['posicion'][0])
    historia_y2.append(hot_jupiter['posicion'][1])
    historia_z2.append(hot_jupiter['posicion'][2])

    steps -= 1

etot_final = calcula_energia_total(cuerpos)
print "Energia total inicial: %s" % (str(etot_inicial))
print "Energia total final: %s" % (str(etot_final))

# Ploteo de las posiciones a lo largo de cada paso. Nos muestra las orbitas
plt.plot(historia_x1, historia_y1, 'r.')
plt.plot(historia_x2, historia_y2, 'g.')

plt.show()