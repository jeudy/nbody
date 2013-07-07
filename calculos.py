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

def energia_cinetica(m, v):
    return 0.5 * m * (np.linalg.norm(v) ** 2)

# r es separacion entre ambas masas
def energia_potencial(mi, mj, r):
    return (-sp.constants.G * mi * mj) / np.linalg.norm(r)