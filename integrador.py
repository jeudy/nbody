# -*- coding: UTF-8 -*-

from calculos import aceleracion_gravitacional
import numpy as np

# Método de Euler
# dt en segundos


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

# Metodo Leapfrog
# dt en segundos

def leapfrog_step(cuerpos, aceleraciones, dt):
    i = 0

    velocidades = []

    for cuerpo in cuerpos:
        velocity_half = cuerpo['velocidad'] + (aceleraciones[i] * (dt / 2.))
        velocidades.insert(i, velocity_half)
        cuerpo['posicion'] += (velocity_half * dt)
        i += 1

    i = 0
    for cuerpo in cuerpos:
        # Calculo las aceleraciones para el i + 1 basado en la nueva posicion
        aceleraciones[i] = calcular_aceleracion(cuerpo, cuerpos)
        cuerpo['velocidad'] = velocidades[i] + (aceleraciones[i] * (dt / 2.))
        i += 1