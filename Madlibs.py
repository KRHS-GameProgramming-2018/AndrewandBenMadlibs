#Andrew 155/200 - P; Good start, but some to still finish up
#Ben 70/200 - N; Lets actually accompish some work.

from screens import *
from getInput import *
import story1 
import story3 

print showSplash()
raw_input("Press Enter to Start")

go = True
while go:
    print showMenu()
    response = getMenuInput()
    if response == "Q":
        go = False
        print "Goodbye and thanks for playing"
    elif response == "1":
        print story1.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "3":
        print story3.playMadlibs()
        raw_input("Press Enter to Continue")
    else:
        print "invaild option"

