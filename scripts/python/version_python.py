
#!/usr/bin/env python3
# Auslesen der Version von Python

import platform

# Python Ausgabe mit format() Methode
print('This is python version {}'.format(platform.python_version()))
# Python f-Strings Ausgabe (Seit Python Version 3.6)
print(f"This is python version as f-string {platform.python_version()}")
