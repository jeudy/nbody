# -*- coding: UTF-8 -*-

import constantes
from clases import Cuerpo
from integrador import euler_step
import scipy as sp
import scipy.constants
import matplotlib.pyplot as plt
from calculos import calcula_energia_total

# inicializacion de condiciones iniciales

# Un día en segundos
dt = 60. * 60. * 24.

# Condiciones iniciales
# El Sol estará en el origen de coordenadas y en reposo
sol = Cuerpo(0, constantes.MASA_SOL, 0, 0, 0, 0, 0, 0, "Sol")
# La Tierra estará a 1 UA y la velocidad inicial será el promedio de su velocidad orbital: ~29 km/s
tierra = Cuerpo(1, constantes.MASA_TIERRA, sp.constants.astronomical_unit, 0, 0, 0, 2.9E4, 0, "Tierra")
# Júpiter estará a 5 UA y la velocidad inicial será el promedio de su velocidad orbital: ~13 km/s
jupiter = Cuerpo(2, constantes.MASA_JUPITER, 5.0 * sp.constants.astronomical_unit, 0, 0, 0, 1.3E4, 0, "Jupiter")

# Integraremos la ecuación de movimiento por 11 años (aproximadamente, el periodo orbital de Jupiter
steps = 366 * 11

# Lista de cuerpos que componen el sistema
cuerpos = [sol, tierra, jupiter]

# Listas en memoria para guardar todos los datos de la evolución para luego graficarlos.

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

historia_x3 = []
historia_y3 = []
historia_z3 = []
historia_vx3 = []
historia_vy3 = []
historia_vz3 = []

# Guardamos la energia total al inicio de la simulación
# para verificar que al final el sistema conserve la energía
etot_inicial = calcula_energia_total(cuerpos)

while steps >= 0:
    euler_step(cuerpos, dt)
    # Mensaje para ir viendo el avance del proceso
    if steps % 1000 == 0:
        print "Faltan %d steps " % (steps)

    # En cada paso, guardamos los valores de posición y velocidad para graficarlos al final

    historia_x1.append(sol.x)
    historia_y1.append(sol.y)
    historia_z1.append(sol.z)
    historia_vx1.append(sol.vx)
    historia_vy1.append(sol.vy)
    historia_vz1.append(sol.vz)

    historia_x2.append(tierra.x)
    historia_y2.append(tierra.y)
    historia_z2.append(tierra.z)
    historia_vx2.append(tierra.vx)
    historia_vy2.append(tierra.vy)
    historia_vz2.append(tierra.vz)

    historia_x3.append(jupiter.x)
    historia_y3.append(jupiter.y)
    historia_z3.append(jupiter.z)
    historia_vx3.append(jupiter.vx)
    historia_vy3.append(jupiter.vy)
    historia_vz3.append(jupiter.vz)

    steps -= 1

etot_final = calcula_energia_total(cuerpos)
print "Energia total inicial: %s" % (str(etot_inicial))
print "Energia total final: %s" % (str(etot_final))


# Ploteo de las posiciones a lo largo de cada paso. Nos muestra las orbitas
plt.plot(historia_x1, historia_y1, 'r.')
plt.plot(historia_x2, historia_y2, 'g.')
plt.plot(historia_x3, historia_y3, 'b.')

plt.show()