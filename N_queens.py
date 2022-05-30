
def isSafe(board,row,col):
    # checking if queen in same col
    for i in range(row):
        if board[i][col]:
            return False
    
    # checking if queen is in same diagonal right side.
    maxLeft = min(row,col)

    for i in range(1,maxLeft+1):
        if board[row-i][col-i]:
            return False

    # checking if queen is in same diagonal left side.
    maxRight = min(row, len(board)-col-1)

    for i in range(1,maxRight+1):
        if(board[row-i][col+i]):
            return False
    
    return True



def queens(board, row):
    if row == len(board):
        display(board)
        print()
        return 1
    
    count = 0

    #placing queen for checking for evry row and col
    for col in range(len(board)):
        #place queen if it is safe.
        if isSafe(board,row,col):
            board[row][col] = True
            count += queens(board,row+1)
            board[row][col] = False

    return count

def display(board):
    for i in range(len(board)):
        print("[",end=' ')
        for j in range(len(board[i])):
            if board[i][j]: print("Q ",end='')
            else: print("_ ",end='')
        print("]")


N = int(input("Enter N: "))
board = [[0 for _ in range(N)] for _ in range(N)]
print(queens(board,0))

