#!/usr/local/bin/python3

import math

def flaeche_dreieck(basis, hoehe):
    return (basis*hoehe)/2

def flaeche_viereck(hoehe, breite):
    return hoehe*breite

def flaeche_kreis(radius):
    return math.pi*(radius**2)