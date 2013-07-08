# -*- coding: UTF-8 -*-

import constantes
from clases import Cuerpo
from integrador import euler_step
import scipy as sp
import scipy.constants
import matplotlib.pyplot as plt
from calculos import calcula_energia_total

# inicializacion de condiciones iniciales

# Un minuto
dt = 60

# Condiciones iniciales
# La estrella estará en el origen de coordenadas y en reposo
estrella = Cuerpo(0, constantes.MASA_SOL, 0, 0, 0, 0, 0, 0, "Estrella")
# Datos aproximadamente como 51 Pegasi
hot_jupiter = Cuerpo(1, 0.47 * constantes.MASA_JUPITER, 0.05 * sp.constants.astronomical_unit, 0, 0, 0, 106E3, 0, "Jupiter")

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

    historia_x1.append(estrella.x)
    historia_y1.append(estrella.y)
    historia_z1.append(estrella.z)

    historia_x2.append(hot_jupiter.x)
    historia_y2.append(hot_jupiter.y)
    historia_z2.append(hot_jupiter.z)

    steps -= 1

etot_final = calcula_energia_total(cuerpos)
print "Energia total inicial: %s" % (str(etot_inicial))
print "Energia total final: %s" % (str(etot_final))

# Ploteo de las posiciones a lo largo de cada paso. Nos muestra las orbitas
plt.plot(historia_x1, historia_y1, 'r.')
plt.plot(historia_x2, historia_y2, 'g.')

plt.show()