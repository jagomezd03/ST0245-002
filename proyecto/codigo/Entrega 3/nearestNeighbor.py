import numpy as np
import math
#Importing the libraries that we need

def compressNeighbor(file,size):
    aux=np.copy(file)#Making a copy of the original file
    rows,columns=aux.shape#Returning the amount of rows and columns
    rowExit=int(rows*size)#Here we set the new amount of rows
    columnsExit=int(columns*size)#Here we set the new amount of columns
    exit=np.zeros((rowExit,columnsExit))#Building a numpy zeros matrix
    chosenRow, chosenColumn=0
    plus=(size)**-1
    for i in range(rowExit):#Here we make the compression
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

def uncompressNeighbor(file,size):
    aux=np.copy(file)#Making a copy of the original file
    rows,columns=aux.shape #Returning the amount of rows and columns
    rowExit=int(rows*size)#Here we set the new amount of rows
    columnsExit=int(columns*size)#Here we set the new amount of columns
    exit=np.zeros((rowExit,columnsExit)) #Building the final image
    chosenRow, chosenColumn, i, j=0
    while i<=rowExit:#Here we make the uncompression
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
