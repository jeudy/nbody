# -*- coding: UTF-8 -*-

__author__ = 'jeudy'

import scipy as sp
import scipy.constants
import numpy as np


# Ecuacion de movimiento

# Aceleracion sobre particula i, ejercida por particula j
# La magnitud del vector se calcula con np.linalg.norm


def aceleracion_gravitacional(ri, rj, mj):
    diff = rj - ri
    return sp.constants.G * mj * (diff / (np.linalg.norm(diff) ** 3))

# Calculo de energia cinética


def energia_cinetica(m, v):
    return 0.5 * m * (np.linalg.norm(v) ** 2)

# Energía potencial gravitacional para 2 cuerpos
# r es separacion entre ambas masas


def energia_potencial(mi, mj, ri, rj):
    diff = rj - ri
    return (-sp.constants.G * mi * mj) / np.linalg.norm(diff)

#Calculo de la energia total: cinetica + potencial

def calcula_energia_total(cuerpos):
    ekin = 0
    epot = 0
    for cuerpo in cuerpos:
        ekin += energia_cinetica(cuerpo.masa, cuerpo.velocidad)
        for c in cuerpos:
            if cuerpo != c:
                epot += energia_potencial(cuerpo.masa, c.masa, cuerpo.posicion, c.posicion)

    #Se divide entre 2 porque el aporte de cada particula se calculó 2 veces
    epot /= 2

    return ekin + epot