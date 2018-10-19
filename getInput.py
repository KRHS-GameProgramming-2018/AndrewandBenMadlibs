def getMenuInput():
    goodInput = False
    while not goodInput:
        response = raw_input(" > ")
        if (response == "1" 
            or response == "One"):
            response = "1"
            goodInput = True
        elif (response == "Q"
              or response == "Quit"
              or response == "q"
              or response == "quit"
              or response == "X"
              or response == "Exit"):
              response = "Q"
              goodInput = True              
        else:
            print "Please make a valid choice"
    return response
    
def getWord(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
    return word
    
def getNumber(prompt, minNumber, maxNumber):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt+" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") ")
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        goodInput = True
        for character in word:
            if character not in nums:
                print "not a number"
                goodInput = False
                break
        if goodInput and (int(word) < minNumber or int(word) > maxNumber):
            goodInput = False
            print "Out of Range"
        
            
    return word

def getTreetype(prompt):  
    goodInput = False
    while not goodinput: 
        word = raw_input(prompt)
        trees = ["oak",
                  "maple",
                  "birch",
                  "magnolia",
                  "redwood",
                  ]
        goodInput = False
        if word in trees:
            goodInput = True
        else:
            print "I've never heard of that type of tree"
    return word

def isSwear(word):
    swearList = ["poop",
                "damn",
                "fuck",
                "fucking",
                "fucked",
                "nigger",
                "kike",
                "shit",
                "Spic",
                "Dyke",
                "Darn",
                "godamn",
                "diddle",
                "shit",
                "cunt",
                "jewnigger",
                "ass",
                "bitch",
                "bastard",
                "cock",
                "slut",
                "vapid-bitch",
                "fag",
                "faggot",
                "chode",
                "whore"
                "fucking",
                "piss"
                ]
    if word in swearList:
        return True
    else:
        return False
