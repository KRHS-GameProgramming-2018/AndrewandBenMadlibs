from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    food1 = getWord("Enter a food: ")
    verb1 = getWord("Enter a verb")
    adjective1 = getWord("Enter an adjective")
    vechile = getWord("enter a vechile")
    communicationsdevice1 = getWord("Enter a communications device")
    friend2 = getWord("enter a name")
    adj2 = getWord("Enter an adjective")
    
    output = ""
    output += "Me and my friend, " + friend1
    output += ". were taking a walk when suddenly  " + friend1
    output += " said that this walk was " + adjective1
    output += "after saying that we arrived on top of the hill and set up a picnic "
    output += "did you bring the " + food1 
    output += "I did! I always love these outings "
    output += "We saw a bird in a tree, we started to walk towards it but then in suddleny it " +verb1
    output += "after the picnic we got in the " +vechile
    output += "wow what a crazy day, I should use my " +communicationsdevice1
    output += "and call my other friend " +friend2
    output += "ok sounds good, thanks for the "+ adj2
    output += "day."
    return output












