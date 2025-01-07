#!/usr/bin/env python3

import geometrie
flaeche = geometrie.flaeche_dreieck(80,50) - geometrie.flaeche_viereck(5,5)
flaecheKreis = geometrie.flaeche_kreis(50) - geometrie.flaeche_kreis(5)
print(flaeche)
print(flaecheKreis)