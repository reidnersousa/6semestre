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
t=retornaVerticeAdj(l)
print(t)


dictionario ={}
dictionario[l[0][0]]=l[0][1]
dictionario[l[0][0]]=l[1][1]
print(dictionario)

print()


"""
rooms = [[l[r][i]  for r in range(0,50)] for i in range(2)]
#rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

#pprint(rooms)
"""


## ultimo elmeento do 1 é 2162 1 7017
rooms2 = [[l[r][i] for i in range(2)] for r in range(2162)]


pprint(rooms2)

# print(l[46822]) ## ultimo elemento # da lista 