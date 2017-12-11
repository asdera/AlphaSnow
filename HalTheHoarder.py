from random import *

#STRATEGY SUMMARY:  SAVE UP 6 SNOWBALLS, THEN THROW CONTINUOUSLY. WHILE BUILDING UP, SOMETIMES
#DUCK WITH A PROBABILITY THAT'S PROPORTIONAL TO THE NUMBER OF DUCKS WE HAVE LEFT


def getMove( myScore, myBalls, myDucksUsed, myMovesSoFar,
             oppScore, oppBalls, oppDucksUsed, oppMovesSoFar ):

    #GET MY LAST MOVE
    if len( myMovesSoFar ) > 0: #if we've played at least 1 round
        myLastMove = myMovesSoFar[ -1 ] #the last item in the array
        
    else:
        myLastMove = ""
        

    #SAVE UP TO 6 SNOWBALLS, THEN THROW 6 TIMES IN A ROW                             
    if myBalls >= 6 or (myLastMove == "THROW" and myBalls > 0):
        return "THROW"

    else:
        duckProbability = (5-myDucksUsed)*15
        reloadProbability = 100 - duckProbability
        return chooseRandomMove(0, duckProbability, reloadProbability)
    

    
def chooseRandomMove( prT, prD, prR ):
    return choice( prT * ["THROW"] + prD * ["DUCK"] + prR * ["RELOAD"] )
