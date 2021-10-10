import numpy as np
import os
from collections import deque
import pandas as pd
import nearestNeighbor as vc

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
    
    def compression(self,folder,array):
        for i in range(len(array)):  
            ImgCom=vc.compressNeighbor(array[i]["Array"],0.5).astype(np.uint8) 
            df=pd.DataFrame(np.array(ImgCom))
            df.to_csv(folder+"/"+array[i]["Name"],header=None) 
            
    def uncompression(self,originalFolder,newFolder):
        for i in os.listdir(originalFolder):
            im=pd.read_csv(originalFolder+"/"+i) 
            array=vc.uncompressNeighbor(np.array(im),2).astype(np.uint8) 
            df=pd.DataFrame(np.array(array))
            df.to_csv(originalFolder+"/"+i,header=None)
            
class __main__():
    sickCattle="./archivosCSV/Enfermos CSV's" 
    healthyCattle="./archivosCSV/Sanos CSV's"
    compHealthyCattleFolder="./archivosCSV/Sanos Comprimidas"
    compSickCattleFolder="./archivosCSV/Enfermos Comprimidas"
    uncompSickCattleFolder="./archivosCSV/Enfermos Descomprimidas"
    uncompHealthyCattleFolder="./archivosCSV/Sanos Descomprimidas"
    file=structure()
    print("Ganado Enfermo")
    sickCattleArray=file.dataStructure(sickCattle)
    print(sickCattleArray)
    print("\n")
    print("Ganado Sano")
    healthyCattleArray=file.dataStructure(healthyCattle)
    print(healthyCattleArray)
    print("...Comprimiendo Archivo...")
    file.compression(compSickCattleFolder,sickCattleArray)
    file.compression(compHealthyCattleFolder,healthyCattleArray)
    print("...Proceso de compresion finalizado...")
    print("...Descomprimiendo archivo...")
    file.uncompression(compSickCattleFolder,uncompSickCattleFolder)
    file.uncompression(compHealthyCattleFolder,uncompHealthyCattleFolder)
    print("...Proceso de descompresion finalizado...")
