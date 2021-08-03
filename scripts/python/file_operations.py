#!/usr/local/bin/python3

import os
from datetime import datetime

def meineTestdatei(afile):
    with open(afile, 'w') as txt_file:
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

if __name__ == "__main__":
    meineFunktion("Testfile.txt")