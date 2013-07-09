# -*- coding: UTF-8 -*-

import constantes
from clases import Cuerpo
from integrador import euler_step
import scipy as sp
import scipy.constants
import matplotlib.pyplot as plt
from calculos import calcula_energia_total

from matplotlib import animation

# inicializacion de condiciones iniciales

# Un dia en segundos
# OJO, cambiar a mas pequeño y ver valor de conservacion de energia
dt = 60. * 60. * 24

# Condiciones iniciales

estrella1 = Cuerpo(0, constantes.MASA_SOL*1.09, -10.9 * sp.constants.astronomical_unit, 0, 0, 0, 2.1E3, 0, "Alpha Centauri A")
estrella2 = Cuerpo(1, constantes.MASA_SOL*0.9, 12.8 * sp.constants.astronomical_unit, 0, 0, 0, -2.1E3, 0, "Alpha Centauri B")
planeta = Cuerpo(2, constantes.MASA_TIERRA, -9.9 * sp.constants.astronomical_unit, 0, 0, 0, -3.1E4, 0, "Planeta")

steps = 366 * 150

original_steps = 366 * 150

# Lista de cuerpos que componen el sistema
cuerpos = [estrella1, estrella2, planeta]

# Listas en memoria para guardar todos los datos de la evolución para luego graficarlos.

guarde_cada = 25

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

fig = plt.figure("N Bdy")
ax = fig.add_subplot(111, title='N Body')
#ax = plt.axes(projection='3d')

x = [estrella1.x, estrella2.x, planeta.x]
y = [estrella1.y, estrella2.y, planeta.y]

sp, = ax.plot(x, y, 'r.')

ax.set_ylim(-10, 10)
ax.set_xlim(-15, 15)

while steps >= 0:
    euler_step(cuerpos, dt)
    # Mensaje para ir viendo el avance del proceso
    if steps % 1000 == 0:
        print "Faltan %d steps " % (steps)

    # En cada paso, guardamos los valores de posición y velocidad para graficarlos al final

    if steps % guarde_cada == 0:

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

def update(i):
    x = [historia_x1[i], historia_x2[i], historia_x3[i]]
    y = [historia_y1[i], historia_y2[i], historia_y3[i]]
    sp.set_data(x, y)
    return sp,

ani = animation.FuncAnimation(fig, update, frames=original_steps/guarde_cada, repeat=False)

plt.show()

# Guarda la animación en un video avi

ani.save("movie.avi", codec='avi')