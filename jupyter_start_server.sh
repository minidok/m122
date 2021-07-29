#!/bin/bash
echo "Starte jupyter Server"
echo "----------------------"
#IP Adresse auslesen in Debian Linux
ip_adresse=$(ip addr | grep 'state UP' -A2 | tail -n5 | awk '{print $2}' | cut -f1  -d'/' | head -n1 | cut -d " " -f1)
echo "Dieser Servier ist unter IP erreichbar: " $ip_adresse
jupyter notebook --ip=$ip_adresse &
