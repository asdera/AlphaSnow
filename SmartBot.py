from random import *



def getMove( myScore, myBalls, myDucksUsed, myMovesSoFar, oppScore, oppBalls, oppDucksUsed, oppMovesSoFar ):
##    print("So far I have made these moves:", myMovesSoFar )
    if oppScore < 2 and len(myMovesSoFar) < 9: #OUR STRATEGY TO CONTINUE RELOADING UNTIL EITHER OUR OPPENENT HITS US TWICE OR WE GET TO TURN 10
        return "RELOAD"
        
    else:
        if oppBalls == 1 and myDucksUsed < 5:   #DUCK WHEN OPPENENT HAS A BALL AS THEYRE MOST LIKELY TO THROW A SNOWBALL
            if myBalls == 0:
                return "RELOAD"
            else:           
                if oppBalls > myBalls:
                    l = oppMovesSoFar[-4:]
                    x = l.count("DUCK")
                    if x > 2:
                        pd = 25
                        pt = 5
                        pr =70

                    else:
                        pd = 60
                        pt = 40
                        pr = 0

                        
                elif oppBalls < myBalls:
                    pd = 40
                    pt = 60
                    pr = 0
                else:
                    l = oppMovesSoFar[-4:]
                    x = l.count("DUCK")
                    if x > 2:
                        pd = 25
                        pt = 5
                        pr =70

                    else:
                        pd = 50
                        pt = 50
                        pr = 0
                OPTIONS = ["DUCK"]*pd + ["THROW"]*pt + ["RELOAD"]*pr
                x = choice(OPTIONS)
                return x


        elif oppBalls == 1 and myDucksUsed == 5:
            if myBalls > 1:
                if oppDucksUsed == 5 and oppScore < 2 :
                    return "THROW"

                else:                      #IN OUR WORST SITUATION WE WILL HAVE AN UNLIKLOEY CHANCE TO RELOAD SO WE WONT BE STUCK IN AN INFINITE LOOP WHERE WE THROW A BALL THEN RELOAD
                    if myBalls == 10:      #IN THE SLIGHT CHANCE WE HAVE 10 SNOWBALLS WE MUST THROW IN ORDER NOT TO CHEAT                
                        return "THROW"

                    elif myScore < 2:      #IF OUR SCORE IS 0 WE WILL HAVE A RANDOM CHANCE OF EITHER RELOADING OR THROWING BUT THE THROWING WILL HAVE A GREATER CHANCE
                        pr = 30
                        pt = 70
                         
                    else:                          
                        pr = 10
                        pt = 90

                    OPTIONS = ["RELOAD"]*pr + ["THROW"]*pt
                    x = choice(OPTIONS)
                    return x                                                
            else:
                return "RELOAD"

        
        elif oppBalls == 0:
            if myBalls == 0:
                return "RELOAD"                #IF THE OPPENENT HAS NO SNOWBALLS AS WELL AS OURS, WE RELOAD
            else:
                if oppDucksUsed == 5:
                    return "THROW"            #ELSE WE THROW BECAUSE THEY HAVE NO SNOWBALLS
                                                   #IF THEY HAVE MORE THEN 1 DUCK WE WILL HAVE A TINY CHANCE OF RELOADING DUE TO US HAVING 0 RISK OF DYING
                else:
                    pt = 80
                    pr = 20
                    
                OPTIONS = ["RELOAD"]*pr + ["THROW"]*pt
                x = choice(OPTIONS)
                return x

        

        elif myBalls == 0:
            return "RELOAD"                      #RELOAD IF WE HAVE NO SNOWBALLS


        elif oppBalls > 1 and myBalls > 0:      #SPECIAL START IF THEY ARE TRYING TO RELOAD SPAM THEN WE CAN GET SOME EASY HITS ON THEM
            return "THROW"  
        
        else:                               
            return "RELOAD"                 
        
      
        

    
    
        
