# -*- coding: UTF-8 -*-

import constantes
from clases import Cuerpo
from integrador import euler_step
import scipy as sp
import scipy.constants
import matplotlib.pyplot as plt

# inicializacion de condiciones iniciales

# El Sol estará en el origen de coordenadas
sol = Cuerpo(0, constantes.MASA_SOL, 0, 0, 0, 0, 0, 0, "Sol")
tierra = Cuerpo(1, constantes.MASA_TIERRA, sp.constants.astronomical_unit, 0, 0, -1E4, 3E4, 0, "Tierra")
jupiter = Cuerpo(2, constantes.MASA_JUPITER, 5.0 * sp.constants.astronomical_unit, 0, 0, 1.3E4, 0, 0, "Jupiter")

# Una hora en segundos
dt = 60. * 60.

# Integremos por un año (poco más) en steps de 1 hora

estrella1 = Cuerpo(0, constantes.MASA_SOL, -sp.constants.astronomical_unit/2, 0, 0, 0, 0, 0, "Estrella1")
estrella2 = Cuerpo(1, constantes.MASA_SOL/10000, sp.constants.astronomical_unit/2, 0, 0, 0, -1E4, 0, "Estrella2")

steps = 30000

#cuerpos = [sol, tierra]

cuerpos = [estrella1, estrella2]

historia_x1 = []
historia_y1 = []
historia_z1 = []
historia_vx1 = []
historia_vy1 = []
historia_vz1 = []

historia_x2 = []
historia_y2 = []
historia_z2 = []
historia_vx2 = []
historia_vy2 = []
historia_vz2 = []


while steps >= 0:
    euler_step(cuerpos, dt)
    if steps % 1000 == 0:
        print "Faltan %d steps " % (steps)
    historia_x1.append(estrella1.x)
    historia_y1.append(estrella1.y)
    historia_z1.append(estrella1.z)
    historia_vx1.append(estrella1.velocidad[0])
    historia_vy1.append(estrella1.velocidad[1])
    historia_vz1.append(estrella1.velocidad[2])

    historia_x2.append(estrella2.x)
    historia_y2.append(estrella2.y)
    historia_z2.append(estrella2.z)
    historia_vx2.append(estrella2.velocidad[0])
    historia_vy2.append(estrella2.velocidad[1])
    historia_vz2.append(estrella2.velocidad[2])

    steps -= 1

#fig = plt.figure("N Body")

plt.plot(historia_x1, historia_y1, 'r.')
plt.plot(historia_x2, historia_y2, 'g.')

plt.show()