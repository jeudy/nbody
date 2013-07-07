# -*- coding: UTF-8 -*-

from clases import Cuerpo
from calculos import aceleracion_gravitacional

# Método de Euler
# dt en segundos

# r_i+1 = r_i * v_i
# v_i+1 =

def euler_step(cuerpos, dt):
    for cuerpo in cuerpos:
        cuerpo.posicion += cuerpo.velocidad * dt
        aceleracion = calcular_aceleracion(cuerpo, cuerpos)
        cuerpo.velocidad += aceleracion * dt

def calcular_aceleracion(cuerpo, cuerpos):
    aceleracion = 0.0
    for c in cuerpos:
        if cuerpo != c:
            aceleracion += aceleracion_gravitacional(cuerpo.posicion, c.posicion, c.masa)
    return aceleracion