from pandas import *
import copy
import time

n = 7

solutions = 2**n

def block(x,y,board):           # Esta funcion pon e el caracter del alfin en (x,y) y 
    CurrentBoard = copy.deepcopy(board)
    CurrentBoard[x][y] = '♗'           # pone una 'x' en todos los lugares a los que ataca
    for i in range(n):
        if((x-y+i) >= 0 and (x-y+i) < n and i != y):
            CurrentBoard[x-y+i][i] = 'x'
        if((x+y-i) >= 0 and (x+y-i) < n and i != y):
            CurrentBoard[x+y-i][i] = 'x'
    return CurrentBoard                           
   
def placeBishop(init_i,init_j,board): #Esta funcion busca y pone un alfil el primer lugar disponible apartir de init(i,j)
    i = init_i
    j = init_j 
    while (1):
        if(board[i][j] == '-'):
            block(i,j,board)
            print (DataFrame(board))
            return [i,j]
        else:
            i += 1
            if(i == n):
                j += 1
                i = 0
                if(j == n):
                    return 0 
                    break 
    
def getChildrenBoards(CurrentBoard):
    children = list()
    for i in range(n):
        for j in range(n):
            if CurrentBoard[i][j] == '-' :
                newChildren = block(i,j,CurrentBoard)
                CurrentBoard[i][j] = "x"
                children.append(newChildren)
    return children

def getNumberOfBishops(CurrentBoard):
    bishops = 0
    for i in range(n):
        for j in range(n):
            if CurrentBoard[i][j] == '♗' :
                bishops +=1 
    return bishops


def DFSNBishops(n):
    InitialBoard = [ [ '-' for i in range(n) ] for j in range(n) ]
    BoardStack = []
    Boards = []
    BoardStack.append(InitialBoard)

    while(len(BoardStack) != 0 and len(Boards) < 2**n):
        CurrentBoard = BoardStack.pop()
        Children = getChildrenBoards(CurrentBoard)
        if(len(Children) == 0): 
            if(len(Boards) == 0):
                Boards.append(CurrentBoard)
            else:
                if(getNumberOfBishops(CurrentBoard) > getNumberOfBishops(Boards[0])):
                    Boards.clear()
                    Boards.append(CurrentBoard)
                elif (getNumberOfBishops(CurrentBoard) == getNumberOfBishops(Boards[0])):
                    Boards.append(CurrentBoard)
        else:
            for child in Children:
                BoardStack.append(child)
    for i,solution in enumerate(Boards):
        print("Solucion : ", i+1, " of ",solutions )
        print (DataFrame(solution, columns=[chr(ord('A')+i) for i in range (n)], index = range(1,n+1) ))

start_time = time.time()
DFSNBishops(n)
print("--- %s seconds ---" % (time.time() - start_time))







