# from __future__ import division
from random import *
# from huge import v4 as data

# # # # # # # # # # # # # # # # #
# DEEPMIND ALPHASNOW            #
# Snowball Fight Terminator     #
#                               #
# For IC i forgot                   #
# By: Andrew Wang               #
#     add your names            #
#                               #
# STRATEGY SUMMARY: KICK BUTT   #
# WITH MACHINE LEARNING write         #
# # # # # # # # # # # # # # # # #


Sharpness = 0.95 # Precision of each move
# 1 Always choose the best move (Good against robots)
# 0 Very Random (Good against humans)

def getMove(myScore, mySnowballs, myDucksUsed, myMovesSoFar, oppScore, oppSnowballs, oppDucksUsed, oppMovesSoFar):
    # Data mining
    sect = data[myScore][mySnowballs][myDucksUsed][oppScore][oppSnowballs][oppDucksUsed]
    throwRatio = 0 if sect[0][0] == 0 and sect[0][1] == 0 else (sect[0][1]+1)/(sect[0][0]+1)
    reloadRatio = 0 if sect[1][0] == 0 and sect[1][1] == 0 else (sect[1][1]+1)/(sect[1][0]+1)
    duckRatio = 0 if sect[2][0] == 0 and sect[2][1] == 0 else (sect[2][1]+1)/(sect[2][0]+1)
    s = throwRatio + reloadRatio + duckRatio
    throwPercentage = (0 if s == 0 else throwRatio/s, "THROW")
    reloadPercentage = (0 if s == 0 else reloadRatio/s, "RELOAD")
    duckPercentage = (0 if s == 0 else duckRatio/s, "DUCK")
    actionList = sorted([throwPercentage, reloadPercentage, duckPercentage], key=lambda tup: tup[0])
    actionList =  list(map(lambda x: (x[0] * (1-Sharpness), x[1]), actionList))

    # Choosing the move
    die = random()
    if die < actionList[0][0]:
        move = actionList[0][1]
    elif die < actionList[0][0]+actionList[1][0]:
        move = actionList[1][1]
    else:
        move = actionList[2][1]

    # Avoiding ties if winning is possible
    if oppMovesSoFar[-4:] == ["THROW", "RELOAD", "THROW", "RELOAD"] or sect == [[0, 0], [0, 0], [0, 0]]:
        if myDucksUsed < 5:
            return "DUCK"
        else:
            return "THROW"

    # Return statement
    return move

# BIG BRAIN


