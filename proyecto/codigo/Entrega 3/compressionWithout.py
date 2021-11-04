import numpy as np
import os
from collections import deque
import pandas as pd
import LZ77 as lz
import nearestNeighbor as vc
import matplotlib.pyplot as plt
from time import time

class structure():
    def dataStructure(self,cattle):
        file=os.listdir(cattle) 
        cattleArray=deque()
        for i in range(len(file)):
            dict={}
            dict["Name"]=file[i]
            address=cattle+"/"+file[i]
            data=pd.read_csv(address,header=None)
            array=np.asarray(data) 
            dict["Array"]=array
            cattleArray.append(dict)
        return cattleArray 
    
    def compressionWithout(self,folder,array):
        for i in range(len(array)):
            rows,columns = arreglo[i]["arreglo"].shape
            compressor=lz.LZ77(30)
            ImgCom=vc.compressNeighbor(array[i]["Array"],0.25).astype(np.uint8) 
            Concatenating=np.concatenate(ImgCom)
            origin=list(Concatenating)
            ImgCon2=compressor.compress(origin)
            df=pd.DataFrame(np,array(ImgCon2))
            df.to_csv(folder+"/"+array[i]["Name"],header=None) 
            plt.imshow(ImgCon2)
            plt.show()
            
class __main__():
    sickCattle="./archivosCSV/Enfermos CSV's" 
    compSickCattleFolder="./archivosCSV/Enfermos Comprimidas"
    uncompSickCattleFolder="./archivosCSV/Enfermos Descomprimidas"
    file=structure()
    print("Ganado Enfermo")
    sickCattleArray=file.dataStructure(sickCattle)
    print(sickCattleArray)
    print("\n")
    print("...Comprimiendo Archivo...")
    inicio=time()
    file.compression(compSickCattleFolder,sickCattleArray)
    fin=time()
    print(fin-inicio)
    print("...Proceso de compresion finalizado...")
