#!/bin/sh

for i in /usr/share/consolefonts/Uni*;
do
	echo $i
	setfont $i
	sleep 1
	#read -n 1 
	scanf "%*c"
done
