# importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pprint import pprint
"""
from hello import *

world()
"""
from  funcoes import*
# estilo notebook
sns.set()


# url dos datasets
url_path = 'https://raw.githubusercontent.com/reidnersousa/6semestre/Teoria-Grafos/GrafoExemplo.txt'

# df recebe o arquivo e transforma em DataFrame
df = pd.read_csv(url_path , sep ='\t',names=["Teste1"])

arrayDi = df['Teste1'].to_numpy()
print(arrayDi)
n=NumeroDeNo(arrayDi)


print(n)

matrizAdjNula=criarMatrizAdj(n)
pprint(matrizAdjNula)

matrizAdj=setValoresMatriz(arrayDi,matrizAdjNula) # setValoresMatriz ta errado
pprint(matrizAdj)



A,B=SeperandoArrayDi(arrayDi)

print(A,B)

rotas=CriarRotas(A,B)
print(rotas)