import numpy as np

def game(n: int, playerStarts: bool, playerIsZero: bool) -> None: 

    available = [[i,j] for i in range(n) for j in range(n)]
    board = [["_" for i in range(n)] for j in range(n)]
    playersGo = playerStarts

    for row in board:
        print("[{0}]".format(', '.join(map(str, row))))

    while len(available) > 0:
        if playersGo:
            x = input("Enter co-ordinate: ")
            while isClean(x, available) == False:
                x = input("Please enter co-ordinate in correct format: ")
            x = [int(i.strip()) for i in x.split()]
            available.remove(x)
            board[x[0]][x[1]] = int(not playerIsZero)
            playersGo = False
        else:
            num = np.random.randint(0,len(available))
            x = available[num]
            print("Bot chooses: " + str(x))
            available.remove(x)
            board[x[0]][x[1]] = int(playerIsZero)
            playersGo = True
            
        for row in board:
            print("[{0}]".format(', '.join(map(str, row))))
                
    det = np.linalg.det(board)
    print("The determinant is: " + str(det))
    if det == int(not playerIsZero):
        print("Player Wins!")
    else:
        print("Bot Wins.")
    

def isClean(string: str, arr: list) -> bool:
    clean = False
    temp = string.split()
    if len(temp) == 2 and temp[0].isnumeric() and temp[1].isnumeric():
        coord = [int(i.strip()) for i in string.split()]
        if coord in arr:
            clean = True
    return clean

if __name__ == "__main__":
    game(3, True, True)