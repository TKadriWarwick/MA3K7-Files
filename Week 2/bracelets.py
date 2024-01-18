starts = [[i,j] for i in range(10) for j in range(10)]  # List of all possible starting pairs
Bracelets = []  # Holder for all bracelets

while starts:   # Runs until all possible starting pairs have been depleted
    bracelet = []                                                   
    pair = starts[0]    # Gets new unused starting pair
    starts.remove(pair)
    bracelet.append(pair)   # Transfers pair to new bracelet
    current = [pair[1], (pair[0]+pair[1])%10]
    while current != pair:  # Iterates until back at the starting pair
        starts.remove(current)
        bracelet.append(current)
        current = [current[1], (current[0]+current[1])%10]
    Bracelets.append(bracelet)  # Adds new bracelet to list

for bracelet in Bracelets:  # Prints all bracelets and lengths
    print(bracelet)
    print(len(bracelet))