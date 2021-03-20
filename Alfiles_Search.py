def block(x,y,board):           # Esta funcion pon e el caracter del alfin en (x,y) y 
    board[x][y] = '♗'           # pone una 'x' en todos los lugares a los que ataca
    for i in range(n):
        if((x-y+i) >= 0 and (x-y+i) < n and i != y):
            board[x-y+i][i] = 'x'
        if((x+y-i) >= 0 and (x+y-i) < n and i != y):
            board[x+y-i][i] = 'x'        
                            
   
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
    


board = [ [ '-' for i in range(n) ] for j in range(n) ] 

whole = [ [[ '-' for i in range(n) ] for j in range(n) ] for z in range(maxB)]

i = 1

while placeBishop(0,0,board) != 0: 
    print("Bishops placed: ", i)
    i+=1
