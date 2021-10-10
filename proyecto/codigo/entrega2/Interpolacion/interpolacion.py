import numpy as np 

def interpolacion(file,size):
    aux=np.copy(file)
    rows,columns=aux.shape
    rowExit=int(rows*size)
    columnExit=int(columns*size)
    exit=np.zeros((rowExit,columnExit))
    for i in range(rowExit):
        for j in range(columnExit):
            Xtemp=i/rowExit*rows
            Ytemp=j/columnExit*columns
            x1=int(Xtemp)
            y1=int(Ytemp)
            x2=x1
            y2,y4=y1+1
            y3=y1
            x3,x4=x1+1
            u=Xtemp-x1
            v=Ytemp-y1
            if x4>=rows:
                x4=rows-1
                x2=x4
                x1,x3=x4-1
            if y4>=columns:
                y4=columns-1
                y3=y4
                y1,y2=y4-1
            exit[i,j]=(1-u)*(1-v)*int(aux[x1,y1])+(1-u)*v*int(aux[x2, y2])+u*(1-v)*int(aux[x3, y3])+u*v*int(aux[x4, y4])
    return exit
