#!/bin/bash
for directory in $*; do
    if [ ! -d $directory ]; then 
       file=$directory	
       md5sum $file
    else
       echo "Verzeichnis $directory, wird ausgelassen!"
    fi 
 
done;
