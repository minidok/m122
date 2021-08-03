#!/usr/bin/env python3

import os
import csv

# CSV Datei mit Daten erstellen
def create_file(filename):
  with open(filename, "w") as file:
    file.write("Getränk,Gebinde,Typ\n")
    file.write("Wein,Karton,Alkoholhaltig\n")
    file.write("Wasser,PET, Alkoholfrei\n")
    file.write("Süssgetränk,PET,Alkoholfrei\n")
    file.write("Tee,Beutel,Koffeinhaltig\n")
    file.write("Cola,Gebinde,Zuckerhaltig\n")

# Dateninhalt lesen und Zeilenweise bearbeiten
def contents_of_file(filename):
  return_string = ""

  # Eigene Funktion zur Erstellung der Datei
  create_file(filename)

  # Erstellte Datei öffnen
  with open(filename, 'r') as csv_file:
    # Zeilen aus Datei einlesen
    rows = csv.reader(csv_file, delimiter=',')
    # Jede Zeile durchgehen
    next(rows)
    for row in rows:
      Getränk, Gebinde, Typ = row
      # Format the return string for data rows only
      return_string += "Ein {}: wird in {} gelagert und ist {}\n".format(Getränk, Gebinde, Typ)
  return return_string

#Call the function
print(contents_of_file("lager.csv"))