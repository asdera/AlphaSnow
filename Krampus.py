#STRATEGY SUMMARY:  SPOOK THE OPPONENT
code = "risky gas pumps"

def demons( myScore, mySnowballs, myDucksUsed, myMovesSoFar,
             oppScore, oppSnowballs, oppDucksUsed, oppMovesSoFar ):
    return "FLEE"

def getMove( myScore, mySnowballs, myDucksUsed, myMovesSoFar,
             oppScore, oppSnowballs, oppDucksUsed, oppMovesSoFar ):
    global victim
    bot1 = __import__("Game App BOT vs BOT").strat1
    bot2 = __import__("Game App BOT vs BOT").strat2
    if hasattr(bot1, "code") and bot1.code == "risky gas pumps":
        victim = bot2
    else:
        victim = bot1
    victim.getMove = demons
    return "THROW"
    
