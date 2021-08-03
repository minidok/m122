#!/usr/bin/env python3

import os

myDirectory = 'tttestfolder'

#Verzeichnis erstellen
try:
    os.mkdir(myDirectory)
except FileExistsError:
    print("Verzeichnis gibt es schon...")

#Auflistung des aktuellen Verzeichnis
datei_liste = os.listdir()
assert(myDirectory in datei_liste)

for name in os.listdir():
    fullname = os.path.join(os.path.curdir, name)
    if os.path.exists:
        if os.path.isdir(fullname):
            print("{} ist ein Verzeichnis".format(fullname))
        else: print("{} ist eine Datei".format(fullname))
    else: print("Verzeichnis {} existiert nicht!".format(fullname))

os.rmdir(myDirectory)

#Ausgabe Pfad ist System abhängig
#Beachte POSIX vs Windows
print(os.getcwd())