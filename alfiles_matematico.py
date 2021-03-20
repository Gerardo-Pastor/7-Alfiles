from pandas import *

n = 4 

#print("omg el numero de soluciones configuraciones es: ", 2**n)

def bitarr(num):
    size =len(bin(2**n-1)[2:])
    output = bin(num)[2:]
    while len(output) < size:
        output = '0'+output
    return output
    
def setPos(i,j,b,tablero):
    if b == True :
        tablero[i][j] = "♝"
    else :
        tablero[i][j] = "☐"


for i in range(2**n):
    pos = [True if digit=='1' else False for digit in bitarr(i)]
    
    tablero = [["☐" for x in range(n)] for y in range(n)] 
    
    print("Configuracion: ",i+1, " de ",2**n)
    
    for i in range(n):
        setPos(0,i,pos[i],tablero)
        
    for i in range(1,n):
        setPos(i,0,not pos[i],tablero)
        setPos(i,n-1,not pos[n-i-1],tablero)
    
    for i in range(1,n-1):
        setPos(n-1,i, pos[n-i-1] ,tablero)
        
        
    print(DataFrame(tablero))
    
    print("---------------------")