#!/bin/bash

egrep ' X =' $1 | cut -c 6-26 > X_$2.txt
egrep ' X =' $1 | cut -c 57-78 > Z_$2.txt
egrep ' X =' $1 | cut -c 31-52 > Y_$2.txt
