#!/usr/local/bin/python3

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
  file.close()
# Dateninhalt lesen und Zeilenweise bearbeiten
def contents_of_file(filename):
  return_string = ""

  # Eigene Funktion zur Erstellung der Datei
  create_file(filename)

  # Datei öffnen
  with open(filename, 'r') as csv_file:
    # Ein dictionary mit Tabelleninhalt abfüllen
    csv_reader = csv.reader() .DictReader(csv_file)
    # Jede Zeile in Dictionary auslesen
    for row in csv_reader:
      return_string += "Ein {} wird in {} und ist {}\n".format(row["Getränk"], row["Gebinde"], row["Typ"])
  csv_file.close()
  return return_string

#Call the function
print(contents_of_file("lager.csv"))