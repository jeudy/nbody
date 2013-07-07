# -*- coding: UTF-8 -*-

__author__ = 'jeudy'

import numpy as np
import constantes
import scipy as sp
import scipy.constants

class Cuerpo(object):

    # Constructor de la clase

    def __init__(self, _indice, _masa, _x, _y, _z, _vx, _vy, _vz, _nombre="Cuerpo generico"):
        self.__indice = _indice
        self.masa = _masa
        self.posicion = np.array([_x, _y, _z])
        self.velocidad = np.array([_vx, _vy, _vz])
        self.nombre = _nombre


    # Definición de propiedades con valores normalizados
    @property
    def x(self):
        return self.posicion[0] / sp.constants.astronomical_unit

    @property
    def y(self):
        return self.posicion[1] / sp.constants.astronomical_unit

    @property
    def z(self):
        return self.posicion[2] / sp.constants.astronomical_unit

    # Defino el operador de comparacion
    def __eq__(self, other):
        if isinstance(other, Cuerpo):
            return self.__indice == other.__indice
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Cuerpo):
            return not self.__indice == other.__indice
        else:
            return True

    # Imprimo el cuerpo, masa en masas solares, posicion al origen en UA, velocidad en km/s
    def __str__(self):
        return "%s: %s,%s,%s,%s,%s,%s,%s" % (self.nombre, self.masa/constantes.MASA_SOL, self.posicion[0]/sp.constants.astronomical_unit, self.posicion[1]/sp.constants.astronomical_unit, self.posicion[2]/sp.constants.astronomical_unit, self.velocidad[0]/1000, self.velocidad[1]/1000, self.velocidad[2]/1000)