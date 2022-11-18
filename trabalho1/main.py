# importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pprint import pprint
from pprint import pprint

from  funcoes import*
# estilo notebook
sns.set()


# url dos datasets
#url_path = 'https://raw.githubusercontent.com/reidnersousa/6semestre/Teoria-Grafos/GrafoExemplo.txt'
url_path = 'https://raw.githubusercontent.com/reidnersousa/6semestre/Teoria-Grafos/as_graph.txt'
# df recebe o arquivo e transforma em DataFrame
df = pd.read_csv(url_path , sep ='\t',names=["Teste1"])

arrayDi = df['Teste1'].to_numpy()
#print(arrayDi)



l=TransformaNPEmLista(arrayDi)


# print(l[0]) # primeiro elemento da lista  ['1','22']
print(l[0])         # ['1','22']
print(l[0][0])      # 1
print(l[0][1])      # 22 


print()
print(l[1])         # ['1','35']
print(l[1][0])      # 1
print(l[1][1])      # 35

print()
print(l[2])         # ['1','10']
print(l[2][0])      # 1
print(l[2][1])      # 10



print()
t=retornaVerticeAdj(l)
print()

"""
variavel1=10 
variavel2=11
dic={}
dic.update({'nome': (variavel1, variavel2)})

print(type(dic),dic)

"""

## ultimo elmeento do 1 é 2162 1 7017



# print(l[46822]) ## ultimo elemento # da lista 