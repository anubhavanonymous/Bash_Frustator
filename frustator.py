# -*- coding: utf-8 -*-

#------------------------------------------------------#
#                    BASH FRUSTATOR !                  #
#               Coded by Anubhav Kashyap               #
#~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#      Github     :   github.com/anubhavanonymous      #
#     Instagram  :  instagram.com/anubhavanonymous     #
#------------------------------------------------------#
#            If you came here to copy code             #
#               then you are an Asshole                #
#------------------------------------------------------#

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
success = G + '[' + W + '√' + G + '] '
error = R + '[' + W + '!' + R + ']'

os.system("clear")
banner = """

   {}    █▄▄ ▄▀█ █▀ █░█   █▀▀ █▀█ █░█ █▀ ▀█▀ ▄▀█ ▀█▀ █▀█ █▀█
   {}    █▄█ █▀█ ▄█ █▀█   █▀  █▀▄ █▄█ ▄█ ░█░ █▀█ ░█░ █▄█ █▀▄
   {}
   {}                           github.com/anubhavanonymous
""".format(G,W,W,Y)

banner2 = """
       {}[{}1{}]{} Encrypt        {}[{}2{}]{} Decrypt
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2

def decrypt():
   try:
       sc = raw_input(ask + W + "Script " + G + ">> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       print("")
       out = raw_input(ask + W + "Output" + G + " >> " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print("")
       print (success + "Done..")

   except KeyboardInterrupt:
       print("")
       print (error + " Stopped !")
   except IOError:
       print("")
       print (error + " File Not Found !")

def encrypt():
   try:
       script = raw_input(ask + W + "Script " + G + ">> " + W)
       print("")
       output = raw_input(ask + W + "Output " + G + ">> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print("")
       print (success + "Done..")
   except KeyboardInterrupt:
       print("")
       print (error + " Stopped !")
   except IOError:
       print("")
       print (error + " File Not Found !")


fuck = raw_input(Y + " ✯ " + W + "Select Option" + G + " ⋙⋙⋙ ")
print("")
if fuck == "1" or fuck == "01":
   encrypt()
elif fuck == "2" or fuck == "02":
   decrypt()
else:
   print (error + " Wrong input")
   print("")
