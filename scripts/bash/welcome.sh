#!/bin/bash
# Variable current_user mit dem eingelogten Benutzer befüllen
current_user=$(whoami)
# Variable timestamp mit aktueller Systemzeit befüllen
timestamp=$(date +%H:%M)
echo "Guten Tag $current_user!"
echo "Es ist jetzt genau: $timestamp"
