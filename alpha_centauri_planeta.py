# -*- coding: UTF-8 -*-

import constantes
from clases import Cuerpo
from integrador import euler_step
import scipy as sp
import scipy.constants
import matplotlib.pyplot as plt
from calculos import calcula_energia_total

# inicializacion de condiciones iniciales

# Un dia en segundos
# OJO, cambiar a mas pequeño y ver valor de conservacion de energia
dt = 60. * 60. * 24

# Condiciones iniciales

estrella1 = Cuerpo(0, constantes.MASA_SOL*1.09, -10.9 * sp.constants.astronomical_unit, 0, 0, 0, 2.1E3, 0, "Alpha Centauri A")
estrella2 = Cuerpo(1, constantes.MASA_SOL*0.9, 12.8 * sp.constants.astronomical_unit, 0, 0, 0, -2.1E3, 0, "Alpha Centauri B")
planeta = Cuerpo(2, constantes.MASA_TIERRA, -9.9 * sp.constants.astronomical_unit, 0, 0, 0, -3.1E4, 0, "Planeta")

steps = 366 * 50

# Lista de cuerpos que componen el sistema
cuerpos = [estrella1, estrella2, planeta]

# Listas en memoria para guardar todos los datos de la evolución para luego graficarlos.

historia_x1 = []
historia_y1 = []
historia_z1 = []

historia_x2 = []
historia_y2 = []
historia_z2 = []

historia_x3 = []
historia_y3 = []
historia_z3 = []

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

        historia_x3.append(planeta.x)
        historia_y3.append(planeta.y)
        historia_z3.append(planeta.z)

    steps -= 1

etot_final = calcula_energia_total(cuerpos)
print "Energia total inicial: %s" % (str(etot_inicial))
print "Energia total final: %s" % (str(etot_final))

# Ploteo de las posiciones a lo largo de cada paso. Nos muestra las orbitas
plt.plot(historia_x1, historia_y1, 'r.')
plt.plot(historia_x2, historia_y2, 'g.')
plt.plot(historia_x3, historia_y3, 'b.')

plt.show()