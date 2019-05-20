#/bin/python

'''
 ________________________________________
/ This script will help you choosing the \
| right font for your linux Distribution |
\ for your HiDpi screen! GoodLuck        /
 ----------------------------------------
   \             \
    \             \_
     \             \\
      \             \\/\
       \            _\\/
        \         /   -\
         \      /  oo   -\
          \   /           \
             |    ---\    -\
             \--/     \     \
                       |      -\
                        \       -\         -------------\    /-\
                         \        \-------/              ---/    \
                          \                                  |\   \
                           |                                 / |  |
                           \                                |  \  |
                            |                              /    \ |
                            |                             /     \ |
                             \                             \     \|
                              -              /--------\    |      o
                               \+   +---------          \   |
                                |   |                   |   \
                                |   |                    \   |
                                |   |                    |   \
                                |   |                     \   |
                                 \  |                     |   |
                                 |  |                      \  \
                                 |  |                      |   |
                                 +--+                       ---+

'''

usage='''USAGE:

$python /directoryWhereTheScriptIs/tryFont.py outPutFile [NumberOfFontsToBeSelected]
--------------------------------------------------------------------------------------
Execute the script. It will cycle through every font installed on you linux distribution (more precisely it will look in /usr/share/consolefonts/ directory).
Each font is then set and the script will wait for input. Insert yes to save the font you like, anything else to ignore it. As soon as every font has been
displayed the script will begin again, cycling this time with just the font you've already selected and it continues this way with less font every time until
the number you specified in the arguments (as NumberOfFontsToBeSelected). NOTE: by default you'll select just ONE font.s
Finally the fonts will be written to a ./outPutFile.txt

SIDENOTE: You have to execute the script while in console. It doesn't work when ran by console emulators (such as gnome-terminal or tilix)
'''

import os
import sys

if( len(sys.argv) < 2 ):
	print(usage)
	quit();

b = []

fonts = os.popen("ls /usr/share/consolefonts/*").read().split();
 
stop = 1; 
 
if len(sys.argv) == 3:
	stop = sys.argv[2]

while len(b) != stop:
	for a in fonts:
		print(a);
		os.popen("setfont "+a);
		d = raw_input();
		if(d == 's'):
			b.append(a)
		print(b)
	print(b)
	print("Ciclo Completato \n\n\n\n")
	fonts = b;
	b = []
	raw_input("Ricominciare")
print(b)
f = open(sys.argv[1]+".txt", "w");
f.write(b);
f.close()
