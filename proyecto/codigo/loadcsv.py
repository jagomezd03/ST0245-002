import pandas as pd
import numpy as np
import os

livestockHealthy = "csv/sano_csv"
livestockSick = "csv/enfermo_csv"
listHealthy=os.listdir(livestockHealthy)
listSick=os.listdir(livestockSick)

for i in range(len(listSick)):
    address=livestockHealthy+"/"+listSick[i]
    data=pd.read_csv(address,header=None)
    arraySick=np.asarray(data)
    print(arraySick)

for i in range(len(listHealthy)):
    address=livestockHealthy+"/"+listHealthy[i]
    data=pd.read_csv(address,header=None)
    arrayHealthy=np.asarray(data)
    print(arrayHealthy)