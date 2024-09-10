# Bedingungen und Eingaben verwenden
# Script vergleicht zwei Eingaben

read -p "Wert für X " x
read -p "Wert für Y " y
if [ $x -gt $y ]; then 
   echo X is greater than Y
elif [ $x -lt $y ]; then 
   echo X is less than Y
elif [ $x -eq $y ]; then 
  echo X is equal to Y
fi  
