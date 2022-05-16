# file made to manually verify no repeated comps
import pandas as pd
from os import listdir, path
import csv   

def checkDupl(data):
    df = pd.DataFrame(data)
    df = df.reset_index()
    for index, row in df.iterrows():
        tempArra = [row['A1'],row['A2'],row['A3'],row['A4'],row['A5']]
        tempArra.sort()
        contador = 0
        for index, row in df.iterrows():
            tempArra2 = [row['A1'],row['A2'],row['A3'],row['A4'],row['A5']]
            tempArra2.sort()
            if tempArra == tempArra2:
                contador += 1   
                if contador > 1:
                    print('Duplicated')  
                    print(tempArra)   

# assign dataset
if __name__ == '__main__':
    for file in listdir('./comps/'):
        if file != ".DS_Store":
            file = './comps/'+file
            print(file)
            data = pd.read_csv(file)
            checkDupl(data)     