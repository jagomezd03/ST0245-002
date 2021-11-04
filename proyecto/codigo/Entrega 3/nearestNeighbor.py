import numpy as np
import math

def compressNeighbor(file,size):
    aux=np.copy(file)
    rows,columns=aux.shape
    rowExit=int(rows*size)
    columnsExit=int(columns*size)
    exit=np.zeros((rowExit,columnsExit))
    chosenRow, chosenColumn=0
    plus=(size)**-1
    for i in range(rowExit):
        for j in range(columnsExit):
            if chosenColumn>=columns:
                break
            exit[i,j]=aux[chosenRow,chosenColumn]
            chosenColumn+=int(plus)
        chosenRow+=int(plus)
        chosenColumn=0
        if chosenRow>=rows:
            break
    return exit 

"""
def uncompressNeighbor(file,size):
    aux=np.copy(file) #Making a copy of the original file
    rows,columns=aux.shape #Returning the amount of rows and columns
    rowExit=int(rows*size)
    columnsExit=int(columns*size)
    exit=np.zeros((rowExit,columnsExit)) #Building the final image
    chosenRow, chosenColumn, i, j=0
    while i<=rowExit:
        while j<=columnsExit:
            exit[i,j]=aux[chosenRow,chosenColumn]
            exit[i,j+1]=aux[chosenRow,chosenColumn]
            exit[i+1,j]=aux[chosenRow,chosenColumn]
            exit[i+1,j+1]=aux[chosenRow,chosenColumn]
            chosenColumn+=1
            j+=2
            if j+1>=columnsExit:
                break
        chosenRow+=1
        chosenColumn, j=0
        i+=2
        if i+1>=rowExit:
            break
    return exit
"""
