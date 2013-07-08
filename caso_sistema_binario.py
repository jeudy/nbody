# -*- coding: UTF-8 -*-

import constantes
from clases import Cuerpo
from integrador import euler_step
import scipy as sp
import scipy.constants
import matplotlib.pyplot as plt
from calculos import calcula_energia_total

# inicializacion de condiciones iniciales

# Una hora en segundos
dt = 60. * 60.

# Condiciones iniciales

estrella1 = Cuerpo(0, constantes.MASA_SOL/2, -3 * sp.constants.astronomical_unit, 0, 0, 0, 5E3, 0, "Estrella1")
estrella2 = Cuerpo(1, constantes.MASA_SOL/2, 3 * sp.constants.astronomical_unit, 0, 0, 0, -5E3, 0, "Estrella2")

# Integraremos la ecuación de movimiento por 10 años
# 10 años para estrellas genericas
steps = 366 * 10 * 24

# Lista de cuerpos que componen el sistema
cuerpos = [estrella1, estrella2]

# Listas en memoria para guardar todos los datos de la evolución para luego graficarlos.

historia_x1 = []
historia_y1 = []
historia_z1 = []

historia_x2 = []
historia_y2 = []
historia_z2 = []

save_every = 10

# Guardamos la energia total al inicio de la simulación
# para verificar que al final el sistema conserve la energía
etot_inicial = calcula_energia_total(cuerpos)

while steps >= 0:
    euler_step(cuerpos, dt)
    # Mensaje para ir viendo el avance del proceso
    if steps % 1000 == 0:
        print "Faltan %d steps " % (steps)

    # En cada paso, guardamos los valores de posición y velocidad para graficarlos al final

    if steps % save_every == 0:
        historia_x1.append(estrella1.x)
        historia_y1.append(estrella1.y)
        historia_z1.append(estrella1.z)

        historia_x2.append(estrella2.x)
        historia_y2.append(estrella2.y)
        historia_z2.append(estrella2.z)

    steps -= 1

etot_final = calcula_energia_total(cuerpos)
print "Energia total inicial: %s" % (str(etot_inicial))
print "Energia total final: %s" % (str(etot_final))

# Ploteo de las posiciones a lo largo de cada paso. Nos muestra las orbitas
plt.plot(historia_x1, historia_y1, 'r.')
plt.plot(historia_x2, historia_y2, 'g.')

plt.show()