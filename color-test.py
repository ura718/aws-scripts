#!/usr/bin/python


#
# Requires package "python2-colorama.noarch" from epel
#

from colorama import *

print (Fore.BLUE  + "Blue TEXT")
print (Fore.RED   + "Red TEXT")
print (Fore.GREEN + "Green TEXT")
print 'Is this normal? No'
print (Style.RESET_ALL)
print 'Back to normal? Yes'
