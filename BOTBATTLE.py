#Imports
import time
from random import *
import random
import math


#Assign strategy names to variables
strat1Name = "AlphaSnow"
strat2Name = "SnowDestroyer9000"

#Import the two strategies
strat1 = __import__(strat1Name)
strat2 = __import__(strat2Name)

wins1 = 0
wins2 = 0
draw12 = 0

duckLimit = 5
snowballLimit = 10
roundLimit = 30


def announce( message ):
    print(message)

                    
def announceGameResult( cheatingFound1, cheatingFound2, score1, score2, roundNum ):
    global wins1, wins2, draw12
    summary = ""

    if cheatingFound1 == True and cheatingFound2 == True:
        summary = "Both players cheated! Loss for both players"
        draw12 += 1
        
    elif cheatingFound1 == True:
        summary = strat1Name + " cheated! " +  strat2Name + " wins!"
        wins2 += 1
        
    elif cheatingFound2 == True:
        summary = strat2Name + " cheated! " +  strat1Name + " wins!"
        wins1 += 1
        
    elif roundNum >= roundLimit:
        summary = str(roundLimit) + " rounds reached."

        if score1 > score2:
            summary = summary + " " + strat1Name + " wins!"
            wins1 += 1
            
        elif score2 > score1:
            summary = summary + " " + strat2Name + " wins!"
            wins2 += 1
            
        else:
            summary = summary + " Draw!"
            draw12 += 1

    else:
        if score1 > score2:
            summary = summary + strat1Name + " wins!"
            wins1 += 1
            
        elif score2 > score1:
            summary = summary + strat2Name + " wins!"
            wins2 += 1

    announce( summary )


def game():
    x=0
    global curMove1, curMove2, cheatingFound1, cheatingFound2
    
    #Initialize variables
    score1 = 0
    score2 = 0
    
    snowballs1 = 1
    snowballs2 = 1
    
    ducksUsed1 = 0
    ducksUsed2 = 0
    
    movesSoFar1 = []
    movesSoFar2 = []
    
    roundNum = 0
    i = -1

    cheatingFound1 = False  #True if Player 1 has cheated
    cheatingFound2 = False  #True if Player 2 has cheated

    #Main loop
    while score1 < 3 and score2 < 3 and roundNum <= roundLimit and cheatingFound1 == False and cheatingFound2 == False:
        #Increment i 
        i += 1
        
        #Use i to find out whose turn it is 
        if i % 2 == 0:
            #Reset booleans
            duckC1 = False
            duckC2 = False
            throwC1 = False
            throwC2 = False
            reloadC1 = False
            reloadC2 = False

            #Increase round number
            roundNum += 1

            #If not round 1, then add both moves to their move-histories
            if roundNum > 1:
                movesSoFar1.append(curMove1)
                movesSoFar2.append(curMove2)
                
            #Get Player 1's move
            curMove1 = strat1.getMove(score1, snowballs1, ducksUsed1, movesSoFar1,
                                      score2, snowballs2, ducksUsed2, movesSoFar2)
            x=x+1

            #Check the validity of Player 1's move
            if curMove1 == "DUCK":
                
                if ducksUsed1 == duckLimit: #ILLEGAL DUCK!
                    print("Player 1 tried to duck for the 6th time!")
                    cheatingFound1 = True
                    
                duckC1 = True

            elif curMove1 == "RELOAD":
                
                if snowballs1 >= snowballLimit: #ILLEGAL RELOAD!
                    print("Player 1 tried to hoard more than " + str(snowballLimit) + " snowballs!")
                    cheatingFound1 = True
 
                reloadC1 = True

            elif curMove1 == "THROW":
                
                if snowballs1 == 0: #ILLEGAL RELOAD!
                    print("Player 1 tried to use snowballs when they have none left!")
                    cheatingFound1 = True
                    
                throwC1 = True
                
            else: #ILLEGAL WORD
                print( strat1Name + ": " + curMove1 + " is not an option!")
                cheatingFound1 = True
        
        else:
            
            #Get Player 2's move
            curMove2 = strat2.getMove(score2, snowballs2, ducksUsed2, movesSoFar2,
                                      score1, snowballs1, ducksUsed1, movesSoFar1)

            #Check validity of Player 2's move
            if curMove2 == "DUCK":

                if ducksUsed2 == duckLimit: #ILLEGAL DUCK!
                    print("Player 2 tried to duck for the 6th time")
                    cheatingFound2 = True
                    
                duckC2 = True
                ducksUsed2 = ducksUsed2 + 1
                
            elif curMove2 == "RELOAD":
                snowballs2 += 1
                if snowballs2 > snowballLimit: #ILLEGAL RELOAD!
                    print("Player 2 tried to hoard more than " + str(snowballLimit) + " snowballs!")
                    cheatingFound2 = True

                reloadC2 = True
                
            elif curMove2 == "THROW":

                if snowballs2 == 0: #ILLEGAL THROW!
                    print("Player 2 tried to throw when they have no snowballs!")
                    cheatingFound2 = True
                    
                throwC2 = True
                snowballs2 -= 1

            else: #ILLEGAL WORD!
                print( strat2Name + ": " + curMove2 + " is not an option!")
                cheatingFound2 = True

            #Adjust snowballs1 and ducksUsed1 (done later so player 2 doesn't know)
            if throwC1:
                snowballs1 -= 1
            if reloadC1:
                snowballs1 += 1
            if duckC1:
                ducksUsed1 = ducksUsed1 + 1
            
            #If no one threw then no one got hit
            if not throwC1 and not throwC2:
                summary = "No one got hit."

            #If any person reloaded that means they got hit (since the other person has thrown as we didn't pass the above if-statement)
            #Also adjusts the scores for the player that scored the hit
            elif reloadC1 or reloadC2:
                if reloadC1:
                    summary = strat1Name + " got hit!"
                    score2 += 1
                else:
                    summary = strat2Name + " got hit!"
                    score1 += 1

            #If both players threw, then snowballs collide and no one gets hit        
            elif throwC1 and throwC2:
                summary = "Snowballs collide, so no one got hit."

            #If none of the above happened then one of the players missed
            #Prints out who missed their snowball
            else:
                if throwC1:
                    summary = strat1Name + " missed!"
                elif throwC2:
                    summary = strat2Name + " missed!"

            # print(curMove1, "\t", curMove2)
            # print(summary)
            # print("Score:", score1, score2)
            # print("Snowballs:", snowballs1, snowballs2)
            # print("Ducks left", duckLimit - ducksUsed1, duckLimit - ducksUsed2)
            # print("")         
            

            
    #Once the while-loop stops (by someone winning or cheating, or we reached the round-limit), announce the result   
    announceGameResult( cheatingFound1, cheatingFound2, score1, score2, roundNum )

for g in range(1000):
    game()

print("WINS")
print(strat1Name)
print(wins1)
print(strat2Name)
print(wins2)
print("DRAWS")
print(draw12)
