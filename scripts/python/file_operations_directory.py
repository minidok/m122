#!/usr/bin/env python3

import os
from datetime import datetime
from posixpath import curdir


def meineTestdatei(afile):
    with open(afile, 'w+') as txt_file:
        txt_file.write('TEST_DATA_STRING')
        txt_file.close()
    return afile


def meineFunktion(afile):
    if os.path.exists(afile):
      os.remove(afile)
    else:
        meineTestdatei(afile)
        os.rename(afile, datetime.now().strftime("%S") +"renamedfile2.txt")
        print(os.path.getsize(meineTestdatei("anotherFile.txt")))


def main():
   
    # Liste für Dateien
    current_working_directory = os.getcwd()
    for file in os.listdir(current_working_directory):
        print(file)
    


if __name__ == "__main__":
    main()