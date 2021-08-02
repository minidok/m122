#!/bin/bash

if [ ! -z $1 ] && [ ! -z $2 ]; then
   nummer_a=$1
   nummer_b=$2
else
   nummer_a=200
   nummer_b=400
fi

if [ $nummer_a -lt $nummer_b ]; then
    echo "$nummer_a is less than $nummer_b!"

else
    echo "$nummer_a is greater than $nummer_b!"
fi
