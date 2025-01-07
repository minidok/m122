#!/usr/bin/env python3

import geometrie
flaeche_Kreis = geometrie.flaeche_kreis(100/2) - geometrie.flaeche_kreis(10/2)
flaeche_dreieck = geometrie.flaeche_dreieck(80,50) - geometrie.flaeche_viereck(5,5)
print(flaeche_Kreis)
print(flaeche_dreieck)