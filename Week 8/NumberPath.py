import numpy as np
from collections import Counter
from functools import cache


def numPath(tile: int, steps: list, doPrint: bool) -> bool:

    curr = 1 # Starts on tile 1.
    while curr < tile: # While not past the desired tile,
        if doPrint:
            print( "Tile num: " + str(curr) )
        curr += np.random.choice(steps) # Selects a step size at random.
    if doPrint:
        print( "Tile num: " + str(curr) + "\n" )

    return True if curr == tile else False # Returns 'True' if the player lands on the tile, 'False' otherwise.


def trials(tile: int, steps: list, samples: int) -> dict:

    results = []
    for _ in range(samples):
        results.append( numPath(tile, steps, False) )

    return Counter(results) # Returns a dictionary of the results and their occurences.


def constantProb(tile: int) -> float: # Works only for move set (1, 2)

    numerator = np.divide( (np.power(2, tile) - np.power(-1, tile % 2 )), 3 )
    denominator = np.power(2, tile-1)

    return np.divide(numerator, denominator)


@cache # Memoization to increase efficiency.
def recursiveProb(tile: int, steps: tuple) -> float:

    if tile == 1:
        return 1
    elif tile < 1:
        return 0

    prob = 0
    for step in steps:
        temp = tile - step # Works backwards from the desired tile
        prob += np.divide( recursiveProb(temp, steps), len(steps) )
    
    return prob


if __name__ == '__main__':

    totalSamples = 50000
    goal = 25
    moves = (1, 2, 3)

    #numPath(goal, moves, True)

    #x = trials(goal, moves, totalSamples)
    #print( "Number of successes: " + str(x[True]) 
    #print( "Probability of success: " + str(np.divide( x[True], totalSamples )) + '\n' )

    #print( "Probability of success: " + str(constantProb(goal)) + '\n' )

    print( "Probability of success: " + str(recursiveProb( goal, moves )) + '\n' )
