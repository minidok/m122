#!/bin/bash

string_a="Tesla"
string_b="VW"

echo "Sind $string_a und  $string_b gleich lange Wörter?"
[ $string_a == $string_b ]
echo $?

num_a=200
num_b=200

echo "Ist $num_a gleich wie $num_b ?" 
[ $num_a -eq $num_b ]
echo $?
