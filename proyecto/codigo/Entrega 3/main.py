import numpy as np
import os
from collections import deque
import pandas as pd
import LZ77 as lz
import VecinoMasCercano_ as vc
import matplotlib.pyplot as mpl
from time import time
#Importing the libraries that we need

class structure():
    def dataStructure(self,cattle):#Building a linked list with python deque()
        file=os.listdir(cattle) 
        cattleArray=deque()
        for i in range(len(file)):#Building a dictionary with the namefile and a matrix with the pixel values
            dict={}#The main reason that why we use the dict is having the original namefileduring the process
            dict["Name"]=file[i]#We build the dictionary
            address=cattle+"/"+file[i]#We make a parameter containing the location
            data=pd.read_csv(address,header=None)
            array=np.asarray(data)#Building a numpy array
            dict["Array"]=array
            cattleArray.append(dict)#Here we build deque list using the dictionary
        return cattleArray 

    def compression(self,folder,arr):#Building a method to compress the files in a folder
        for i in range(len(arr)):
            rows,columns=arr[i]["array"].shape 
            compressor=lz.LZ77(30)#Using our auxiliar called compressor we use the lz77 algorythm
            ImgCom=vc.compressNeighbor(arr[i]["array"],0.25).astype(np.uint8)#Using anothr auxiliar called ImgCon that contains the compressed image using the nearest neighbor algorythm
            concatenation=np.concatenate(ImgCom)#We concatenate using the numpy concatenation method on the ImgCon parameter
            origin=list(concatenation)#We make a list that contain th last paramter called origin
            ImgCom2=compressor.compress(origin)#We build a second compressed image to use the methods of the lz77 algorythm
            df=pd.DataFrame(np.array(ImgCom2))#We build a new parameter to contain the use of the DataFrame method included in pandas library to make a numpy array
            df.to_csv(folder+"/"+arr[i]["name"],index=False) #We make the csv file using the df parameter
            mpl.imshow(ImgCom2)#Here we display the data as an image to the user
            mpl.show()#Here display all open figures

    def uncompression(self,originFolder,finalFolder):#Building a method to uncompress the files and leave them in the new folder
        for i in os.listdir(originFolder):
            im=pd.read_csv(originFolder+"/"+i)#We build an auxiliar to use as an imported file into our method
            uncompressor=lz.LZ77(30)#Using our auxiliar called uncompressor we use the lz77 algorythm
            arr=uncompressor.decompress(im.values)#We build an array to use the methods of the lz77 algorythm
            columns=i.split(".")#Here we split the file by a point
            rowsG=int(columns[2])#We made a tuple fo 2 items using the rows in the file
            rowsGG=int(rowsG/4)#We divide by 4 the tuple
            columnsG=int(columns[3])#We made a tuple of 3 items using the columns in the file
            columnsGG=int(columnsG/4)#We divide by 4 the tuple
            uncompression=np.array(arr).reshape(rowsGG,columnsGG)#Now is time to start uncompressing the files but we need contain in a parameter having the numpy array with the new rows and columns
            arrL=vc.uncompressNeighbor(np.asarray(uncompression),4).astype(np.uint8) #We build a new array that use the uncompressing method of the nearest neighbor algortyhm
            df=pd.DataFrame(np.array(arrL))#We build a new parameter to contain the use of the DataFrame method included in pandas library to make a numpy array with the arrL parameter
            df.to_csv(finalFolder+"/"+i,header=None,index=False) #We make the csv file using the df parameter
            mpl.imshow(arrL)#Here we display the data as an image to the user
            mpl.show()#Here we display all open figures

class __main__():#Our main class
    sickCattle="./archivosCSV/Enfermos CSV's"#Parameter that contains the location of the sick cattle folder
    compSickCattleFolder="./archivosCSV/Enfermos Comprimidas"#Parameter that contains the location of the compressed sick cattle folder
    uncompSickCattleFolder="./archivosCSV/Enfermos Descomprimidas"#Parameter that contains the location of the uncompressed sick cattle folder
    file=structure()#We called our structure class
    print("Ganado Enfermo\n")
    sickCattleArray=file.dataStructure(sickCattle)#We make an array containing the compressing of the files on Enfermos CSV's folder
    print(sickCattleArray)
    print("\n...Comprimiendo Archivo...\n")
    index=time()#Take the time at the start of the process
    file.compression(compSickCattleFolder,sickCattleArray)#We make the final operation
    fin=time()#Take the time at the end of the process
    print("...Proceso de compresion finalizado...\nTiempo de ejecucion: \n")
    print(fin-index)#We print the execution time of the code
    print("...Descomprimiendo Archivo...\n")
    index1=time()#Take the time at the start of the process
    file.descompresion(compSickCattleFolder,uncompSickCattleFolder)
    fin1=time()#Take the time at the end of the process
    print("...Proceso de descompresion finalizado...\nTiempo de ejecucion:\n")
    print(fin1-index1)#We print the execution time of the code
