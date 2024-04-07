import numpy as np
import time

def stringGame(n: int, k: int) -> list: # Function that simulates tying k times in a bowl of n strings
    loops = []
    stringBowl = np.array([i for i in range(n) for _ in (0, 1)])
    np.random.shuffle(stringBowl)

    connections = []
    for i in range(k):
        a,b = stringBowl[2*i:2*(i+1)] # Pairs up random ends
        connections.append([a,b])

    while connections: # Collects the connections into loops or discards remaining strings
        if connections[0][0] == connections[0][-1]:
            loops.append(connections[0])
            connections.pop(0)
        else:
            found = False
            for i in range(1, len(connections)):
                a = connections[0][0]
                if a in connections[i]:
                    found = True
                    if connections[i][0] == a:
                        connections[0].insert(0, connections[i][1])            
                    else:
                        connections[0].insert(0, connections[i][0])
                    connections.pop(i)
                    break
            if found == False:
                connections.pop(0)
    return loops


def probZeroLoopsBasic(n: int, k: int) -> float: # Calculates the probability via the product
    x = 1
    for i in range(1,k+1):
        x = x * np.divide((2 * n) - (2*i), (2*n) - (2*i) + 1)
    return x

def probZeroLoopsAlt(n: int, k: int) -> float: # Calculates the probability via the product 
    x = 1
    y = 1
    for i in range(k):
        x = x * np.divide((2*(n-i)) -1, (n -i +1))
        y = y*2
    return np.divide(y * (n-k) * (n-k+1), n * (n+1) * x)

 
def compare(n: int, a: float, b: float) -> None: # Generates and compares a value for k to a/b
    b2 = b*b
    a2 = a*a
    k = int(np.floor(((b2-a2)*n)/b2))
    if n%b2 != 0:
        k+=1

    x1 = probZeroLoopsBasic(n,k-1)
    x2 = x1 * (((2*n)-(2*k))/((2*n)-(2*k)+1)) # Value of k in the function
    x3 = x2 * (((2*n)-(2*(k+1)))/((2*n)-(2*(k+1))+1))

    diff = abs(x2-(a/b))
    closest = " --------- "
    if diff < abs(x1-(a/b)) and diff < abs(x3-(a/b)):
        closest = " -closest- "
    
    print("n."+str(n), "k."+str(k) + closest, end="")
    if x1 > a/b and x2 < a/b:
        print("Correct")
    elif x2 > a/b:
        print("Under")
    else:
        print("Over")


def stringGameToMatrix(n: int) -> np.matrix: # Generates an adjacency matrix from a string game
    pathMatrix = np.zeros((n,n))
    stringBowl = [i for i in range(n) for _ in [0,1]]
    np.random.shuffle(stringBowl)
    for i in range(n):
        a,b = stringBowl[2*i:2*(i+1)]
        pathMatrix[a][b] = 1
        pathMatrix[b][a] = 1
    return pathMatrix


def countPaths(pathMatrix: np.matrix) -> int: # Counts the number of loops in the adjacency matrix
    n = len(pathMatrix)
    vals = [val for val in range(n)]
    pathCount = 0
    while vals:
        start = vals[0]
        vals.remove(start)
        toGo = np.where(pathMatrix[start] == 1)[0]
        if len(toGo) == 1:
            if start == toGo[0]:
                pathCount += 1
            else:
                pathCount += 1
                vals.remove(toGo[0])
            continue
        current = start
        prev = start
        nextString = toGo[0]
        while nextString != start:
            vals.remove(nextString)
            prev = current
            current = nextString
            toGo = np.where(pathMatrix[current] == 1)[0]
            temp = np.where(toGo != prev)[0]
            nextString = toGo[temp[0]]        
        pathCount += 1

    return pathCount

def trialsForZero(n: int, k: int, trialNum: int) -> float:
    total = 0
    for _ in range(trialNum):
        total += not(bool(len(stringGame(n, k))))
    return np.divide(total, trialNum)


        
if __name__ == "__main__":
    n = 5
    k = 4
    samples = 100_000

    # strings = stringGame(n, k)
    # print(strings)
    # print(len(strings))

    # print(probZeroLoopsAlt(n, k))
    # print(probZeroLoopsBasic(n, k))
    
    # print(trialsForZero(n, k, samples))

    # mat = stringGameToMatrix(n)
    # print(mat)
    # print(countPaths(mat))

    a,b = 1,2
    num = 100_000
    for i in range(num,num+100):
        compare(i, a, b)
    
    
