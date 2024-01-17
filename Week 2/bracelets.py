starts = [[i,j] for i in range(10) for j in range(10)]  # List of all possible starting pairs
loops = []  # Holder for all bracelets

while starts:   # Runs until all possible starting pairs have been depleted
    loop = []                                                   
    pair = starts[0]    # Gets new unused starting pair
    starts.remove(pair)
    loop.append(pair)   # Transfers pair to new bracelet
    current = [pair[1], (pair[0]+pair[1])%10]
    while current != pair:  # Iterates until back at the starting pair
        starts.remove(current)
        loop.append(current)
        current = [current[1], (current[0]+current[1])%10]
    loops.append(loop)  # Adds new bracelet to list

for loop in loops:  # Prints all bracelets and lengths
    print(loop)
    print(len(loop))