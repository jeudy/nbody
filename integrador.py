# -*- coding: UTF-8 -*-

from calculos import aceleracion_gravitacional
import numpy as np

# Método de Euler
# dt en segundos

# r_i+1 = r_i * v_i
# v_i+1 =

def euler_step(cuerpos, dt):
    for cuerpo in cuerpos:
        cuerpo['posicion'] += cuerpo['velocidad'] * dt
        aceleracion = calcular_aceleracion(cuerpo, cuerpos)
        cuerpo['velocidad'] += aceleracion * dt

def calcular_aceleracion(cuerpo, cuerpos):
    aceleracion = 0.0
    for c in cuerpos:
        if np.any(cuerpo['posicion'] != c['posicion']):
            aceleracion += aceleracion_gravitacional(cuerpo['posicion'], c['posicion'], c['masa'])
    return aceleracion